from User import *


def getnewusers():
    
    userlist = []

    for i in range(100):
        id = 20000 + i
        name = "name" + str(i)
        ic = "311G"
        status = "PENDING"
        group = "11";

        userlist.append(User(id , name , ic , status , group))
        print(id , name , ic , status , group)

    return userlist

