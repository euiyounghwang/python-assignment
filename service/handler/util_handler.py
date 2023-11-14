
import re

class Utils(object):
    ''' uitls include read files and sorted function '''
    def __init__(self, logger):
        self.inputs = []
        self.logger = logger

    def read_file(self, path):
        inputs = []
        try:
            with open(path) as f:
                while True:
                    line = self.transform_trim_string(f.readline())
                    # print(f'read line -- {line}')
                    if not line:
                        break
                    if not '#' in line:
                        self.inputs.append(line)
                return self.inputs
        except Exception as e:
            self.logger.error(e)


    def transform_trim_string(self, to_replace):
        ''' transform with replace '''
        if isinstance(to_replace, (str)):
            to_replace = to_replace.strip()
            to_replace = re.sub(r'\n|\\n', ' ', to_replace)
            to_replace = re.sub(r'\t|\\t', ' ', to_replace)
            to_replace = re.sub(r'\f|\\f', ' ', to_replace)
            to_replace = re.sub(r'\s+', ' ', to_replace)

            return to_replace


    def sort_str_list(self, s):
        ''' sort_str_list '''
        s_dict = {}
        s_sorted = sorted(s)
        for idx, s in enumerate(s_sorted):
            s_dict.update({s:idx+1})
        return s_dict