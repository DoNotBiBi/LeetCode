import pymysql


# 错误处理
# Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
# Error	警告以外所有其他错误类。必须是 StandardError 的子类。
# InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
# DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
# DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
# OperationalError	指非用户控制的，而是操作数据库时发生的错误。
#                   例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
# IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
# InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
# ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
# NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，
#                   然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。
def db_Test():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "newlife1994", "test")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "select * from stu_info"
    # 使用 execute()  方法执行 SQL 查询
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print("id={0},name={1},row={2}".format(row[0], row[1], row[2]))
    except:
        print("Error: unable to fetch data")

    # 增删改 属于操作
    # 事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
    # try:
    #     # 执行sql语句
    #     cursor.execute(sql)   # sql为增删改语句
    #     # 执行sql语句
    #     db.commit()
    # except:
    #     # 发生错误时回滚
    #     db.rollback()
    # 关闭数据库连接
    db.close()
