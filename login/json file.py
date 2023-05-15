import json 
def submit():
    username=input("username?")
    password=input("password?")
    c_pass=input("c_pass?")
    
    if password!=c_pass:
        print("your password and c_pass miss match")
        return
    
    if len(password)<8:
        print("your password most be over than 8 char")
        return
    
    with open ("info.json") as f:
        dct=json.load(f)
        
    if username in dct:
        print("your username is already exist")
        return
    
    dct[username]=password
    
    with open ("info.json",'w') as f:
        json.dump(dct,f)
        
    print("submit Done!!!")
    
def login():
    global user_log
    if user_log:
        print("you are already logged in!")
    username=input("username?")
    password=input("password?")
    
    with open ("info.json") as f:
        dct=json.load(f)
        
    if username in dct and dct[username]==password:
        user_log=username
        print("wellcome to your account")
    else:
        print("wrong username and password")
        
def delete():
    global user_log
    if (user_log == False):
        print("please login first")
        return
    if (user_log=="admin"):
        print("admin account has not remmvable")
        return
    # username=input("username?")
    # password=input("password?")
    
    with open("info.json") as f:
        dct=json.load(f)
        
    question=input("are you sure? yes or no")
    if question=="yes":
        
        dct.pop(user_log)
        with open ("info.json",'w') as f:
            json.dump(dct,f)
        print("you account has been deleted")
        user_log=False
    else:
        print("canceld by user")
        
def logout():
        global user_log
        if (user_log == False):
            print("you are not logged in")
            return
        user_log=False
        print("you are loged out")
    
def users_list():
    global user_log
    if (user_log != "admin"):
        print("access denied!")
        return
    with open ("info.json") as f:
        dct=json.load(f)
    for username in dct:
        print(username)
        

user_log=False

while(True):
    plan=input("whats your plan?")
    if plan=="submit":
        submit()
    elif plan=="login":
        login()
    elif plan=="delete":
        delete()
    elif plan=="logout":
        logout()
    elif plan=="users_list":
        users_list()
    elif plan=="exit":
        break
    else:
        print("wrong input!!!!")
        