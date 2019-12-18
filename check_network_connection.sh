#!/bin/sh

echo "프로그램이 종료되는 시간이 $1 으로 지정되었습니다."

dueTime=$1
server="google.com"
valid=1
route_connect

# Airport command is private so make instance airport command using function.
function airport(){
    AIRPORT_PATH="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport "
    AIRPORT_COMMAND=${AIRPORT_PATH}${1}
    ${AIRPORT_COMMAND}
}

# Check mac's WIFI Router on/off and wifi router connection.
function do_wifi(){
    status=$(ifconfig en5 | grep status | awk '{print $2}')
    echo "현재 기기의 WIFI 상태는 ${status}입니다."

    if [ "${status}" != "active" ];
    then
        echo "기기의 WIFI가 꺼져 있습니다."
        echo "기기의 무선 네트워크 랜 카드를 작동합니다."
        sudo -p " " ifconfig en5 up

        airport -s | awk '{print $1}' | grep "T Free WiFi Zone"

        if [ $? == 0 ];
        then
            echo "주변에서 T Free WiFi Zone을 검색하였습니다."
            echo "해당 WIFI에 연결합니다....."
            networksetup -setairportnetwork en5 "T Free WiFi Zone"

            route_connect=$(airport -I | grep state | awk '{print $2}')
            SSID=$(airport -I | grep SSID | awk '{print $2}')

            if [ "${route_connect}" == "running" ];
            then
                echo "${SSID} 에 연결되었습니다."
            else
                echo "WIFI 라우터 연결에 실패하였습니다."
            fi
        else
            echo "등록된 WIFI가 없습니다."
        fi
    else
        echo "기기의 WIFI가 켜져 있습니다."
        route_connect=$(airport -I | grep state | awk '{print $2}')
    fi
}

# main flow
# first check route connect of mac. if failed, connect to wifi route until connected.
# then do ping test to google.com
# if failed, try to connect to wifi, until connected.
# while-loop is infinite loop, it makes wifi connection until dueTime.
# => # First check your Mac's path connection. If it fails, connect to the wifi path until you are connected.
# Ping test on google.com
# If it fails, try to connect to wifi until you are connected.
# while-loop is an infinite loop, so create a wifi connection until dueTime
while ((${valid}==1));
do  
    until [ "${route_connect}" == "running" ];
    do
        do_wifi
    done

    echo "................... PING TEST를 진행합니다."
    echo "................... 구글(https://www.google.com/)에 요청을 보내 연결을 확인합니다."
    ping -c 3 -W 1 ${server}
    result=$?
    echo "................... 결과는 ${result} 입니다."

    if [ "${result}" == 0 ];
    then
        echo "${server} ........ 네트워크 연결이 정상입니다."
    else
        until [ "${result}" == 0 ];
        do
            echo "${server} ........ 네트워크 연결에 문제가 있습니다."
            python ~/workspace/GW_Study/Connecting_network.py
            ping -c 3 -W 1 ${server}
            result=$?
        done
        echo "${server} ........ 네트워크에 연결되었습니다."
    fi

    local_currentTime=$(date +%H:%M)
    _dueTime=${dueTime:0:2}

    if [ ${_dueTime} == ${local_currentTime:0:2} ];
    then
        echo ">> 지정된 시간 ${dueTime} 이 지났습니다. 프로그램을 종료합니다."
        valid=0
        sleep 3;
    else
        echo ">> 현재 시각은 ${local_currentTime} 입니다."
        sleep 600;
    fi
done

## https://m.blog.naver.com/PostView.nhn?blogId=nkyle9361&logNo=110128237777&proxyReferer=https%3A%2F%2Fwww.google.com%2F