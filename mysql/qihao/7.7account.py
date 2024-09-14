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

def insert_u():
    number=input("输入账号")
    b_name=input("输入银行名称")
    address=input("请输入地址")
    bbalabce=float(input("输入账户余额"))
    maxpay=float(input("输入每月最大支出"))
    phone=input("输入手机号")
    c_number=input("输入企业账号")
    sql="insert into t_account(ac_number,bank_name,bank_address,balabce,maxMonthpay,ac_phone,regist_date,co_number) values(%s,%s,%s,%s,%s,%s,now(),%s)"
    cursor.execute(sql,(number,b_name,address,bbalabce,maxpay,phone,c_number))
    db.commit()
    rowcount=cursor.rowcount
    if rowcount>0:
        print("写入数据成功")
    else :
        print("写入数据失败")

insert_u()

# 修改数据

def update_u() :
    id=int(input("输入需要修改的id"))
    number = input("输入需要修改的账号")
    b_name = input("输入修改的银行名称")
    address = input("请输入修改的地址")
    bbalabce = float(input("输入修改账户余额"))
    maxpay = float(input("输入修改每月最大支出"))
    phone = input("输入修改手机号")
    c_number = input("输入修改的企业账号")
    sql="update t_account set ac_number=%s,bank_name=%s,bank_address=%s,balabce=%s,maxMonthpay=%s,ac_phone=%s,co_number=%s where a_id=%s"
    cursor.execute(sql,(number,b_name,address,bbalabce,maxpay,phone,c_number,id))
    db.commit()
    rowcount=cursor.rowcount
    if rowcount>0:
        print("信息修改成功")
    else :
        print("信息修改失败")

# update_u()

# 删除数据
def delete_u() :
    id=int(input("输入需要删除的id号"))
    sql="delete from t_account where a_id=%s"
    cursor.execute(sql,(id,))
    db.commit()
    rowcount=cursor.rowcount
    if rowcount>0:
        print("删除成功")
    else :
        print("删除失败")


# delete_u()
