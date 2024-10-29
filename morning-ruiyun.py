import pandas as pd

outpath = 'output\输出.xlsx'
path = '瑞云寄修积压_20241029.xlsx'
def main():
    df = pd.read_excel(path)
    # df['发货状态'].fillna(0,inplace=True)
    df = df.query(" 处理状态 != '已取消'")
    df = df.query(" 发货状态 != '全部发货'")
    df = df.query("发货状态 != '部分发货'")
    df = df.query(" 申请类别 == '寄修/返修'")
    df = df.query(" 产品型号 == '产成品-吹风机' or 产品型号 == '产成品-电动牙刷'")
    with pd.ExcelWriter(outpath) as writer:
        df.to_excel(writer, index=False)
    print('Done!')
main()