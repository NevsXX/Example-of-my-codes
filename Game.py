import random
import time
import keyboard
import os

#боты
class bot:
    Names = ['Mabel','Mackenzie','Mia','Jaden','Jeffery','Jesus','Joseph Jostar','Juan','Horace','Hunter','George','Gordon','Carlos','Connor','Cody','clown Joker','rap rocker','Rayan Gosling']
    def __init__(self,name=Names[random.randint(0,19)],creampie=random.randint(0,20000),points=random.randint(4,30)):
        self.name = name
        self.creampie = creampie
        self.points = points
    def show(self):
        print('Name:',self.name,'\n' 'Money:',self.creampie, '\n' 'Points:',self.points)

#Главный игрок
class user:
    def __init__(self, creampie=0, name='Unknow', gender='Unknow',points=0):
        self.creampie = creampie
        self.name = name
        self.gender = gender
        self.points = points

    def show(self):
        print('Name:',self.name, '\n' 'Gender:',self.gender, '\n''Creampie count:',self.creampie,'\n''Points:',self.points)

    def take_card(self):
        self.points += random.randint(6,12)
        print('\n''Points was plus','\n''Your points: ',self.points)
        return self.points
    
    def your_bet(self):
        credit = int(input('Write your credit: '))
        self.creampie -= credit
        print('Your bet: ',credit,'\n''Your cash: ',self.creampie)
        return self.creampie, credit
    
#Подсчет результатов и конец игры    
def the_end():
    print('Funcion the_end worked')   
#Меню
def menu():
    print('\n''Start 21 - press Q ','\n' 'Show my state - press S','\n''Exit from game - press ESC')
    keyboard.add_hotkey('S', show_my_state)
    keyboard.add_hotkey('Q', game)
    keyboard.wait('esc')
    
def game():
    me.your_bet()
    keyboard.add_hotkey('A', me.take_card)
    keyboard.wait('esc')
    
#Функция изображения загрузки
def download(n):
    for i in range(101):
        dw = str(i)+ '%'
        print('  ',dw, end='')
        print('\r', end='')
        k = random.uniform(0.02,0.3)/n
        time.sleep(k)
        
def show_my_state():
    me.show()


#Приветствие игры
credit = 0
clear = lambda: os.system('cls')
clear()
print('Добро пожаловать в игру 21','\n')
time.sleep(1)
clear()

#Заполнение класса пользователя и создание ботов
count = int(input("введите количество игроков: "))
bots = []
for i in range(count):
    bots.append(bot())
my_name = str(input('Введите ваше имя: '))
my_creampie = int(input('Введите вашу денежку: '))
my_gender = str(input('Введите ваш пол (гендер): '))
me = user(my_creampie, my_name, my_gender)
clear()
print('\n''  Saving','\n')
#download(1)
clear()

#Начало игры
print("Ваш статус","\n")
me.show()
"""download(4)"""
menu()