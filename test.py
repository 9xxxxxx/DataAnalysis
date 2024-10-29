import pandas as pd
import re
import os

path = r"退换运营报表数据分析\源数据\销售退仓10-21.xlsx"
date = re.search(r'\d+-\d+',path)
outpath = fr'退换运营报表数据分析\分析输出\{date[0]}退换货运营汇总表.xlsx'

df = pd.read_excel(path, header=0)
excel_writer = pd.ExcelWriter(outpath, engine='openpyxl')

def match(df):
    # df = pd.read_excel('退换运营报表数据分析\源数据\销售退仓10-16.xlsx',usecols=['商品编码','数量'], sheet_name='Sheet1')
    df_original = df
    df_matching = pd.read_excel('我的映射表.xlsx',sheet_name='究极完整')    

    df_original.rename(columns={'商品编码':'物料编码'},inplace=True)

    # 假设原表中的匹配列为'key_column'，要提取的列为'value_column'
    # 匹配表中的对应列也为'key_column'，要提取的列为'value_column'
    merged_df = pd.merge(df_original, df_matching[['物料编码', '无颜名称', '产品类型']], on='物料编码', how='left')
    merged_df['汇总数量'] = merged_df.groupby('无颜名称')['数量'].transform('sum')
    merged_df.sort_values('汇总数量',inplace=True,ascending=False)
    # 将合并后的数据写回原表
    merged_df.drop_duplicates('无颜名称', inplace=True)
    # merged_df.to_excel('merged_output.xlsx', index=False)
    return merged_df  

def dealexgoods():
    #获取换货的分类报表
    exgoods = df.query("售后分类 == '换货'")[['商品编码','商品名称','数量']]
    exgoods = match(exgoods)

    exgoods.rename(columns={'汇总数量':'换货数量'}, inplace=True)
    summary = exgoods.groupby('无颜名称').agg({'换货数量': 'sum'}).reset_index()

    exgoods.drop('数量', axis=1, inplace=True)

    exgoods.to_excel(excel_writer, sheet_name='换货型号未汇总', index=False)
    summary.to_excel(excel_writer, sheet_name='换货型号汇总', index=False)
    print("提取完成，结果已保存 ----")

    return exgoods,summary

def dealreturngoods():
    #获取退货的分类报表
    returngoods = df.query("售后分类 == '拒收退货' or 售后分类 == '普通退货'")[['商品编码','商品名称','数量']]
    returngoods = match(returngoods)

    returngoods.rename(columns={'汇总数量': "退货数量"}, inplace=True)

    summary = returngoods.groupby('无颜名称').agg({'退货数量': 'sum'}).reset_index()
    returngoods.drop('数量', axis=1, inplace=True)
    # # 按型号分组汇总

    returngoods.to_excel(excel_writer, sheet_name='退货型号未汇总', index=False)
    summary.to_excel(excel_writer, sheet_name='退货型号汇总', index=False)
    print("提取完成，结果已保存 --", )
    return returngoods,summary
    
def dealallgoods():
    exgoods,exsummary = dealexgoods()
    regoods,resummary = dealreturngoods()
    merged_count_df = pd.concat([exsummary, resummary],ignore_index=True)
    merged_count_df = merged_count_df.groupby('无颜名称').agg({'换货数量':'sum', '退货数量': 'sum'}).reset_index()
    merged_notcount_df= pd.concat([exgoods, regoods],ignore_index=True)
    merged_count_df.fillna(0,inplace=True)
    merged_notcount_df.fillna(0,inplace=True)
   
    merged_notcount_df.to_excel(excel_writer, sheet_name='退换货型号未汇总',index=False)
    merged_count_df.to_excel(excel_writer, sheet_name="退换货型号汇总", index=False)
    print("提取完成，结果已保存 --", )
    return merged_notcount_df
   
def separate():
    df = dealallgoods()
    df_part = df.query("产品类型 == '电吹风配件' or 产品类型 == '电动牙刷配件'")
    df_product = df.query("产品类型 == '电吹风' or 产品类型 == '电动牙刷'")
    df_part = df_part.groupby('无颜名称').agg({'换货数量':'sum', '退货数量': 'sum', }).reset_index()
    df_product = df_product.groupby('无颜名称').agg({'换货数量':'sum', '退货数量': 'sum'}).reset_index()

 
    df_part.to_excel(excel_writer, sheet_name='退换货配件easyfill', index=False)
    df_product.to_excel(excel_writer, sheet_name='退换货整机easyfill', index=False)
    print("提取完成，结果已保存---", )

def main():
    _ = input('即将开始执行：按任意键继续-------')
    separate()
    excel_writer.close()
    print('done!!!!!-----------------------------!!!!!！')
    

main()

