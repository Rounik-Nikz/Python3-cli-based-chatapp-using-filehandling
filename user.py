def userName(n):

    users = []

    for i in range(n):
        name = input(f"Enter the user {i+1} name: ")
        users.append(name)
        print(" ")

    return users


def existingMessageViewer(roomname):
    f = open(rf"chatrooms/{roomname}.txt","r")

    fetchLines = f.readlines()
    for i in fetchLines:
        print(i)
    f.close()


def sendMessage(n,roomname):

    f = open(rf"chatrooms/{roomname}.txt", "a")

    for i in n:
        message = input(f"{i}: ")
        print(" ")
        f.write(f"{i} : {message}\n")
    
    f.close()