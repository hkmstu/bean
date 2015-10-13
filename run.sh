#1. init mjpeg server.
cd mjpg-streamer
sh start.sh &

#2. init motors and servos. 
cd -
cd motion-part
sudo python socket_server.py &
