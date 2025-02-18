# vosper: a simple tool to easily get high-quality Automatic Speech Recognition using SOTA models
from os import system as cmd
from vosper import listener
import time




def vspr_run(queue, stopFlag, listenEvent, listenCD):
    
    mic, rec = listener.Stream(), listener.load(model='small') # you can download more realtime models here: https://alphacephei.com/vosk/models
    print('Listener ready.')
    listenEvent.set()
    while 'listening':
        if stopFlag.qsize() == 0:
            _input = listener.listen(mic, rec, listenCD)
            if _input is not None:
                queue.put(_input)
                
                
        else:
            time.sleep(1)

        #if ('-' in _input):
        #    print(_input)
        #elif (_input != ''):
        #    cmd('cls'); print('- '+ _input)