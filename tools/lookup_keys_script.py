
import json
import os
from datetime import datetime
from threading import Thread
import argparse
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from inject.injector import (logger, util, service_inject)


# def load_files(path1, path2):
#     ''' compare and write results '''
#     source = util.read_file(path1)
#     dest = util.read_file(path2)
    
#     return source, dest


# def extract_results(path, source, dest):
#     results = util.lookup_difference(source=util.sort_str_dict(source), dest=util.sort_str_dict(dest))
#     logger.info(json.dumps(results, indent=2))
#     # print(f'{path}')
#     util.write_file(output, os.path.basename(path), results)


def work(path1, path2, output):
    ''' main task '''
    try:
        logger.info(f'work from {path1}, {path2} -> {output}')
        
        source, dest = service_inject.load_files(path1, path2)
        
        service_inject.extract_results(output, path1, source, dest)
        service_inject.extract_results(output, path2, dest, source)
        
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
    