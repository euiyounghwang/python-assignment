
def read_file(path):
    try:
        with open(path) as f:
            while True:
                line = f.readline()
                print(f'read line -- {line}')
                if not line:
                    break
    except Exception as e:
        logger.errors(e)


def sort_str_list(s):
    ''' sort_str_list '''
    s_dict = {}
    s_sorted = sorted(s)
    for idx, s in enumerate(s_sorted):
        s_dict.update({s:idx+1})
    return s_dict
    

# Driver Code
results = ["car", "cAr", "apple", "banana", "fan", "dog"]
print('1', results)
print('2', sort_str_list(results))
read_file('./dataset/a.txt')