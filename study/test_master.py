# !/usr/bin/env python3
# _*_ coding:utf-8 _*_

'test_master module'

__author__ = 'fengjinyuan'

import sys,time,queue,random
from multiprocessing.managers import BaseManager

# Create Task Queue
TaskQueue = queue.Queue()
# Create Result Queue
ResultQueue = queue.Queue()

# inherit BaseManager

class QueueManager(BaseManager):
    pass
# register Task Queue
QueueManager.register('deal_task_queue',callable = lambda: TaskQueue)
QueueManager.register('get_result_queue',callable = lambda: ResultQueue)
# bind port 8888,set authkey 'abc'
manager =QueueManager(address = ('',8888),authkey = b'abc')
manager.start()
putdata = manager.deal_task_queue()
getresult = manager.get_result_queue()

for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d ' % n)
    putdata.put(n)
print('Try get results....')
for i in range(10):
    r =getresult.get(timeout = 10)
    print("result: %s " % r)

# close manager
manager.shutdown()
print('master exit.')
