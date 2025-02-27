import pandas as pd
import re
from tqdm import tqdm

tqdm.pandas(desc='FUCKING PROGRESSING')
model_pattern = {
 '徕芬新一代高速家用吹风机': 'LF03',
 '电动牙刷情人节礼盒-手提袋':'电动牙刷情人节礼盒-手提袋',
 '电动牙刷充电线':'电动牙刷充电线',
 '洁玉静水干发帽DST2-013':'洁玉静水干发帽DST2-013',
 'S9511淡雅灰大圆按摩梳':'S9511淡雅灰大圆按摩梳',
 'S9516淡雅灰卷发梳':'S9516淡雅灰卷发梳',
 '铝合金电动牙刷': '铝合金 电动牙刷',
 '电吹风收纳袋':'电吹风收纳袋',
 '不锈钢电动牙刷': '不锈钢 电动牙刷',
 '不锈钢': 'T91 不锈钢',
 '铝合金': 'T91 铝合金',
 '塑胶版': 'T91 ABS',
 '塑胶': 'T91 ABS',
 'ABS版':'T91 ABS',
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
 'LF01':'LF01',
 '电吹风':'电吹风',
 '吹风机':'吹风机',
 }

part_pattern = {
 '羊毛毡支架 PC 注塑 灰色(PT427U)': '羊毛毡支架 PC 注塑 灰色(PT427U)',
 '标准热缩膜（装带滤波器）LF02共用': '标准热缩膜（装带滤波器）LF02共用',
 '电机套 （铝合金、不锈钢共用）': '电机套 （铝合金、不锈钢共用）',
 '情人节礼盒-粉色-底盒标签': '情人节礼盒-粉色-底盒标签',
 '情人节礼盒-蓝色-底盒标签': '情人节礼盒-蓝色-底盒标签',
 '情人节礼盒-紫色-底盒标签': '情人节礼盒-紫色色-底盒标签',
 '情人节礼盒-白色-底盒标签': '情人节礼盒-白色-底盒标签',
 '情人节礼盒-黄色-底盒标签': '情人节礼盒-黄色-底盒标签',
 '情人节礼盒-绿色-底盒标签': '情人节礼盒-绿色-底盒标签',
 '情人节礼盒-奶茶色-底盒标签': '情人节礼盒-奶茶色-底盒标签',
 '情人节礼盒国内底盒标签':'情人节礼盒国内底盒标签',
 'USB-C转USB转换器': 'USB-C转USB转换器',
 '电动牙刷旅行盒白色':'电动牙刷旅行盒白色',
 '电动牙刷透明护龈刷头':'电动牙刷透明护龈刷头',
 '电动牙刷适配器套装':'电动牙刷适配器套装',
 '旅行盒紫色适配ABS版': '旅行盒 适配ABS版',
 '旅行盒粉色适配ABS版': '旅行盒 适配ABS版',
 '旅行盒白色适配ABS版': '旅行盒 适配ABS版',
 '旅行盒蓝色适配ABS版': '旅行盒适配ABS版',
 '旅行盒奶茶色适配ABS版': '旅行盒 适配ABS版',
 '旅行盒黄色适配ABS版': '旅行盒 适配ABS版',
 '旅行盒绿色适配ABS版':'旅行盒 适配ABS版',
 '旅行盒黑色适配ABS版':'旅行盒 适配ABS版',
 '旅行盒紫色刷头通配适配ABS版' : '旅行盒刷头 通配适配ABS版',
 '旅行盒蓝色刷头通配适配ABS版' : '旅行盒刷头 通配适配ABS版',
 '旅行盒粉色刷头通配适配ABS版': "旅行盒刷头 通配适配ABS版",
 '旅行盒白色刷头通配适配ABS版': "旅行盒刷头 通配适配ABS版",
 '旅行盒奶茶色刷头通配适配ABS版': "旅行盒刷头 通配适配ABS版",
 '旅行盒黑色刷头通配适配ABS版': "旅行盒刷头 通配适配ABS版",
 '旅行盒黄色刷头通配适配ABS版': "旅行盒刷头 通配适配ABS版",
 '旅行盒绿色色刷头通配适配ABS版': "旅行盒刷头 通配适配ABS版",
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
 '迷你磁吸支架':'迷你磁吸支架',
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
 '扩散风嘴': '扩散风嘴',
 '开关滑片': '开关滑片',
 '顺滑风嘴':'顺滑风嘴',
 '后盖组件': '后盖组件',
 '迷你支架': '迷你支架',
 '风嘴铁环': '风嘴铁环',
 '外滤网': '外滤网',
 '外壳带': '外壳带',
 '束线带': '束线带',
 '内滤网': '内滤网',
 '收纳袋': '收纳袋',
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

def match_and_label(row):
    for key, value in tqdm(model_pattern.items(), desc = 'Processing'):
        # 使用正则表达式确保精确匹配
        if re.search(re.escape(key) , row['物料名称']):
            return value  # 找到第一个匹配，立即返回
    return ''  # 如果没有匹配，返回无匹配、

def match_and_part(row):
    for key, value in tqdm(part_pattern.items(), desc = 'Processing'):
        # 使用正则表达式确保精确匹配
        if re.search(re.escape(key), row['物料名称']):
            return row['型号'] + ' ' + value  # 找到第一个匹配，立即返回
    return row['型号']  # 如果没有匹配，返回无匹配

def getmodel():
    df = pd.read_excel('3-10月配件进出仓情况.xlsx',sheet_name='调出不良')
    df = df.astype('str')
    df['物料名称'] = df['物料名称'].str.replace(' ','')
    df.insert(1,'型号','')
    df.insert(2,"数量",1)
    df['型号'] = df.progress_apply(match_and_label, axis=1)
    # df['型号'] = df.progress_apply(match_and_part, axis=1)
    df.to_excel('调出不良.xlsx',index=False)
    print("done!!!")

getmodel()
tqdm.pandas(desc="ENDING---------------~!")