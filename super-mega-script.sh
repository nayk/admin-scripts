#!/bin/bash
for i in 1 2; do for j in db radius; do echo "$j$i: `zabbix_get -s "$j$i".perm.ertelecom.ru -k raid.stat`";  done done

for i in `grep -R "/usr/local/scripts/zabbix/raid/raid_status.sh" ./* | grep -v .svn | cut -d ":" -f 1`; do emacs $i; done
