import pickle
import os

def createUserDict(u, p):

    f = open(r"credentials/AdminData.dat","ab")

    userDict = {}
    userDict[u] = p
    pickle.dump(userDict,f)

def checkExistingAdmin(username, password):

    userDict = {}
    userDict[username] = password

    f = open(r"credentials/AdminData.dat","rb")
    run = True
    while run:
        try:
            data = pickle.load(f)
            if userDict == data:
                return "True"

        except EOFError:
            return "False"

def checkAdminUsername(username):

    f = open(r"credentials/AdminData.dat","rb")
    run = True
    while run:
        
        try:
            data = pickle.load(f)
            for key in data.keys():
                if key == username:
                    return "True"

        except EOFError:
            return "False"
                        

def viewMessages(roomname):

    f = open(rf"chatrooms/{roomname}.txt","r")

    fetchLines = f.readlines()

    for i in fetchLines:
        print(i)

def deleteRoom(roomname):

    if os.path.isfile(rf"chatrooms/{roomname}.txt"):
        os.remove(rf"chatrooms/{roomname}.txt")
        print("Chatroom Deleted Successfully...")
    else:
        print("Room Do not Exists...")