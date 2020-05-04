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

    while (query.next()):  # 判断是否有下一条记录
        print(query.value(1))

    db.close()
    return True

select()