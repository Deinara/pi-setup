#!/usr/bin/python
import os
import sys
import termios
import json
TERMIOS = termios

#check for root
if os.geteuid() != 0:
   exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'.")

#define character get for the menu
def getkey():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
                c = os.read(fd, 1)
        finally:
                termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c

#get menu items
menuarray=[]
with open('setup_config.json') as data_file:
    data = json.load(data_file)
for dataentry in data["actions"]:
   print dataentry
   menuarray.append(dataentry)

#get longest menu name
maxlength=0
for name in menuarray:
    length=len(name[0])
    if maxlength<length:
        maxlength=length

#Display menu
while True:
   i=1
   menunumoptions=[]
   os.system('clear')
   print " "
   print "*****************************************************"
   print "**       Please select which scripts to run        **"
   print "*****************************************************"
   print " "
   for selectitem in menuarray:
       if selectitem[2]=='ON':
         selectedicon='X'
       else:
         selectedicon=' '
       print "[" + selectedicon + "] " + str(i) + ": " + selectitem[0].ljust(maxlength) + "  " + selectitem[1]
       menunumoptions.append(i)
       i=i+1
   print " "
   print "(de)select by entering option number, enter to accept and q to quit"
   print " "

   c = getkey()
   if c == '\n':     ## break on a Return/Enter keypress
      break
   if c == 'q':     ## quit when q is pressed
      quit()
   c=int(c)
   if c in menunumoptions: #switch on or OFF
      if menuarray[c-1][2]=='OFF':
          menuarray[c-1][2]='ON'
      else:
         menuarray[c-1][2]='OFF'

#run the commands
os.system('clear')
print 'Starting...'
for selectitem in menuarray:
    if selectitem[2]=='ON':
        print ""
        print "Executing " + selectitem[0]
        for command in selectitem[3]:
           os.system(command)
