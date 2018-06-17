# !/usr/bin/env python3
# _*_ coding:utf-8 _*_

'test_worker module'

__author__ = 'fengjinyuan'

import sys,time,queue,random
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('deal_task_queue')
QueueManager.register('get_result_queue')

ServerAddr = '127.0.0.1'
print('Connect to Server %s  ' % ServerAddr)

Manager = QueueManager(address=(ServerAddr,8888),authkey=
b'abc')
Manager.connect()
getdata = Manager.deal_task_queue()
putresult = Manager.get_result_queue()

for i in range(10):
    try:
        n =  getdata.get(timeout = 1)
        print('excute task %d*%d ' % (n,n))
        r = '%d * %d = %d ' % (n,n,n*n)
        time.sleep(1)
        putresult.put(r)
    except Queue.Empty:
        print('task queue is empty')
print('worker exit.')
