
import pprint
from collections import OrderedDict

model_pattern = {
 '徕芬新一代高速家用吹风机': 'LF03',
 '充电线+转接头':'充电线+转接头',
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
 '手提袋':'手提袋',
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
    '羊毛毡支架 PC 注塑 灰色PT427U', '羊毛毡支架 PC 注塑 灰色PT427U',
    '护龈刷头缓震款透明3支装/新包胶刷头', '护龈刷头缓震款透明3支装/新包胶刷头',
    '护龈刷头缓震款透明6支装/新包胶刷头', '护龈刷头缓震款透明6支装/新包胶刷头',
    '标准热缩膜（装带滤波器）LF02共用', '标准热缩膜（装带滤波器）LF02共用',
    '护龈刷头缓震款透明3支装/包胶刷头', '护龈刷头缓震款透明3支装/包胶刷头',
    '护龈刷头缓震款透明单支装/包胶刷头', '护龈刷头缓震款透明单支装/包胶刷头',
    '旅行盒奶茶色刷头通配适配ABS版', '旅行盒奶茶色刷头通配适配ABS版',
    '旅行盒绿色色刷头通配适配ABS版', '旅行盒绿色色刷头通配适配ABS版',
    '旅行盒白色刷头通配适配ABS版', '旅行盒白色刷头通配适配ABS版',
    '旅行盒粉色刷头通配适配ABS版', '旅行盒粉色刷头通配适配ABS版',
    '旅行盒紫色刷头通配适配ABS版', '旅行盒紫色刷头通配适配ABS版',
    '旅行盒蓝色刷头通配适配ABS版', '旅行盒蓝色刷头通配适配ABS版',
    '旅行盒黄色刷头通配适配ABS版', '旅行盒黄色刷头通配适配ABS版',
    '旅行盒黑色刷头通配适配ABS版', '旅行盒黑色刷头通配适配ABS版',
    '电机套 （铝合金、不锈钢共用）', '电机套 （铝合金、不锈钢共用）',
    '情人节礼盒-奶茶色-底盒标签', '情人节礼盒-奶茶色-底盒标签',
    '情人节礼盒-白色-底盒标签', '情人节礼盒-白色-底盒标签',
    '情人节礼盒-粉色-底盒标签', '情人节礼盒-粉色-底盒标签',
    '情人节礼盒-紫色-底盒标签', '情人节礼盒-紫色-底盒标签',
    '情人节礼盒-绿色-底盒标签', '情人节礼盒-绿色-底盒标签',
    '情人节礼盒-蓝色-底盒标签', '情人节礼盒-蓝色-底盒标签',
    '情人节礼盒-黄色-底盒标签', '情人节礼盒-黄色-底盒标签',
    'USB-C转USB转换器', 'USB-C转USB转换器',
    '旅行盒奶茶色适配ABS版', '旅行盒奶茶色适配ABS版',
    '发热丝组件（220V', '发热丝组件（220V',
    '情人节礼盒国内底盒标签', '情人节礼盒国内底盒标签',
    '旅行盒白色适配ABS版', '旅行盒白色适配ABS版',
    '旅行盒粉色适配ABS版', '旅行盒粉色适配ABS版',
    '旅行盒紫色适配ABS版', '旅行盒紫色适配ABS版',
    '旅行盒绿色适配ABS版', '旅行盒绿色适配ABS版',
    '旅行盒蓝色适配ABS版', '旅行盒蓝色适配ABS版',
    '旅行盒黄色适配ABS版', '旅行盒黄色适配ABS版',
    '旅行盒黑色适配ABS版', '旅行盒黑色适配ABS版',
    'Pogopin转换器', 'Pogopin转换器',
    '壁挂支架ABS款', '壁挂支架ABS款',
    '电动牙刷透明护龈刷头', '电动牙刷透明护龈刷头',
    '壁挂支架金属款', '壁挂支架金属款',
    '电动牙刷旅行盒白色', '电动牙刷旅行盒白色',
    '电动牙刷适配器套装', '电动牙刷适配器套装',
    '电源线标准1.5M', '电源线标准1.5M',
    '电源线标准1.7M', '电源线标准1.7M',
    '白盒封盒贴纸（上）', '白盒封盒贴纸（上）',
    '白盒封盒贴纸（下）', '白盒封盒贴纸（下）',
    '拨动温控开关组件', '拨动温控开关组件',
    '新包胶刷头单支装', '新包胶刷头单支装',
    '铝合金 主体外壳', '铝合金 主体外壳',
    'USB-C电源', 'USB-C电源',
    '刷头套盒3支装', '刷头套盒3支装',
    '刷头套盒6支装', '刷头套盒6支装',
    '包胶刷头单支装', '包胶刷头单支装',
    '双色把手内壳上', '双色把手内壳上',
    '导风嘴220V', '导风嘴220V',
    '导风嘴带螺丝孔', '导风嘴带螺丝孔',
    '档位开关座压板', '档位开关座压板',
    '电机轴防水软胶', '电机轴防水软胶',
    '开关风速按钮', '开关风速按钮',
    '温度调节按钮', '温度调节按钮',
    '温控开关按钮', '温控开关按钮',
    '电源线连插头', '电源线连插头',
    '磁吸壁挂支架', '磁吸壁挂支架',
    '磁吸顺滑风嘴', '磁吸顺滑风嘴',
    '礼盒版手提袋', '礼盒版手提袋',
    '返工底盒标签', '返工底盒标签',
    '迷你磁吸支架', '迷你磁吸支架',
    '风速开关按钮', '风速开关按钮',
    '1500W', '1500W',
    'USB-A', 'USB-A',
    '仿绒收纳袋', '仿绒收纳袋',
    '双色内壳上', '双色内壳上',
    '双色导风嘴', '双色导风嘴',
    '导风嘴组件', '导风嘴组件',
    '开关保护盖', '开关保护盖',
    '把手内壳下', '把手内壳下',
    '收纳包外盒', '收纳包外盒',
    '数据线套装', '数据线套装',
    '旅行收纳包', '旅行收纳包',
    '标准热缩膜', '标准热缩膜',
    '温控开关板', '温控开关板',
    '独立装刷头', '独立装刷头',
    '电源线压块', '电源线压块',
    '电源线尾座', '电源线尾座',
    '羊毛毡支架', '羊毛毡支架',
    '铁片固定座', '铁片固定座',
    '后盖组件', '后盖组件',
    '壁挂支架', '壁挂支架',
    '开关滑片', '开关滑片',
    '扩散风嘴', '扩散风嘴',
    '把手外壳', '把手外壳',
    '电线尾座', '电线尾座',
    '迷你支架', '迷你支架',
    '顺滑风嘴', '顺滑风嘴',
    '风嘴铁环', '风嘴铁环',
    '风筒外壳', '风筒外壳',
    '69码', '69码',
    '内滤网', '内滤网',
    '后盖上', '后盖上',
    '外壳带', '外壳带',
    '外滤网', '外滤网',
    '收纳包', '收纳包',
    '收纳袋', '收纳袋',
    '束线带', '束线带',
    '气垫梳', '气垫梳',
    '聚风嘴', '聚风嘴',
    '后盖', '后盖',
    '外壳', '外壳',
    '底盖', '底盖',
    '铁环', '铁环'
}
 


sorted_dict = {key: part_pattern[key] for key in sorted(part_pattern.keys(), key=lambda x: x, reverse=False)}
unique_dict = dict(OrderedDict(part_pattern.items()))


pprint.pprint(sorted_dict, indent=4)
ks = []
vs = []
for k,v in part_pattern.items():
    ks.append(k)
    vs.append(v)
print('------------------------------')
ks = sorted(ks,key=len,reverse=True)
vs = sorted(ks,key=len,reverse=True)

kd = OrderedDict()
for k,v in zip(ks,vs):
    kd[k] = v

pprint.pprint(ks,indent=4)
pprint.pprint(vs,indent=4)
pprint.pprint(kd,indent=4)