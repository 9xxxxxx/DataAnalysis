import pandas as pd
import re
from tqdm import tqdm


path = r"退换运营报表数据分析\源数据\销售退仓10-20.xlsx"
date = re.search(r'\d+-\d+',path)
exoutpath = fr"退换货数据输出文件夹\{date[0]}换货运营汇总表.xlsx" 
returnoutpath = fr'退换货数据输出文件夹\{date[0]}退货运营汇总表.xlsx'
outpath = fr'退换货数据输出文件夹\{date[0]}退换货运营汇总表.xlsx'
output_file = fr'退换货数据输出文件夹\{date[0]}easytofill.xlsx'
separate_pattern = [r'支架', r'气垫梳', r'收纳包', r'风嘴', r'刷头',r'毛巾',r'干发帽',r'文件袋', r'适配器',r'转换器',r'旅行盒',r'手提袋']

df = pd.read_excel(path,sheet_name='导出筛选结果', header=0)
# df['商品名称'] = df['商品名称'].str.replace(' ', '')

# 型号匹配
model_pattern = {
 '电动牙刷电机套（铝合金、不锈钢共用）': '电动牙刷电机套（铝合金、不锈钢共用）',
 '电池支架（铝合金、不锈钢共用）': '电池支架（铝合金、不锈钢共用）',
 '徕芬新一代高速家用吹风机': 'LF03',
 'MOS管（替代）': 'MOS管（替代）',
 '铝合金电动牙刷': '铝合金 电动牙刷',
 '不锈钢电动牙刷': '不锈钢 电动牙刷',
 '迷你磁吸支架': '迷你磁吸支架',
 '圣菲特干发帽': '圣菲特干发帽',
 '维修-电吹风': 'LF02',
 '洁丽雅毛巾': '洁丽雅毛巾w0191',
 '顺丰文件袋': '顺丰文件袋',
 '静水干发帽': '洁玉静水干发帽DST2-013',
 '不锈钢': 'T91 不锈钢',
 '铝合金': 'T91 铝合金',
 '塑胶版': 'T91 ABS',
 '塑胶': 'T91 ABS',
 '电动牙刷': '电动牙刷',
 'HD30MINIlite': 'HD30 MINIlite',
 'LFHDMINIlite': 'LFHD MINIlite',
 'LFHDSE-Lite': 'LFHD SE-Lite',
 'LF03&LF03SE': 'LF03&LF03SE',
 'HD31MINI': 'HD31 MINI',
 'LFHDMINI': 'LFHD MINI',
 'MINIlite': 'MINI Lite',
 'MiniLite': 'MINI Lite',
 'LF04MINI': 'LF04MINI',
 'MINILITE': 'MINILITE',
 'LFHDSE2': 'LFHD SE 2',
 'LF03SE': 'LF03 SE',
 'LF03-SE':'LF03-SE',
 'LF03-S':'LF03-S',
 'LF03': 'LF03',
 'LF02': 'LF02',
 'SE': 'LF03 SE',
 'se': 'LF03 SE',
 }
 
# 字典排序
# sorted_by_key_length = dict(sorted(pattern.items(), key=lambda item: len(item[0]), reverse=True),)

