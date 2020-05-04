from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    # 指定SQLite数据库的文件名
    db.setDatabaseName('./db/database.db')
    if not db.open():
        print('无法建立与数据库的连接')
        return False
    query = QSqlQuery()
    query.exec("create table radio(Id int primary key,RadioName char(10) NOT NULL,First char(10) NOT NULL,Second char(10),\
    Third char(10),Fourth char(10),Fifth char(10),Sixth char(10))")
    query.exec('insert into radio values(1,"抑郁与否","是","否",Null,Null,Null,Null)')
    query.exec('insert into radio values(2,"快乐与否","是","否",Null,Null,Null,Null)')
    db.close()
    return True


if __name__ == '__main__':
    createDB()
