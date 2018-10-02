# -*- coding: utf-8 -*-

import tx
import time
import os
from datetime import datetime
import threading
from pprint import pprint
import threadpool
from multiprocessing import Pool

adds = []
SIZE = 100
neighbors = ["56", "57", "58", "60", "61", "62", "63", "66"]


def get_address():
    adds = []
    with open('./Snapshot.txt', 'r') as fs:
        for line in fs.readlines():
            add = line.split(';')[0]
            adds.append(add)
    return adds

# send 0 value bundle by a single thread 
def single_thread_tx(size):

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    start = int(time.time())
    for i in range(0, size):
        tx.send_text()
        print(i)
    end = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(end - start)

# send a transfer (4 tx in a bundle) by a single thread
def single_thread_transfer(adds_index_list):
    url = "http://localhost:14700"
    start = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    for i in adds_index_list:
        print(i)
        tx.send_transfer(url, adds[i], adds[SIZE], i)     
    end = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(end - start)


# multi-thread by thread pool 
def multi_thread_tx(size):
    '''
    args = []

    url = "http://localhost:14700"
    for i in range(0, size):
        t = (url, i)
        args.append(t)
    print(args)
    '''
    args = list(range(0, size))
    pool = threadpool.ThreadPool(8) 
    requests = threadpool.makeRequests(_transfer_task, args) 
    start = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    [pool.putRequest(req) for req in requests] 
    pool.wait()
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    end = int(time.time())
    print(end - start)


# multi-process by fork
def multi_process_tx(size):
    pid = os.fork()
    if pid == 0:
        ppid1 = os.fork()
        if ppid1 == 0:
            single_thread_transfer([0])
            print('tx by thread 0')
            os._exit(os.EX_OK)
        else:
            single_thread_transfer([1])
            print('tx by thread 1')
            os._exit(os.EX_OK)
    else:
        ppid2 = os.fork()
        if ppid2 == 0:
            single_thread_transfer([2])
            print('tx by thread 2')
            os._exit(os.EX_OK)
        else:
            single_thread_transfer([3])
            print('tx by thread 3')
            os._exit(os.EX_OK)
    return
    

def _transfer_task(index):
    last_num = neighbors[index % 7 + 1]
    url = "http://192.168.5." + last_num + ":14700"
    print(index)
    tx.send_transfer(url, adds[index], adds[SIZE], index) 


# multi-process by process pool
def multi_transfer_with_pool(size):
    p = Pool(4)
    print('task start!')

    for i in range(0, size):
        p.apply_async(_transfer_task, args=(i, ))

    p.close()
    p.join()
    

if __name__ == '__main__':
    adds = get_address()

    start = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    #single_thread_tx(3)
    #single_thread_transfer(3)
    #multi_process_tx(1)
    #multi_thread_tx(100)
    

    multi_transfer_with_pool(4)

    end = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(end - start)


