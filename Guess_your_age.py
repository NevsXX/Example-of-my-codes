import json
import requests
from transliterate import translit
import os

def st():
    try:
        name = str(input("Вы попали на программу отгадывания возраста по имени \nВведите ваше имя: "))
        if 'ь' in name: name = name.replace('ь','i',1)
        r_name = translit(name,reversed=True)
        '''print('Вы ввели имя: ',r_name)'''
        res = requests.get(f'https://api.agify.io?name={r_name}&country_id=RU') 
        print('Ваш предположительный возраст:',res.json()["age"])
        anw = input('Продолжить?''\n')
        if anw == 'yes' or anw == 'Yes' or anw == 'Да' or anw == 'да': st()
        else: print('Увидимся!') ; exit
    except:
        os.system('CLS')
        print('ERROR: данные введены неверно''\n''\n''Повторный запуск''\n')
        st()
st()