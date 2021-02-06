"""
TIRTH HOMEWORK

1) user login application:
-get username and values from the user
-check the values in an if statement and tell the user if they were succesful

"""
import time

user = {"id": "asdasd", "pass": "asdasdasd"} # prototype of a dictionary
user_validated = False

retry_cnt = 0

while user_validated == False:
    print("please enter your credentials:\n")

    user.update({"id": input("id: ")})
    user.update({"pass": input("password ")})
    
    if user.get("id") == "lucas" and user.get("pass") == "gotico13":
        print("all good.")
        user_validated = True
    else: 
        print("incorrect username or password. %d trys left" %(3-retry_cnt))
        retry_cnt += 1
        if retry_cnt == 4:
            print("max retry exceed. you can re-try in 1 minutes")
            penalty_time = 60
            while penalty_time != 0:
                print("%d seconds left.." %(penalty_time)) #this of course can be omitted
                time.sleep(1)
                penalty_time-=1
            
