
import json
import os
from datetime import datetime
from threading import Thread
import argparse
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from inject.injector import (logger, util)


def work(input1, input2, output):
    ''' main task '''
    try:
        logger.info(f'work from {input1}, {input2} -> {output}')
        logger.info(json.dumps(util.read_file(input1), indent=2))
    except Exception as e:
        logger.error("work - {}".format(str(e)))


  
if __name__ == "__main__":
    
    ''' 
        Run (Extract the following condtions between two files by using this script)
        poetry run python ./tools/lookup_keys_script.py
    '''
    parser = argparse.ArgumentParser(description="Index into Elasticsearch using this script")
    parser.add_argument('-a', '--input1', dest='input1', default="./dataset/a.txt", help='input file a')
    parser.add_argument('-b', '--input2', dest='input2', default="./dataset/b.txt", help='input file a')
    parser.add_argument('-o', '--output', dest='output', default="./dataset", help='path for output')
    args = parser.parse_args()
    
    if args.input1:
        input_1 = args.input1
        
    if args.input2:
        input_2= args.input2
        
    if args.output:
        output = args.output
        
    # util = Utils()
    # --
    # Only One process we can use due to 'Global Interpreter Lock'
    # 'Multiprocessing' is that we can use for running with multiple process
    # --
    try:
        th1 = Thread(target=work, args=(input_1, input_2, output))
        th1.start()
        th1.join()
        
    except ThreadIssue:
        pass
    