DB_HOST = "ec2-3-215-57-87.compute-1.amazonaws.com"
DB_NAME = "d790e22ak9nhgt"
DB_USER = "mnilykstdctavj"
DB_PASS = "42c03c362ae741444d0ce7c465c4d8bfd4c0b6e9ea071251ede2f2fdd40bbd09"

import psycopg2
from AddUsers import getnewusers
from User import *

def addStationtoDb(user,num,cur):
    cur.execute(user.addStation(num)[0],user.addStation(num)[1])


def writeusertoDb(user,cur):
    cur.execute(user.writetodb()[0],user.writetodb()[1])

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

print(cur.execute("SELECT * FROM \"User\""))


rows = cur.fetchall()
# cur.execute('''UPDATE \"User\"
# SET "name" = "Adam Tan(demo)"
# WHERE "name"="Adam Tan(Click here for demo)";''')

userlist = []

# user = User(23006,"Adam Tan (demo)","311B","PENDING","?")
# user2 = User(23007,"Micheal Lim","311B","PENDING","?")

# writeusertoDb(user,cur)
# writeusertoDb(user2,cur)

for user in rows:
    id = user[0]
    name = user[1]
    ic = user[2]
    status = user[3]
    group = user[4]
    userlist.append(User(id , name , ic , status , group))
    #print(user)


for i in getnewusers():
    writeusertoDb(i,cur)
    print("asd")

print("asdasd")
conn.commit()
cur.close()
conn.close()
print("asdasdasdasd")

