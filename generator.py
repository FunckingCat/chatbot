from random import randint
from const import *

def generate_name(list):

    first_name = names[list["race"]+'-'+list["gender"]][randint(0, len(names[list["race"]+'-'+list["gender"]])-1)]
    last_name = names[list["race"]+'-subname'][randint(0, len(names[list["race"]+'-subname'])-1)]
    behavior = list['outlook'] + '-' + list['kindness']
    if list['race'] == 'Дварф' or list['race'] == 'Гном':
        clan = names[list['race']+'-'+'clan'][randint(0, len(names[list['race']+'-'+'clan'])-1)]
        return ' '.join([x for x in [behavior, list['class'], first_name, last_name, 'из клана', clan] if x])
    return (' '.join([behavior, list['class'], first_name, last_name]))
