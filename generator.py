from random import randint

def get_name(race='human', gender='man'):
    file = open('names.txt', encoding='UTF-8')
    read = [''.join(x.split('\n')).split(':') for x in file]
    names = dict(zip([x.pop(0) for x in read], [x[0].split(', ') for x in read]))
    file.close()
    return (names[race+'-'+gender][randint(0, len(names[race+'-'+gender]))] + ' ' + names[race+'-subname'][randint(0, len(names[race+'-subname']))])
