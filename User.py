

class User:
    def __init__(self , id , name , ic , status , group , stationlist = [False,False,False,False]):
        self.id = id
        self.name = name
        self.ic = ic
        self.status = status
        self.group = group
        self.stationlist = stationlist

    def writetodb(self):
        return ("INSERT INTO \"User\"\nVALUES(%s,%s,%s,%s,%s);",(self.id, self.name, self.ic, self.status, self.group))


    def getstations(self):
        return self.stationlist

    def addStation(self,num):
        self.stationlist[num-1] = True
        return("INSERT INTO \"StationRecord\"\nVALUES(%s,%s,%s,%s,%s)",(self.id,"2038-01-19 03:14:07",self.id,"04141b26-f4e7-409a-b4fa-9ca22284b025",num))





