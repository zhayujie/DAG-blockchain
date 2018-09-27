# -*- coding: utf-8 -*-

import tx
import time
from iota.crypto.addresses import AddressGenerator
from pprint import pprint

def generate_address():
    seed = b"N9MOJKSFIHTPRIBYDIWEHLRNBLNFSLWPVNYTEGBIRAOZRJSIBXDNCDBVPSEJRFVRSMISGQMSLAGZEVQTR"
    generator = AddressGenerator(seed=seed, security_level=2)
    num = 20
    results = generator.get_addresses(0, num)
    with open('./Snapshot.txt', 'w') as fs:
        for i in range(0, num-1):
            fs.write(str(results[i]) + ';' + '1000000000\n')
        fs.write(str(results[num-1]) +';' + str(2779530283277761-1000000000*(num-1)))


def single_thread_one_tx():
    start = int(time.time())
    for i in range(0, 10):
        tx.send_text()
        print(i)
    end = int(time.time())
    print(end - start)



if __name__ == '__main__':
    #single_thread_one_tx()
    generate_address()