
__version__ = '0.1.0'

import re

def parse(text):
    dict = {}
    m = re.search('Add (.+?) mana', text)
    if m:
        value = m.group(1)
        dict['Add_mana'] = value
    return dict 
