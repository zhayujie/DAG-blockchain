# !/bin/bash

function startIota() {
    if [[ ! -d "iri" || ! -d "private-iota-testnet" ]]
    then
        echo "Wrong path"
        exit 1
    fi

    cd iri/target

    if [[ -d testnetdb ]]; then
        rm -rf testnetdb*
    fi

    # start iota node
    nohup java -jar iri-1.4.2.4.jar --testnet --testnet-no-coo-validation --snapshot=Snapshot.txt -p 14700 --remote --zmq-enabled &

    cd -

    sleep 2

    # send the first milestone by coordinator tool
    java -jar private-iota-testnet/target/iota-testnet-tools-0.1-SNAPSHOT-jar-with-dependencies.jar Coordinator localhost 14700
}

function addAllNeighbors() {
    lastIP=("56" "57" "58" "59" "60" "61" "62" "63" "66")
    i=0
    while [[ i -lt 8 ]]; do
        curl http://192.168.5."${lastIP[$i]}":14700 \
            -X POST \
            -H 'Content-Type: application/json' \
            -H 'X-IOTA-API-Version: 1' \
            -d '{"command": "addNeighbors", "uris": 
                ["udp://192.168.5.56:14600", "udp://192.168.5.57:14600", "udp://192.168.5.58:14600", 
                "udp://192.168.5.60:14600", "udp://192.168.5.61:14600", "udp://192.168.5.62:14600",
                "udp://192.168.5.63:14600", "udp://192.168.5.66:14600"]}'
        ((i++))
    done
}

function addNeighbors() {
    curl http://localhost:14700 \
        -X POST \
        -H 'Content-Type: application/json' \
        -H 'X-IOTA-API-Version: 1' \
        -d '{"command": "addNeighbors", "uris": 
            ["udp://192.168.5.56:14600", "udp://192.168.5.57:14600", "udp://192.168.5.58:14600", 
            "udp://192.168.5.60:14600", "udp://192.168.5.61:14600", "udp://192.168.5.62:14600",
            "udp://192.168.5.63:14600", "udp://192.168.5.66:14600"]}'
}

function removeSelf() {
    lastIP=("56" "57" "58" "59" "60" "61" "62" "63" "66")
    i=0
    while [[ i -lt 8 ]]; do
        NUM=${lastIP[$i]}
        curl http://192.168.5."$NUM":14700 \
            -X POST \
            -H 'Content-Type: application/json' \
            -H 'X-IOTA-API-Version: 1' \
            -d '{"command": "removeNeighbors", "uris": ["udp://http://192.168.5.'$NUM':14600"]}'
        ((i++))
    done
   
}

function killPre() {
    pid=$(ps -aux|grep 14700|grep -v "grep"|awk '{print $2}')
    if [[ $? -eq 0 ]]; then
        kill -9 $(pid)
    fi
}
#startIota
#addAllNeighbors
removeSelf
