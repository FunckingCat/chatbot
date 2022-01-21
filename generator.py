from random import choice
from const import *


def generate_name(data):

    first_name = choice(names[data['race']+'-'+data['gender']])
    last_name = choice(names[data['race']+'-subname'])
    behavior = data['outlook']
    if data['race'] == 'Дварф' or data['race'] == 'Гном':
        clan = choice(names[data['race']+'-'+'clan'])
        if data['name'] == '__RANDOM__':
            return ' '.join([x for x in [behavior, data['class'], first_name, last_name, 'из клана', clan] if x])
        else:
            return ' '.join([x for x in [behavior, data['class'], data['name'], 'из клана', clan] if x])
    if data['name'] == '__RANDOM__':
        return (' '.join([x for x in [behavior, data['class'], first_name, last_name] if x]))
    else:
        return (' '.join([x for x in [behavior, data['class'], data['name']] if x]))
