# -*- coding: utf-8 -*-

import iota
from pprint import pprint
from iota.crypto.addresses import AddressGenerator

# transfer between trytes and trits
def trytes_encode():
    trytes_bytes = 'YZJEATEQ9JKLZ'
    trytes = iota.TryteString(trytes_bytes)
    pprint(trytes)
    trits = trytes.as_trits()
    print(trits)

# getNodeInfo
def get_node_info():
    node_url = 'http://localhost:14700'
    api = iota.Iota(node_url)
    res = api.get_node_info()
    print(res)

# query the tx details in bundle 
def get_bundles():
    api = iota.Iota("http://localhost:14700") 
    pb = api.get_bundles('RGREW9FJKCFZQUYAGJXGYMKJAPSHQ9OAEEHCCINOVKKMSUDINSBGQTU9TRC9JB9UTXQTPZBQTMPGA9999')
    txs = vars(pb['bundles'][0])['transactions']
    for tx in txs:
        pprint(vars(tx))

def get_tips():
    api = iota.Iota("http://localhost:14700") 
    tips = api.get_transactions_to_approve(depth=15)
    return tips

def generate_address(num):
    seed = b"N9MOJKSFIHTPRIBYDIWEHLRNBLNFSLWPVNYTEGBIRAOZRJSIBXDNCDBVPSEJRFVRSMISGQMSLAGZEVQTR"
    generator = AddressGenerator(seed=seed, security_level=2)
    results = generator.get_addresses(0, num+2)
    with open('./Snapshot.txt', 'w') as fs:
        for i in range(0, num+1):
            fs.write(str(results[i]) + ';' + '1000000000\n')
        fs.write(str(results[num+1]) +';' + str(2779530283277761-1000000000*(num+1)))


if __name__ == '__main__':
    generate_address(100)