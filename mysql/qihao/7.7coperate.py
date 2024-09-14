import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="zhanghang"
)
cursor = db.cursor()
# 写入数据
def insert_u() :
    ename = input("请输入企业名称")
    main_work=input("请输入企业主要业务")
    regist=input("请输入企业的注册地址")
    money=float(input("请输入注册金额"))
    cnumber=input("请输入企业账号")
    sql="insert into t_corporate(co_name,major_work,regist_address,regist_date,regist_money,co_number) values(%s,%s,%s,now(),%s,%s)"
    cursor.execute(sql,(ename,main_work,regist,money,cnumber))
    db.commit()
    rowcount=cursor.rowcount
    if rowcount>=0:
        print("企业信息添加成功")
    else :
        print("企业信息添加失败")

insert_u()

# 修改信息

def update_u():
    id=int(input("请输入需要修改的id"))
    ename = input("请输入修改后企业名称")
    main_work = input("请输入修改后企业主要业务")
    regist = input("请输入修改后企业的注册地址")
    money = float(input("请输入修改后注册金额"))
    cnumber = input("请输入修改后的企业账号")
    sql="update t_corporate set co_name=%s,major_work=%s,regist_address=%s,regist_money=%s,co_number=%s where co_id=%s"
    cursor.execute(sql,(ename,main_work,regist,money,cnumber,id))
    db.commit()
    rowcount=cursor.rowcount
    if rowcount>0:
        print("企业信息修改成功")
    else :
        print("企业信息修改失败")

# update_u()

# 删除数据
def delete_u():
    id=int(input("输入需要删除的id"))
    sql="delete from t_corporate where co_id=%s"
    cursor.execute(sql,(id,))
    db.commit()
    rowcount=cursor.rowcount
    if rowcount>0:
        print("企业数据删除成功")
    else :
        print("企业数据删除失败")

# delete_u()