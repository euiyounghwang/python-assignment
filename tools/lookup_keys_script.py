
import json
import os
from datetime import datetime
from threading import Thread
import argparse
import os, sys
import asyncio
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from inject.injector import (logger, util, service_inject)



async def work(path1, path2, output) -> None:
    ''' main task '''
    try:
        logger.info(f'work from {path1}, {path2} -> {output}')
        
        source, dest = service_inject.load_files(path1, path2)
        
        ''' call service_inject.extract_results twice times to write file '''
        '''
        service_inject.extract_results(output, path1, source, dest)
        service_inject.extract_results(output, path2, dest, source)
        '''
        ''' call call service_inject.extract_results simultaneously to write file '''
        result = await asyncio.gather(
            service_inject.extract_results(output, path1, source, dest),
            service_inject.extract_results(output, path2, dest, source)
        )

    except Exception as e:
        pass
        

  
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
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(work(input_1, input_2, output))
        asyncio.run(work(input_1, input_2, output))
        # th1 = Thread(target=work, args=(input_1, input_2, output))
        # th1.start()
        # th1.join()
        
    except Exception as e:
        logger.error(e)
    