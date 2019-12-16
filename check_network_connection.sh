#!/bin/sh

echo $0, $1

dueTime=$1

server="210.220.163.82" ## SK
valid=1

while ((${valid}==1));
do
    ping -c 1 | awk '{result=$2} END {print result}'
    if [ $result=="timeout" ];
    then
        echo "$server ..... 네트워크 연결에 문제가 있습니다."
        python ~/workspace/GW_Study/Connecting_network.py
    else
        echo "$server ..... 네트워크 연결이 정상입니다."
    fi

    local_currentTime=$(date +%H:%M)
    _dueTime=${dueTime:0:2}
    _currentTime=$(date +%H)

    if (($_dueTime == $_currentTime));then
        echo "지정된 시간 ${dueTime} 이 지났습니다. 프로그램을 종료합니다."
        valid=0
        sleep 3;
    else
        echo "현재 시각은 ${local_currentTime} 입니다."
        sleep 120;
    fi
done

## https://m.blog.naver.com/PostView.nhn?blogId=nkyle9361&logNo=110128237777&proxyReferer=https%3A%2F%2Fwww.google.com%2F