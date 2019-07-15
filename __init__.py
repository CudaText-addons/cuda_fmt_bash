import re
import json
from .beautysh import Beautify
from cuda_fmt import get_config_filename

fmt = Beautify()

def do_format(text):

    fn = get_config_filename('Bash Beautify')
    s = open(fn, 'r').read()
    #del // comments
    s = re.sub(r'(^|[^:])//.*', r'\1', s)
    d = json.loads(s)

    fmt.tab_size = d.get('tab_size', 4)
    fmt.tab_str = d.get('tab_str', ' ')
    fmt.apply_function_style = d.get('apply_function_style', None)

    res, error = fmt.beautify_string(text)
    return res
