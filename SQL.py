
import Union
import Bool
import Time


def sql_inject(Url):
    Union.log('欢迎使用SQL注入工具......')

    Union.log('1--Union ; 2--Boolean ; 3--Sleep')
    choose = int(input("选择注入类型："))

    if choose == 1:
        Union.Union_inject(Url)
    elif choose == 2:
        Bool.Bool_inject(Url)
    elif choose == 3:
        Time.Sleep_inject(Url)


if __name__ == '__main__':
    url = input("……请输入目标url：")              # http://47.92.152.17:12345/Less-2/
    sql_inject(url)
