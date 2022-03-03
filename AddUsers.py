from User import *

import csv




def getnewusers():
    
    userlist = []
    with open("TPT2_NR.csv","r") as file:
        reader = csv.reader(file)
        i = 10000
        for row in reader:
            i = i+1
            id = i
            name = row[1]
            ic = row[0]
            status = "PENDING"
            group = ""

            print(id,name,ic,status,group)
            userlist.append(User(id,name,ic,status,group))

    print(userlist)



    return userlist

getnewusers()
