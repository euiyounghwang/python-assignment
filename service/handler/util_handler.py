
import re

class Utils(object):
    ''' uitls include read files and sorted function '''
    def __init__(self, logger):
        self.logger = logger

    async def read_file(self, path):
        inputs = []
        try:
            with open(path, 'r') as f:
                while True:
                    line = self.transform_trim_string(f.readline())
                    # print(f'read line -- {line}')
                    if not line:
                        break
                    if not '#' in line:
                        inputs.append(line)
                return inputs
        except Exception as e:
            self.logger.error(e)
            
            
    def write_file(self, path, filename, results: list):
        # self.logger.info(f'write_file : {path}')
        full_path = path+'/output_'+ filename
        try:
            with open(full_path, 'w') as f:
                for item in results:
                    # print(item)
                    f.write(item + '\n')
                f.close()
        except Exception as e:
            self.logger.error(e)
        finally:
            self.logger.info(f'Succesfully write file into {full_path}')
        

    def transform_trim_string(self, to_replace):
        ''' transform with replace '''
        if isinstance(to_replace, (str)):
            to_replace = to_replace.strip()
            to_replace = re.sub(r'\n|\\n', '', to_replace)
            to_replace = re.sub(r'\t|\\t', '', to_replace)
            to_replace = re.sub(r'\f|\\f', '', to_replace)
            to_replace = re.sub(r'\s+', '', to_replace)

            return to_replace


    def sort_str_dict(self, s):
        ''' sort_str_list '''
        s_dict = {}
        s_sorted = sorted(s)
        for idx, s in enumerate(s_sorted):
            s_dict.update({s:idx+1})
        return s_dict
    
    
    async def lookup_difference(self, source, dest):
        ''' compare source and dest '''
        try:
            extract_result = [k for k, v in dest.items() if k not in source.keys()]
            # print(extract_result)
            return extract_result
        
        except Exception as e:
            self.logger.error(e)