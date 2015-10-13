#!/bin/sh

./mjpg_streamer -i "./input_uvc.so -d /dev/video0" -o "./output_http.so -w ./www" >./log/mjpg_`date +%Y%m%d_%H%M%S`.log 2>&1
