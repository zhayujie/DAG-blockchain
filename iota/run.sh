# !/bin/bash

if [[ ! -d "iri" || ! -d "private-iota-testnet" ]]
then
    echo "Wrong path"
    exit 1
fi

cd iri/target

if [[ -d ./testdb ]]; then
    rm -rf testdb*
fi

# start iota node
nohup java -jar iri-1.5.0.jar --testnet --testnet-no-coo-validation --snapshot=Snapshot.txt -p 14700 --remote --zmq-enabled &

cd -

sleep 3

# send the first milestone by coordinator tool
java -jar private-iota-testnet/target/iota-testnet-tools-0.1-SNAPSHOT-jar-with-dependencies.jar Coordinator localhost 14700