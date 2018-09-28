# -*- coding: utf-8 -*-

import tx
import time
import os
from datetime import datetime
import threading
from pprint import pprint
import threadpool

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
def single_thread_transfer(size):
    url = "http://localhost:14700"
    start = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    for i in range(0, size):
        print(i)
        tx.send_transfer(url, adds[i], adds[size], i)     
    end = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(end - start)

def multi_process_tx(size):
    pid = os.fork()
    if pid == 0:
        single_thread_transfer(size)
        print('tx by thread 0')
    else:
        single_thread_transfer(size)
        print('tx by thread 1')
        os._exit(os.EX_OK)
    return


def _transfer_task(index):
    last_num = neighbors[index % 8]
    url = "http://192.168.5." + last_num + ":14700"
    print(index)
    tx.send_transfer(url, adds[index], adds[SIZE], index)     

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
    pool = threadpool.ThreadPool(16) 
    requests = threadpool.makeRequests(_transfer_task, args) 
    start = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    [pool.putRequest(req) for req in requests] 
    pool.wait()
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    end = int(time.time())
    print(end - start)

if __name__ == '__main__':
    adds = get_address()
    #single_thread_tx(3)
    #single_thread_transfer(3)
    #multi_process_tx(5)
    multi_thread_tx(100)


