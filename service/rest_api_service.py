
import json
import os

class ServiceHandler(object):
    
    def __init__(self, util, logger):
        self.logger = logger
        self.util = util
    
    
    async def load_files(self, path1, path2):
        ''' compare and write results '''
        source = await self.util.read_file(path1)
        dest = await self.util.read_file(path2)
        
        return source, dest


    def extract_results(self, output, path, source, dest):
        ''' single process to write file '''
        try:
            results = self.util.lookup_difference(source=self.util.sort_str_dict(source), 
                                                  dest=self.util.sort_str_dict(dest))
            self.logger.info(json.dumps(results, indent=2))
            # print(f'{path}')
            self.util.write_file(output, os.path.basename(path), results)
            
        except Exception as e:
            self.logger.error(e)
            
            
    async def extract_results_parallel(self, output, path, source, dest) -> None:
        ''' parallel process to write file '''
        try:
            results = await self.util.lookup_difference(source=self.util.sort_str_dict(source), 
                                                  dest=self.util.sort_str_dict(dest))
            self.logger.info(json.dumps(results, indent=2))
            # print(f'{path}')
            self.util.write_file(output, os.path.basename(path), results)
            return results
            
        except Exception as e:
            self.logger.error(e)