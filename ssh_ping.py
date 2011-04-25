#!/usr/bin/env python
import subprocess, MySQLdb, sys
connection = MySQLdb.connect(host='109.195.48.202', user='django', passwd='Django!', db='test_flowdb')
cursor = connection.cursor()
cursor.execute("select name, status from stata_city where status='1'")
citys = cursor.fetchall()
connection.close()

for city in citys:
    source = city[0]
    for city in citys:
        dest = city[0]
        start_ping = subprocess.Popen('ssh %s ping -c 1 -W 1 %s' % (source, dest), shell=True, stdout=subprocess.PIPE).stdout.readlines()
        try:
            ping = start_ping[1].split()[-2].split('=')[1]
        except IndexError:
            ping = 100
        if float(ping) < 500.0:
            print "%s -> %s: %s" % (source, dest, ping)
#                try:
#                    
#                    value = ping.split('=')[1]
#                    break
#                except IndexError:
#                    print "Oops!  That was no valid number.  Try again..."
#                    

