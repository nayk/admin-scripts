#!/usr/bin/env python
import subprocess, MySQLdb, sys
cmd = 'sudo /etc/init.d/zabbix-agentd restart'

#cmd = 'grep ertelecomsb /etc/passwd'

# COPY FILE
#file = sys.argv[2]
#cmd = 'scp %s' % file
server_type = sys.argv[1]

connection = MySQLdb.connect(host='servers.nayk.pro', user='ertelecom', passwd='9uajkj1kL', db='ertelecom')
cursor = connection.cursor()

cursor.execute("select id, name from servers_servertype where name = '%s';"  % server_type)
server_type_id = cursor.fetchone()

cursor.execute("select fqdn from servers_summarytable where server_type_id = '%s' and puppet = 1 and city_id = 1"  % server_type_id[0])
servers = cursor.fetchall()
connection.close()

for server in servers:
    if not subprocess.call("ping -c 1 -W 1 %s" % server[0], shell=True, stdout=subprocess.PIPE):
#        retcode = subprocess.call('scp %s %s:/home/nayk/ ' % (file, server[0]), shell=True)
        retcode = subprocess.call('ssh nayk@%s " %s " ' % (server[0], cmd), shell=True)
        if retcode == 0:
            print "OK!  %s   <<< %s >>>\n" % (cmd, server[0])
        else:
            print "FAIL! %s  >>> %s <<<\n" % (cmd, server[0])

