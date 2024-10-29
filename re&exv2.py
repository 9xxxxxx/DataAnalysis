from datetime import date, timedelta
import pandas as pd
path = fr"退换运营报表数据分析\源数据\销售退仓{date}.xlsx"

df = pd.read_excel(path, header=0, sheet_name='Sheet1')

def match(df):
    # df = pd.read_excel('退换运营报表数据分析\源数据\销售退仓10-16.xlsx',usecols=['商品编码','数量'], sheet_name='Sheet1')
    df_original = df
    df_matching = pd.read_excel('我的映射表.xlsx',sheet_name='究极完整')    

    df_original.rename(columns={'商品编码':'物料编码'},inplace=True)

    # 假设原表中的匹配列为'key_column'，要提取的列为'value_column'
    # 匹配表中的对应列也为'key_column'，要提取的列为'value_column'
    merged_df = pd.merge(df_original, df_matching[['物料编码', '型号名称', '产品类型']], on='物料编码', how='left')
    merged_df['汇总数量'] = merged_df.groupby('型号名称')['数量'].transform('sum')
    merged_df.sort_values('汇总数量',inplace=True,ascending=False)
    merged_df.drop_duplicates('型号名称', inplace=True)
    return merged_df  


def dealfixgoods(df):
    fixgoods = df.query("售后分类 == '维修'")[['商品编码','商品名称','数量']]
    fixgoods = match(fixgoods)

    fixgoods.rename(columns={'汇总数量':'维修数量'}, inplace=True)
    
    summary = fixgoods.groupby('型号名称').agg({'换货数量': 'sum', '产品类型': lambda x:'-'.join(x)}).reset_index()
    summary['产品类型'] = summary['产品类型'].apply(lambda x:x.split('-')[0])


    fixgoods.drop('数量', axis=1, inplace=True)

    fixgoods.to_excel(excel_writer, sheet_name='维修型号未汇总', index=False)
    summary.to_excel(excel_writer, sheet_name='维修型号汇总', index=False)

    print("提取完成，结果已保存 ----")
    return fixgoods,summary

def dealexgoods(df):
    #获取换货的分类报表
    exgoods = df.query("售后分类 == '换货'")[['商品编码','商品名称','数量']]
    exgoods = match(exgoods)

    exgoods.rename(columns={'汇总数量':'换货数量'}, inplace=True)
    summary = exgoods.groupby('型号名称').agg({'换货数量': 'sum', '产品类型': lambda x:'-'.join(x)}).reset_index()
    summary['产品类型'] = summary['产品类型'].apply(lambda x:x.split('-')[0])


    exgoods.drop('数量', axis=1, inplace=True)

    exgoods.to_excel(excel_writer, sheet_name='换货型号未汇总', index=False)
    summary.to_excel(excel_writer, sheet_name='换货型号汇总', index=False)
    print("提取完成，结果已保存 ----")

    return exgoods,summary

def dealreturngoods(df):

    #获取退货的分类报表
    returngoods = df.query("售后分类 == '拒收退货' or 售后分类 == '普通退货'")[['商品编码','商品名称','数量']]
    returngoods = match(returngoods)

    returngoods.rename(columns={'汇总数量': "退货数量"}, inplace=True)

    summary = returngoods.groupby('型号名称').agg({'退货数量': 'sum','产品类型': lambda x:'-'.join(x)}).reset_index()
    summary['产品类型'] = summary['产品类型'].apply(lambda x:x.split('-')[0])

    returngoods.drop('数量', axis=1, inplace=True)
    # # 按型号分组汇总

    returngoods.to_excel(excel_writer, sheet_name='退货型号未汇总', index=False)
    summary.to_excel(excel_writer, sheet_name='退货型号汇总', index=False)
    print("提取完成，结果已保存 --", )
    return returngoods,summary
    
def dealallgoods(df):
    exgoods,exsummary = dealexgoods(df)
    regoods,resummary = dealreturngoods(df)

    merged_count_df = pd.concat([exsummary, resummary,],ignore_index=True)
    merged_count_df = merged_count_df.groupby('型号名称').agg({'换货数量':'sum', '退货数量': 'sum','产品类型':lambda x:'-'.join(x) }).reset_index()
    merged_count_df['产品类型'] = merged_count_df['产品类型'].apply(lambda x:x.split('-')[0])

    merged_notcount_df= pd.concat([exgoods, regoods],ignore_index=True)

    merged_count_df.fillna(0,inplace=True)
    merged_notcount_df.fillna(0,inplace=True)
   
    
    merged_notcount_df.to_excel(excel_writer, sheet_name='退换货型号未汇总',index=False)
    merged_count_df.to_excel(excel_writer, sheet_name="退换货型号汇总", index=False)
    print("提取完成，结果已保存 --", )
    return merged_notcount_df
   
def separate(df):
    df = dealallgoods(df)
    df_part = df.query("产品类型 == '电吹风配件' or 产品类型 == '电动牙刷配件' or  产品类型 == '其他'")
    df_product = df.query("产品类型 == '电吹风' or 产品类型 == '电动牙刷'")
    df_part = df_part.groupby('型号名称').agg({'换货数量':'sum', '退货数量': 'sum','产品类型':lambda x:'-'.join(x) }).reset_index()
    df_product = df_product.groupby('型号名称').agg({'换货数量':'sum', '退货数量': 'sum','产品类型':lambda x:'-'.join(x)}).reset_index()

    df_part['产品类型'] = df_part['产品类型'].apply(lambda x:x.split('-')[0])
    df_product['产品类型'] = df_product['产品类型'].apply(lambda x:x.split('-')[0]) 

    df_part.to_excel(excel_writer, sheet_name='退换货配件easyfill', index=False)
    df_product.to_excel(excel_writer, sheet_name='退换货整机easyfill', index=False)
    print("提取完成，结果已保存---", )

def main(path):
    df = pd.read_excel(path, header=0, sheet_name='Sheet1')
    # _ = input('即将开始执行：按任意键继续-------')
    separate(df)
    excel_writer.close()
    print(f"{path.split('\\')[-1]}提取完成，已保存到输入文件夹----------~~")




today = date.today()
date = today - timedelta(days=1)
date = f'{date.month}-{date.day}'
path = fr"退换运营报表数据分析\源数据\销售退仓{date}.xlsx"
outpath = fr'退换运营报表数据分析\分析输出\退换货运营汇总表{date}.xlsx'
excel_writer = pd.ExcelWriter(outpath, engine='openpyxl')
main(path)


