from random import randint

def get_name(race='human', gender='man'):
    file = open('names.txt', encoding='UTF-8')
    read = [''.join(x.split('\n')).split(':') for x in file] # файл парсится на списки в формате [['race-gender'], ['items']]
    file.close()
    keys = [x.pop(0) for x in read] # передаю ключи (формата race-gender) в один список
    items = [x[0].split(', ') for x in read] # передаю значения для ключей в другой список
    names = dict(zip(keys, items)) # объединяю в словарь
    first_name = names[race+'-'+gender][randint(0, len(names[race+'-'+gender]))] # из передаваемых функции аргументов race и gender формируются ключи, по которым находятся списки с именами
    last_name = names[race+'-subname'][randint(0, len(names[race+'-subname']))] # и при через randint беруются случайные комбинации
    return (first_name + ' ' + last_name)