# 配件匹配
part_pattern = {
 '羊毛毡支架 PC 注塑 灰色(PT427U)': '羊毛毡支架 PC 注塑 灰色(PT427U)',
 '标准热缩膜（装带滤波器）LF02共用': '标准热缩膜（装带滤波器）LF02共用',
 '电机套 （铝合金、不锈钢共用）': '电机套 （铝合金、不锈钢共用）',
 '情人节礼盒-粉色-底盒标签': '情人节礼盒-粉色-底盒标签',
 '情人节礼盒-蓝色-底盒标签': '情人节礼盒-蓝色-底盒标签',
 '情人节礼盒国内底盒标签':'情人节礼盒国内底盒标签',
 'USB-C转USB转换器': 'USB-C转USB转换器',
 '旅行盒紫色适配ABS版': '旅行盒 适配ABS版',
 '旅行盒粉色适配ABS版': '旅行盒 适配ABS版',
 '旅行盒白色适配ABS版': '旅行盒 适配ABS版',
 '发热丝组件（220V)': '发热丝组件（220V)',
 '壁挂支架(ABS款)': '壁挂支架(ABS款)',
 'Pogopin转换器': 'USB-C转磁吸Pogopin转换器',
 '壁挂支架(金属款)': '壁挂支架(金属款)',
 '白盒封盒贴纸（上）': '白盒封盒贴纸（上）',
 '白盒封盒贴纸（下）': '白盒封盒贴纸（下）',
 '新包胶刷头单支装': '新包胶刷头单支装',
 '拨动温控开关组件': '拨动温控开关组件',
 '电源线标准1.7M':'电源线1.7M',
 '电源线标准1.5M':'电源线1.5M',
 '铝合金 主体外壳': '铝合金 主体外壳',
 '电机轴防水软胶': '电机轴防水软胶',
 '档位开关座压板': '档位开关座压板',
 '刷头套盒3支装': '刷头套盒3支装',
 '刷头套盒6支装': '刷头套盒6支装',
 '导风嘴带螺丝孔':'导风嘴带螺丝孔', 
 '双色把手内壳上':'双色把手内壳上',
 'USB-C电源': 'USB-C电源适配器',
 '包胶刷头单支装': '包胶刷头单支装',
 '导风嘴220V': '导风嘴220V',
 '磁吸壁挂支架': '磁吸壁挂支架',
 '电源线连插头': '电源线连插头',
 '磁吸顺滑风嘴': '磁吸顺滑风嘴',
 '礼盒版手提袋': '礼盒版手提袋',
 '温度调节按钮': '温度调节按钮',
 '开关风速按钮': '开关风速按钮',
 '风速开关按钮': '风速开关按钮',
 '温控开关按钮': '温控开关按钮',
 '返工底盒标签': '返工底盒标签',
 '电源线尾座': '电源线尾座',
 '标准热缩膜': '标准热缩膜',
 '旅行收纳包': '旅行收纳包',
 '独立装刷头': '独立装刷头',
 'USB-A': 'USB-A转TYPE-C转换器',
 '仿绒收纳袋': '仿绒收纳袋',
 '铁片固定座': '铁片固定座',
 '数据线套装': '数据线套装',
 '导风嘴组件': '导风嘴组件',
 '双色导风嘴': '双色导风嘴',
 '开关保护盖':'开关保护盖',
 '电源线压块': '电源线压块',
 '双色内壳上': '双色内壳上',
 '把手内壳下': '把手内壳下',
 '收纳包外盒': '收纳包外盒',
 '羊毛毡支架': '羊毛毡支架',
 '仿绒收纳袋': '仿绒收纳袋',
 '1500W': '外壳1500W',
 '温控开关板': '温控开关板',
 '壁挂支架': '壁挂支架',
 '风筒外壳': '风筒外壳',
 '把手外壳': '把手外壳',
 '电线尾座': '电线尾座',
 '开关滑片': '开关滑片',
 '顺滑风嘴':'顺滑风嘴',
 '后盖组件': '后盖组件',
 '迷你支架': '迷你支架',
 '风嘴铁环': '风嘴铁环',
 '外滤网': '外滤网',
 '外壳带': '外壳带',
 '束线带': '束线带',
 '内滤网': '内滤网',
 '收纳包': '收纳包',
 '聚风嘴': '聚风嘴',
 '外滤网': '外滤网',
 '气垫梳': '气垫梳',
 '69码': '69码',
 '后盖上': '后盖上',
 '后盖': '后盖',
 '外壳': '外壳',
 '铁环': '铁环',
 '底盖': '底盖'}

# 自定义函数进行匹配
def match_and_label(row):
    for key, value in tqdm(model_pattern.items(), desc = 'Processing'):
        # 使用正则表达式确保精确匹配
        if re.search(re.escape(key) , row['商品名称']):
            return value  # 找到第一个匹配，立即返回
    return ''  # 如果没有匹配，返回无匹配

def match2time(row):
    for key, value in tqdm(part_pattern.items(), desc = 'Processing'):
        # 使用正则表达式确保精确匹配
        if re.search(re.escape(key), row['商品名称']):
            return row['型号'] + ' ' + value  # 找到第一个匹配，立即返回
    return row['型号']  # 如果没有匹配，返回无匹配



