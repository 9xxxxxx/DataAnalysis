import pandas as pd
import re
from tqdm import tqdm



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
 '电源线': '电源线',
 '69码': '69码',
 '后盖上': '后盖上',
 '后盖': '后盖',
 '外壳': '外壳',
 '铁环': '铁环',
 '底盖': '底盖'}

color_pattern = {
    '白色':'白色',
    "金粉":'金粉',
    '黄色':'黄色',
    '粉色':'粉色',
    '蓝色':'蓝色',
    '简白':'简白',
    '紫色':'紫色',
    '紫色':'紫色',
    '奶茶':'奶茶',
    '闪银':'闪银',
    '中国红':'中国红',
    '冰川蓝':'冰川蓝',
    '深灰':'深灰',
    '镜黑':'镜黑',
    '樱粉':'樱粉',
    '皓月白':'皓月白',
    '梦幻紫':'梦幻紫',
    '绿野':'绿野',
    '浅蓝':'浅蓝',
    '牛奶粉':'牛奶粉',
    '抹茶绿':'抹茶绿',
    '圣诞蓝金':'圣诞蓝金',
    '青柚':'青柚',
    '白金':'白金',
    '熔岩红':'熔岩红',
    '蓝金':'蓝金',
    '浅紫':'浅紫',
    '亮白':'亮白',
    '浅粉':'浅粉',
    '浅灰':'浅灰',
    '浅绿':'浅绿',
    '透明':'透明',
    '蓝灰色':'蓝灰',
    '蓝灰':'蓝灰',
    '粉金':'粉金',
    '灰色':'灰色',
    '星空银':'星空银',
    '绿色':'绿色',
    '星空紫':'星空紫',
    '银色':'银色',
    '深蓝':'深蓝',
    '冰川银':'冰川银',
    '青山绿':'青山绿',
    '深空灰':'深空灰',
    '白+黄':'白+黄',
    '光感白':'光感白',
    '幻夜黑':'幻夜黑',
    '浅岛绿':'浅岛绿',
    '极光蓝':'极光蓝'

}
def match_color(row):
    for key, value in tqdm(color_pattern.items(), desc='FUCKING PROCESSING.......'):
        if re.search(re.escape(key), row['物料名称']):
            return row['型号'] + value
    return row['型号']

# 去除名称重复字段
def remove_duplicates(s):
    seen = set()
    unique_words = []
    for word in s.split():  # 按空格分割字符串
        if word not in seen:
            seen.add(word)
            unique_words.append(word)
    return ' '.join(unique_words)  # 重新连接成字符串

# 自定义函数进行匹配
def match_and_label(row):
    for key, value in tqdm(model_pattern.items(), desc = 'Processing'):
        # 使用正则表达式确保精确匹配
        if re.search(re.escape(key) , row['物料名称']):
            return value  # 找到第一个匹配，立即返回
    return ''  # 如果没有匹配，返回无匹配

def match2time(row):
    for key, value in tqdm(part_pattern.items(), desc = 'Processing'):
        # 使用正则表达式确保精确匹配
        if re.search(re.escape(key), row['物料名称']):
            # 如果匹配重复返回原始值
            # if re.search(re.escape(value), row['物料名称']):
            #     return row['型号']
            # else:
                return row['型号'] + ' ' + value  # 找到第一个匹配，立即返回
    return row['型号']  # 如果没有匹配，返回原始值

def dealexgoods():
    df = pd.read_excel('备件良品仓.xlsx')
    #获取换货的分类报表
    # exgoods = df.query("售后分类 == '换货'")[['物料名称','数量']]

    # exgoods.rename(columns={'数量':'换货数量'}, inplace=True)
    # 按名称汇总
    # exgoods = exgoods.groupby('物料名称')['换货数量'].sum().reset_index()
    # exgoods.to_excel(exoutpath,index=False)
    # exgoods.insert(1,'型号','')

    # exgoods = exgoods.drop_duplicates(subset='物料名称')
    #按型号分组
    df.insert(5,'占比',0)
    df['数量(库存)'] = df['数量(库存)'].astype(int)
    df['60天以上'] = df['60天以上'].astype(int)
    df['物料名称'] = df['物料名称'].astype(str)
    df['物料名称'] = df['物料名称'].str.replace(' ','')
    df['型号'] = df.apply(match_and_label, axis=1)
    # df['型号'] = df.apply(match_color, axis=1)
    df['型号'] = df.apply(match2time, axis=1)
 
    # total_row0 = pd.DataFrame({'物料名称': ['Total'], '数量(库存)': [df['数量(库存)'].sum()],'60天以上': [df['60天以上'].sum()]})
    # df = pd.concat([df, total_row0], ignore_index=True)
    df['占比'] = df['60天以上']/df['数量(库存)']
    df['型号'] = df['型号'].apply(remove_duplicates)
    df = df.sort_values(by='60天以上', ascending=False)
    
    with pd.ExcelWriter('输出.xlsx') as writer:
        df.to_excel(writer, sheet_name='型号未汇总', index=False)
    return df
    # exgoods.to_excel(exoutpath,index=False)
    # summary.to_excel(exoutpath0, index=False)
    # return summary
  

def count():
# 按型号分组汇总
    df = pd.read_excel('输出.xlsx')
    summary = df.groupby('型号').agg({'数量(库存)':'sum','60天以上': 'sum'}).reset_index()
    # 计算总和
    total_row = pd.DataFrame({'型号': ['Total'], '数量(库存)': [summary['数量(库存)'].sum()],'60天以上': [summary['60天以上'].sum()]})

    # 添加总和行
    summary= pd.concat([summary, total_row,], ignore_index=True)
    summary.insert(3,'占比',0)
    summary['占比'] = summary['60天以上']/summary['数量(库存)']
    summary = summary.sort_values(by='60天以上',ascending=False)
    with pd.ExcelWriter('汇总.xlsx') as writer:
        summary.to_excel(writer, sheet_name='型号汇总', index=False)

dealexgoods()
count()
print('DONe!!!')
