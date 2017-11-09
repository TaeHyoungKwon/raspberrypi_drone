@echo off
cd \gstreamer\1.0\x86_64\bin

gst-launch-1.0 -v tcpclientsrc host=192.168.200.144 port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false
