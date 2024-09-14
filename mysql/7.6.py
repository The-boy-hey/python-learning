import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="zhanghang"
)

cursor = db.cursor()
def login ():
    usename=input("输入用户名")
    usepassword=input("输入密码")
    # sql="select u_id,user_name,password,age,gender,phone,address from t_user where user_name=%s and password=%s"
    sql="select u_id,user_name from t_user where user_name=%s and password=%s"
    cursor.execute(sql,(usename,usepassword))
    result = cursor.fetchall()
    print(result)
    n=len(result)
    if n>0 :
        print("成功")
    else :
        print("用户名或者密码错误，重新输入")

# login()