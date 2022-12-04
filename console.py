import os
import time

def clear():
    return os.system('cls')

def processing(t):
    clear()
    print("Proccesing...")
    time.sleep(t)
    clear()

def afterView():
    print("Hit [enter] once you have done viewing the messages")
    input()
    processing(2)

def chatrooms():
    dir_list = os.listdir(r"chatrooms")
    return dir_list