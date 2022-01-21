from random import choice
from const import *

def generate_name(list):

    first_name = choice(names[list["race"]+'-'+list["gender"]])
    last_name = choice(names[list["race"]+'-subname'])
    behavior = list['outlook'] + '-' + list['kindness']
    if list['race'] == 'Дварф' or list['race'] == 'Гном':
        clan = choice(names[list['race']+'-'+'clan'])
        return ' '.join([x for x in [behavior, list['class'], first_name, last_name, 'из клана', clan] if x])
    return (' '.join([behavior, list['class'], first_name, last_name]))