def dealexgoods():
    #获取换货的分类报表
    exgoods = df.query("售后分类 == '换货'")[['商品名称','数量']]

    exgoods.rename(columns={'数量':'换货数量'}, inplace=True)
    # 按名称汇总
    exgoods = exgoods.groupby('商品名称')['换货数量'].sum().reset_index()
    # exgoods.to_excel(exoutpath,index=False)
    exgoods.insert(1,'型号','')

    # exgoods = exgoods.drop_duplicates(subset='商品名称')
    #按型号分组
    exgoods['商品名称'] = exgoods['商品名称'].str.replace(' ','')
    exgoods['型号'] = exgoods.apply(match_and_label, axis=1)
    exgoods['型号'] = exgoods.apply(match2time, axis=1)
    
    # 按型号分组汇总
    summary = exgoods.groupby('型号').agg({'换货数量': 'sum'}).reset_index()
    # 计算总和
    total_row = pd.DataFrame({'型号': ['Total'], '换货数量': [summary['换货数量'].sum()]})
    # 添加总和行
    summary= pd.concat([summary, total_row], ignore_index=True)

    with pd.ExcelWriter(exoutpath) as writer:
        exgoods.to_excel(writer, sheet_name='型号未汇总', index=False)
        summary.to_excel(writer, sheet_name='型号汇总', index=False)
    # exgoods.to_excel(exoutpath,index=False)
    # summary.to_excel(exoutpath0, index=False)
    return summary

def dealreturngoods():
    #获取退货的分类报表
    returngoods = df.query("售后分类 == '拒收退货' or 售后分类 == '普通退货'")[['商品名称','数量']]
    # print(returngoods)
    returngoods.rename(columns={'数量': "退货数量"}, inplace=True)
    # 按双排名称分组
    returngoods = returngoods.groupby('商品名称')['退货数量'].sum().reset_index()
    returngoods.insert(1,'型号','')
    # # returngoods = returngoods.drop_duplicates(subset='商品名称') 
    # 匹配型号
    returngoods['商品名称'] = returngoods['商品名称'].str.replace(' ', '')
    returngoods['型号'] = returngoods.apply(match_and_label, axis=1)
    returngoods['型号'] = returngoods.apply(match2time, axis=1)

    summary = returngoods.groupby('型号').agg({'退货数量': 'sum'}).reset_index()
    total_row = pd.DataFrame({'型号': ['Total'], '退货数量': [summary['退货数量'].sum()]})
    summary= pd.concat([summary, total_row], ignore_index=True)

    # # 按型号分组汇总
    with pd.ExcelWriter(returnoutpath) as writer:
        returngoods.to_excel(writer, sheet_name='型号未汇总', index=False)
        summary.to_excel(writer, sheet_name='型号汇总', index=False)
    # returngoods.to_excel(returnoutpath,index=False)
    # summary.to_excel(returnoutpath0,index=False)
    return summary
    
def dealallgoods():
    exsummary = dealexgoods()
    resummary = dealreturngoods()
    merged_df = pd.merge(exsummary, resummary, on='型号',how='outer')
    merged_df.fillna(0, inplace=True)
    # 找到要移动的行，例如按某列条件筛选
    row_to_move = merged_df[merged_df['型号'] == 'Total']
    # 删除该行
    merged_df = merged_df[merged_df['型号'] != 'Total']
    # 将该行添加到末尾
    merged_df = pd.concat([merged_df, row_to_move])
    merged_df.to_excel(outpath, index=False)

def separategoods(outpath):
    # 读取数据
    df = pd.read_excel(outpath)
    # 将多个条件组合成一个正则表达式
    combined_pattern = '|'.join(separate_pattern)
    # 找到匹配的行
    matched_rows = df[df.iloc[:, 0].astype(str).str.contains(combined_pattern, na=False)]
    # 删除源文件中匹配的行
    remaining_rows = df[~df.index.isin(matched_rows.index)]
    # 将提取的行和剩余的行分别保存到新的Excel文件
    with pd.ExcelWriter(output_file) as writer:
        matched_rows.to_excel(writer, sheet_name='配件', index=False)
        remaining_rows.to_excel(writer, sheet_name='整机', index=False)
    print("提取完成，结果已保存到", output_file)

def main():
    
    dealallgoods()
    separategoods(outpath)
    print('done!!!!!-----------------------------!!!!!！')

main()
