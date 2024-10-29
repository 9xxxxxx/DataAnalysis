import re
import pandas as pd
from tqdm import  tqdm

tqdm.pandas(desc='FUck Progressing')

paths = [r'丸辣/水8.1-9.25.xlsx', r'丸辣/水9.26-10.10.xlsx', r'丸辣/水10.11-10.22.xlsx']
outpaths =[r'丸辣/op/output8.1-9.25.xlsx', r'丸辣/op/output9.26-10.10.xlsx', r'丸辣/op/output10.11-10.22.xlsx']
match_pattern = {
    '电吹风':'吹风机',
    '电动牙刷':'电动牙刷',
    '吹风机':'吹风机',
    '塑胶':'电动牙刷',
    '不锈钢':'电动牙刷',
    '铝合金':'电动牙刷',
    'LF04MINI':'吹风机',
    'LF03闪银':'吹风机',
    'LF03简白':'吹风机',
    'LF03白金':'吹风机',
    'LF03镜黑':'吹风机',
    'LF03樱粉':'吹风机',
    'LF02-极光蓝':'吹风机',
    'LF03中国红':'吹风机',
    'LF03蓝金':'吹风机',
    'LF03绿野':'吹风机',
    'LF03青柚':'吹风机',
    'LF03-七夕':'吹风机'
}
name = '分类'
def match_and_label(row):
    for key, value in tqdm(match_pattern.items(), desc = 'Processing'):
        # 使用正则表达式确保精确匹配
        if re.search(re.escape(key) , row[name]):
            return value  # 找到第一个匹配，立即返回
    return ''  # 如果没有匹配，返回无匹配、

def get_type(path,outpath):
    df = pd.read_excel(path)
    df = df.astype('str')
    df[name] = df[name].str.replace(' ','')
    # df.insert(10,'品类','')
    df['品类'] = df.progress_apply(match_and_label, axis=1)
    df.to_excel(outpath,index=False)
    print('Done!---------------------------!!')


for i,o in zip(paths, outpaths):
    get_type(i,o)
