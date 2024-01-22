#!/bin/bash
# starter.sh

ngrok tcp --region ap 25565 &
ngrok tcp --region us 25565 &
ngrok tcp --region au 25565 &
ngrok tcp --region eu 25565 &
ngrok tcp --region in 25565 