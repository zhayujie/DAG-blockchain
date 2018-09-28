curl http://localhost:14700 \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'X-IOTA-API-Version: 1' \
  -d '{"command": "addNeighbors", 
    "uris": ["udp://192.168.5.56:14600", "udp://192.168.5.57:14600", "udp://192.168.5.58:14600",
             "udp://192.168.5.60:14600", "udp://192.168.5.61:14600", "udp://192.168.5.62:14600",
             "udp://192.168.5.63:14600"]}'
