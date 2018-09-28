# getBalance
curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{
    "command": "getBalances", 
    "addresses": ["FCFOXYDMOCKOQDP9XHMAXWJIXNHOZNZDBUBTVMY9ZGQZTQLNRQ9TLRZGLDMGDEIOGEOHULWMGWRMQSGXX"], 
    "threshold": 100
}'

# getTips: tips（未确认交易）
curl http://localhost:14700\
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "getTips"}'

# findTx
curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "findTransactions", "addresses": ["RUVLPUG9GHCAZEOBOLLHEQPLYQMTZJNGPHGQMZPXERMMXATBPEAH9CLQ9BNJVJHFNNEPFRSZ9FREMWOBD"]}'

# getTransactionsToApprove
curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "getTransactionsToApprove", "depth": 3}'

# addNeighbors
curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "addNeighbors", "uris": ["udp://192.168.5.56:14600"]}'

# getNeighbors
curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "getNeighbors"}'

# removeNeighbors
curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "removeNeighbors", "uris": ["udp://192.168.5.58:14600"]}'

# addAllNeighbors
curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "addNeighbors", 
    "uris": ["udp://192.168.5.56:14600", "udp://192.168.5.57:14600", "udp://192.168.5.58:14600",
             "udp://192.168.5.60:14600", "udp://192.168.5.61:14600", "udp://192.168.5.62:14600",
             "udp://192.168.5.63:14600"]}'

# getNodeInfo
curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "getNodeInfo"}'