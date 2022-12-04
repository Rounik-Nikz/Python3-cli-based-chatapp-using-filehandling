from console import *
import os
import admin
import user
import time
import help


"""
=================================
MAIN ADMIN LOGIN PASSWORD = 123
=================================

"""

while True:
    print("============================================")
    print("         PYTHON CLI BASED CHATAPP           ")
    print("============================================")

    chooseFeature = input("1] Admin Login 2] Send Message 3] Help 4] Exit: ")
    processing(2)

    if chooseFeature == "1":

        print("Welcome to Admin Login")

        mainPassword = input("Enter Password to Proceed: ")
        clear()
        
        if mainPassword == "123":
            processing(1)
            print("Password Verified...")
            time.sleep(1)
            clear()

            chooseAdminType = input("1] Register New Admin 2] Login Existing Admin: ")
            processing(1)

            if chooseAdminType == "1":
                print("WELCOME TO ADMIN REGISTRATION PAGE")

                username = input("Enter New Username: ")
                checkUsername = admin.checkAdminUsername(username)
                
                if checkUsername == "False":
                    password = input("Enter New password: ")
                    processing(1)
                    print("New admin created successfully...")
                    admin.createUserDict(username,password)
                    time.sleep(1)

                    clear()
                    print("Please Login with the username and password")
                    loginUsername = input("Enter Username: ")
                    loginPassword = input("Enter Password: ")

                    check = admin.checkExistingAdmin(loginUsername, loginPassword)

                    if check == "True":
                        processing(1)
                        print("Logged in Successfull...")
                        time.sleep(2)
                        clear()

                        command = input("1] View Messages 2] Delete Chatrooms: ")

                        if command == "1":
                            processing(1)

                            availableChatRoom = chatrooms()
                            print("============================================")
                            print("             AVAILABLE CHATROOMS            ")
                            for i in availableChatRoom:
                                print(i.rstrip(".txt"))
                            print("============================================")

                            chatroomName = input("Enter the name of the chatroom: ")
                            try:
                                processing(2)
                                print("============================================")
                                admin.viewMessages(chatroomName)
                                print("============================================")

                                afterView()

                            except FileNotFoundError:
                                processing(2)
                                print("Room Do not Exists")
                                time.sleep(2)
                                clear()

                        elif command == "2":
                            processing(1)

                            availableChatRoom = chatrooms()
                            print("============================================")
                            print("             AVAILABLE CHATROOMS            ")
                            for i in availableChatRoom:
                                print(i.rstrip(".txt"))
                            print("============================================")

                            chatroomName = input("Enter the name of the chatroom: ")
                            processing(2)
                            admin.deleteRoom(chatroomName)
                            time.sleep(2)
                            clear()

                        else:
                            processing(1)
                            print("Enter Options Properly...")
                            time.sleep(2)
                            clear()

                    elif check == "False":
                        processing(1)
                        print("Incorrect Username/Password")
                        time.sleep(2)
                        clear()
                
                elif checkUsername == "True":
                    processing(1)
                    print("Admin Already Exists...")
                    time.sleep(2)
                    clear()


            elif chooseAdminType == "2":

                print("WELCOME TO ADMIN LOGIN PAGE")
                username = input("Admin Username: ")
                password = input("Admin Password: ")
              
                check = admin.checkExistingAdmin(username, password)
                if check == "True":
                    processing(1)
                    print("Logged in Successful")
                    time.sleep(2)
                    clear()
                    command = input("1] View Messages 2] Delete Chatrooms: ")


                    if command == "1":
                        processing(1)

                        availableChatRoom = chatrooms()
                        print("============================================")
                        print("             AVAILABLE CHATROOMS            ")
                        for i in availableChatRoom:
                            print(i.rstrip(".txt"))
                        print("============================================")

                        chatroomName = input("Enter the name of the chatroom: ")

                        processing(2)
                        print("============================================")
                        admin.viewMessages(chatroomName)
                        print("============================================")
                        afterView()

                    elif command == "2":
                        processing(1)

                        availableChatRoom = chatrooms()
                        print("============================================")
                        print("             AVAILABLE CHATROOMS            ")
                        for i in availableChatRoom:
                            print(i.rstrip(".txt"))
                        print("============================================")
                        
                        chatroomName = input("Enter the name of the chatroom: ")
                        processing(2)
                        admin.deleteRoom(chatroomName)
                        time.sleep(2)
                        clear()

                    else:
                        processing(1)
                        print("Select options properly...")
                        time.sleep(2)
                        clear()

                elif check == "False":
                    processing(1)
                    print("Incorrect Username/Password")
                    time.sleep(2)
                    clear()
                
            else:
                print("Select options properly...")
                time.sleep(2)
                clear()

        else:
            processing(1)
            print("Please Enter Proper Password...")
            time.sleep(2)
            clear()

    elif chooseFeature == "2": 
        
        chooseRoom = input("1]New Chatroom 2]Exisiting Chatroom: ")
        processing(1)
            
        if chooseRoom == "1": 

            try:
                send = True
                availableChatRoom = chatrooms()
                print("============================================")
                print("             AVAILABLE CHATROOMS            ")
                for i in availableChatRoom:
                    print(i.rstrip(".txt"))
                print("============================================")                
                roomname = input("Enter a new room name: ")
                processing(1)


                if os.path.exists(rf"chatrooms/{roomname}.txt") == True:
                    print("Room Already Exists")
                    time.sleep(2)
                    clear()

                else:
                    userNo = int(input("Enter the number of user: "))
                    processing(2)
                    users = user.userName(userNo)
                    processing(1)

                    print("==================================================")
                    print("INSTRUCTIONS: PRESS CTRL+C TO STOP SENDING MESSAGE")
                    print("==================================================")
                    time.sleep(2)

                    while send:
                        user.sendMessage(users, roomname)

            except KeyboardInterrupt:
                send=False
                processing(1)

            except ValueError:
                processing(1)
                print("Erorr!! Only numeric inputs are allowed...")
                send = False
                time.sleep(2)
                clear()

        elif chooseRoom == "2": 

            try:
                send = True

                availableChatRoom = chatrooms()
                print("============================================")
                print("             AVAILABLE CHATROOMS            ")
                for i in availableChatRoom:
                    print(i.rstrip(".txt"))
                print("============================================")     

                roomname = input("Enter the room name: ")
                processing(1)
  
                if os.path.exists(rf"chatrooms/{roomname}.txt") == False:
                    print("Room Do Not Exists")
                    time.sleep(2)
                    clear()

                else:
                    userNo = int(input("Enter the number of user: "))
                    processing(2)  
                    users = user.userName(userNo)
                    processing(1)

                    print("==================================================")
                    print("INSTRUCTIONS: PRESS CTRL+C TO STOP SENDING MESSAGE")
                    print("==================================================")
                    time.sleep(2)

                    user.existingMessageViewer(roomname)


                    while send:
                        user.sendMessage(users, roomname)

            except KeyboardInterrupt:
                send = False
                processing(1)

            except ValueError:
                processing(2)
                print("Erorr!! Only numeric inputs are allowed...")
                send = False
                time.sleep(2)
                clear()

        else: 
            processing(1)
            print("Select options properly...")
            time.sleep(2)
            clear()

    elif chooseFeature == "3":
    
        processing(1)
        print("==================================================")
        print("   INSTRUCTIONS: PRESS CTRL+C TO EXIT HELP PANEL  ")
        print("             WELCOME TO HELP PAGE                 ")
        print("==================================================")
        time.sleep(2)        
        try:
            help.helpMe()
            time.sleep(100)
            processing(1)
            print("Help feature expired... Select the help command again.")
            time.sleep(2)
            clear()
            
        except KeyboardInterrupt:
            processing(2)
            clear()
        

    elif chooseFeature == "4":
        processing(2)
        print("Exiting the app...")
        time.sleep(2)
        clear()
        break

    else:
        processing(2)
        print("Enter Proper Options...")
        time.sleep(2)
        clear()