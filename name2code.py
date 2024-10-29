import pandas as pd
import re
from tqdm import tqdm
tqdm.pandas(desc='FUCKING PROCESSING.......')
path = r'持续更新聚水潭匹配表\returns.xlsx'
outpath = 'out.xlsx'

# 载入信息所在单元格并根据商品名称去重
def extract_info(path):
    df = pd.read_excel(path,sheet_name='退换货')
    df = df[['线上单号','商品编码','商品名称']]    
    df = df.drop_duplicates(subset=['商品名称'])
    # df.to_excel(outpath,index=False)     
    return df   

model_pattern = {'HD30MINIlite': 'HD30 MINIlite',
 'LFHDMINIlite': 'LFHD MINIlite',
 '徕芬新一代高速家用吹风机': 'LF03',
 'LFHDSE-Lite': 'LFHD SE-Lite',
 'LF03&LF03SE': 'LF03&LF03SE',
 'HD31MINI': 'HD31 MINI',
 'LFHDMINI': 'LFHD MINI',
 'MINIlite': 'MINI Lite',
 'MiniLite': 'MINI Lite',
 'LF04MINI': 'LF04MINI',
 'MINILITE': 'MINILITE',
 'LFHDSE2': 'LFHD SE 2',
 '收纳包':'收纳包',
 '洁丽雅毛巾': '洁丽雅毛巾w0191',
 '迷你磁吸支架':'迷你磁吸支架',
 '顺丰文件袋': '顺丰文件袋',
 '静水干发帽': '洁玉静水干发帽DST2-013',
 '迷你支架': '迷你支架',
 '电动牙刷': 'T91',
 '圣菲特干发帽': '圣菲特干发帽',
 'LF03SE': 'LF03 SE',
 'LF03-SE':'LF03-SE',
 '维修-电吹风': 'LF02',
 'LF03': 'LF03',
 'LF02': 'LF02',
 'SE': 'LF03 SE',
 'se': 'LF03 SE',
 '支架': '支架'}

type_pattern = dict(sorted(model_pattern.items(), key=lambda item: len(item[0]), reverse=True),)
part_pattern = {'USB-C转USB转换器': 'USB-C转USB转换器',
 'Pogopin转换器': 'USB-C转磁吸Pogopin转换器',
 '刷头套盒3支装': '刷头套盒3支装',
 '刷头套盒6支装': '刷头套盒6支装',
 'USB-C电源': 'USB-C电源适配器',
 '(ABS款)': '壁挂支架(ABS款)',
 '磁吸壁挂支架': '磁吸壁挂支架',
 '(金属款)': '壁挂支架(金属款)',
 '旅行收纳包': '旅行收纳包',
 '独立装刷头': '独立装刷头',
 'USB-A': 'USB-A转TYPE-C转换器',
 '壁挂支架': '壁挂支架',
 '包胶刷头': '包胶刷头单支装',
 '不锈钢': '不锈钢',
 '铝合金': '铝合金',
 '旅行盒': '旅行盒',
 '聚风嘴': '聚风嘴',
 '气垫梳': '气垫梳',
 '塑胶': 'ABS'}

part_pattern = dict(sorted(part_pattern.items(), key=lambda item: len(item[0]), reverse=True),)

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

# 匹配颜色函数
def match_color(row):
    for key, value in tqdm(color_pattern.items(), desc='FUCKING PROCESSING.......'):
        if re.search(re.escape(key), row['商品名称']):
            return value
    return ''

# 匹配版本函数
def match_type(row):
    if re.search(re.escape('礼盒'), row['商品名称']):
        return '礼盒版'
    return '普通版'

# 匹配主型号函数
def match_and_label(row):
    for key, value in tqdm(type_pattern.items(), desc = 'FUCKING PROCESSING.......'):
        # 使用正则表达式确保精确匹配
        if re.search(re.escape(key) , row['商品名称']):
            return value  # 找到第一个匹配，立即返回
    return ''  # 如果没有匹配，返回无匹配

#匹配具体型号函数
def match2time(row):
    for key, value in tqdm(part_pattern.items(), desc = 'FUCKING PROCESSING.......'):
        # 重复了的不在匹配
        if value in row['型号']:
            return row['型号']  # 不进行匹配
        # 使用正则表达式确保精确匹配
        else:
            if re.search(key, row['商品名称']):
                return row['型号'] + ' ' + value  # 找到第一个匹配，立即返回
    return row['型号']  # 如果没有匹配，返回无匹配

# 合并名称函数
def makename(row):
    return row['型号'] + row['颜色'] + '-' + row['版本']
  

#提取型号
def get_model(df):
    # df = pd.read_excel('out.xlsx')
    df['商品名称'] = df['商品名称'].str.replace(" ", '')
    df['商品名称'] = df['商品名称'].str.replace("国内", '')
    df['商品名称'] = df['商品名称'].str.replace("1.5M", '')
    df['商品名称'] = df['商品名称'].str.replace("1.7M", '')
    df.insert(3,'型号','')
    df['型号'] = df.progress_apply(match_and_label, axis=1)
    df['型号'] = df.progress_apply(match2time, axis=1)
    # df.to_excel('mid.xlsx',index=False) 
    return df

#获取颜色
def get_color(df):
    # df = pd.read_excel('out.xlsx')
    df.insert(4,'颜色','')
    df['商品名称'] = df['商品名称'].str.replace(" ", '')
    df['颜色'] = df.progress_apply(match_color, axis=1) 
    # df.to_excel('mid.xlsx',index=False) 
    return df

#判断是礼盒还是普通 
def get_type(df):
    # df = pd.read_excel('out.xlsx')
    df.insert(5,'版本','')
    df['版本'] = df.progress_apply(match_type, axis=1 )
    # df.to_excel('mid.xlsx',index=False)
    return df

def concat_name(df):
    df = df.fillna('')
    df['型号'] = df['型号'].astype(str)
    df ['颜色'] = df['颜色'].astype(str)
    df['版本'] = df['版本'].astype(str)
    df.insert(6,'组合名称','')
    df['组合名称'] = df.progress_apply(makename,axis=1)
    return df


def main():
    df = extract_info(path)
    df = get_model(df)
    df = get_color(df)
    df = get_type(df)
    df = concat_name(df)
    with pd.ExcelWriter(outpath) as writer:
        df.to_excel(writer,index=False)
    tqdm.pandas(desc=None)
    print('!ddoonnee!')

main() 



    