import winreg as reg
import os
import sys
import ctypes as cx
import psutil as util_ps
import time
def Main():
    username = input("Write You're Username For Cracking Remotr: ")
    auth = input("Write You're Email: ")
    hkey_currentuser = reg.HKEY_CURRENT_USER
    hkey_localmachine = reg.HKEY_LOCAL_MACHINE
    reg.CreateKey(hkey_currentuser, 'SOFTWARE\\Remotr')
    remotr_curuser = reg.OpenKey(hkey_currentuser, 'SOFTWARE\\Remotr', 0, reg.KEY_ALL_ACCESS + reg.KEY_WOW64_64KEY)
    remotr_x64 = reg.OpenKey(hkey_localmachine, 'SOFTWARE\\WOW6432Node\\Remotr', 0, reg.KEY_ALL_ACCESS + reg.KEY_WOW64_64KEY)
    reg.SetValueEx(remotr_curuser, "CurrentAccount", 0, reg.REG_SZ, username)
    reg.SetValueEx(remotr_curuser, "Auth", 0, reg.REG_SZ, auth)
    reg.SetValueEx(remotr_x64, "CurrentAccount", 0, reg.REG_SZ, username)
    reg.SetValueEx(remotr_x64, "Auth", 0, reg.REG_SZ, auth)
    for proc in util_ps.process_iter():
        if(proc == "RemotrService.exe"):
            proc.kill()
            print("Successfully Terminated!!!")
            time.sleep(20)
            os._exit(300)
        else:
            print("This Process is Already Terminated!!!")
            time.sleep(10)
            os._exit(443)
    os._exit(300)
            

if __name__ == "__main__":
    Main()