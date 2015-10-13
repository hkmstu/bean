#!/bin/sh

IP_INFO=`curl http://members.3322.org/dyndns/getip`
python sendmail.py ${IP_INFO}
