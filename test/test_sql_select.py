from PyQt5.QtSql import QSqlDatabase, QSqlQuery
def select():
    db = QSqlDatabase.addDatabase('QSQLITE')
    # 指定SQLite数据库的文件名
    db.setDatabaseName('./db/database.db')
    if not db.open():
        print('无法建立与数据库的连接')
        return False
    query = QSqlQuery()
    query.exec('SELECT * FROM "radio"')

    j = 1

    alllist = []

    while (query.next()):  # 判断是否有下一条记录
        mylist = []
        for i in range(1,8):
            print(j,i,query.value(i))
            if query.value(i) != '':
                mylist.append(query.value(i))

        j += 1
        alllist.append(mylist)

    print(alllist)
    print(alllist[1][0])
    db.close()
    return True

select()