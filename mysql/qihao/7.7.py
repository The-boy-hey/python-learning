# for i in range(10) :
#     print("齐豪")

# s=0
# for i in range(1,21) :
#     s+=i
# print(s)

# s=0
# for i in range(2,101,2) :
#     s+=i
# print(s)

# 对表格的数据进行添加 删改


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="zhanghang"
)
cursor = db.cursor()

# 增添数据
def insertt_user() :
    userid=input("输入id")
    username=input("输入名字")
    password=input("输入密码")
    age=input("输入年龄")
    gender=input("输入性别")
    userphone=input("输入手机号")
    address=input("输入地址")
    sql="insert into t_user(u_id,user_name,password,age,gender,phone,address) values (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(userid,username,password,age,gender,userphone,address))
    db.commit()
    rowcount=cursor.rowcount
    if rowcount >0 :
        print("成功")
    else:
        print("s失败")

# insertt_user()


# 修改
def updateuser() :
    userid = int(input("输入id"))
    username = input("输入修改后的名字")
    password = input("输入修改后的密码")
    age = int(input("输入修改后的年龄"))
    gender = input("输入修改后的性别")
    phone = input("输入修改i后的手机号")
    address = input("输入修改后的地址")
    sql="update t_user set user_name=%s,password=%s,age=%s,gender=%s,phone=%s,address=%s where u_id=%s"
    cursor.execute(sql,(username,password,age,gender,phone,address,userid))
    db.commit()
    rowcount=cursor.rowcount
    if rowcount>0 :
        print("修改成功")
    else :
        print("修改失败")

updateuser()

# 删除
def deleteuser():
    userid = int(input("输入id"))
    username=input("输入需要删除的名字")
    password=input("输入密码")
    sql="delete from t_user where u_id=%s and user_name=%s and password=%s"
    cursor.execute(sql,(userid,username,password))
    db.commit()
    recount=cursor.rowcount
    if recount >0 :
        print("删除成功")
    else :
        print("删除失败")


# deleteuser()




