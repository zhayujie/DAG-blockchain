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
SIZE = 300
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
def single_thread_transfer(add_list):
    url = "http://192.168.5.57:14700"
    start = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    for i in add_list:
        print(i)
        tx.send_transfer(url, adds[i], adds[SIZE], i)     
    end = int(time.time())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(end - start)

def multi_process_tx(size):
    pid = os.fork()
    if pid == 0:
        ppid1 = os.fork()
        if ppid1 == 0:
            single_thread_transfer([10, 11, 12])
            print('tx by thread 0')
            os._exit(os.EX_OK)
        else:
            single_thread_transfer([13, 14])
            print('tx by thread 1')
            os._exit(os.EX_OK)
    else:
        ppid2 = os.fork()
        if ppid2 == 0:
            single_thread_transfer([15, 16, 17])
            print('tx by thread 2')
            os._exit(os.EX_OK)
        else:
            single_thread_transfer([18, 19])
            print('tx by thread 3')
            os._exit(os.EX_OK)
    return



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

def _transfer_task(index):
    last_num = neighbors[index % 7 + 1]
    url = "http://192.168.5." + last_num + ":14700"
    #url = "http://192.168.5.57:14700"
    #print(index)
    a = time.time()
    tx.send_transfer(url, adds[index], adds[SIZE], index)     
    #tx.send_text(url)
    b = time.time()
    print(b - a)

    #tx.send_text(url)


def multi_transfer_with_pool(size):
    p = Pool(8)               # 8 processes in 8-cpu is optimal
    print('task start!')

    for i in range(0, size):
        p.apply_async(_transfer_task, args=(i,))

    p.close()
    p.join()
    

if __name__ == '__main__':
    adds = get_address()
    #single_thread_tx(3)
    #single_thread_transfer(list(range(0,8)))
    #multi_process_tx(1)
    #multi_thread_tx(100)
    a = time.time()
    #print(a)
    multi_transfer_with_pool(300)
    b = time.time()
    #print(b)
    print(b - a)
    
