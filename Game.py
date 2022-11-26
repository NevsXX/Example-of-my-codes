import random
import time
import keyboard
import os

#боты
class bot:
    Names = ['Mabel','Mackenzie','Mia','Jaden','Jeffery','Jesus','Joseph Jostar','Juan','Horace','Hunter','George','Gordon','Carlos','Connor','Cody','clown Joker','rap rocker','Rayan Gosling']
    def __init__(self,name=Names[random.randint(0,19)],creampie=random.randint(0,20000),points=random.randint(6,30)):
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

    def take_card_2(self):
        self.points += random.randint(6,12)
        print('\n''You take card','\n''Your points: ',self.points)
        return self.points
    
    def take_card(self):
        self.points += random.randint(6,12)
        return self.points
    
    
    def your_bet(self):
        credit = int(input('Write your credit: '))
        self.creampie -= credit
        print('Your bet: ',credit,'\n''Your cash: ',self.creampie)
        return self.creampie, credit
    
#Подсчет результатов и конец игры    
def the_end(count):
    me.points += random.randint(6,12)
    if me.points > 21:
            print('Ваши очки: ',me.points,'\n' 'Вы проиграли')
            
    elif me.points == 21:
            me.creampie  + (credit * 2)
            print(me.name, 'Набрал 21 очко и является победителем')
    else:
        while count>=0:
            count -= 1
            a = bot()
            if a.points == 21:
                a.creampie + (credit * 2)
                print(a.name, '- Winner')
                break
            else:
                if a.points > 21:
                    a.creampie - credit
                    break
                elif a.points < 21 and a.points > me.points:
                    a.creampie + (credit * 2)
                    print(a.name, '- победил, так как имеет больше всего очков',a.points)
                    break
                else:
                    me.creampie  + (credit * 2)
                    print(me.name,'Победил, так как имеет',me.points,'\n' 'Ваш кредит был возвращен в двойном размере')
                    break
                
    
    
    
    
#Начально меню
def menu():
    print('\n''Start 21 - press Q ','\n' 'Show my state - press A','\n''Exit from game - press ESC','\n' 'Instruction - press Z')
    keyboard.add_hotkey('Z', inst)
    keyboard.add_hotkey('A', show_my_state)
    keyboard.wait('Q')
    
'''def game():
    keyboard.add_hotkey('Z', inst)
    keyboard.add_hotkey('S', me.take_card)
    keyboard.add_hotkey('A', show_my_state)
    keyboard.add_hotkey('X',the_end)
    me.your_bet()
    me.take_card(0)
    print('\n' 'Начинается раздача карт.')
    print('\n''Ваш счет: ', me.points, '\n' 'Если хотите взять еще карту нажмите -  S','\n''Чтобы закончить игру и вскрыть неизвестну карту нажмите - X')
    keyboard.wait('esc')'''
    
#Функция изображения загрузки
def download(n):
    for i in range(101):
        dw = str(i)+ '%'
        print('  ',dw, end='')
        print('\r', end='')
        k = random.uniform(0.02,0.3)/n
        time.sleep(k)

#Отображение статы
def show_my_state():
    me.show()

#Инструкция
def inst():
        print('\n''Start 21 - press Q ','\n' 'Show my state - press S','\n''Exit from game - press ESC','\n' 'Instruction - press I')        

#Приветствие игры
a = 0
credit = 0
clear = lambda: os.system('cls')
clear()
print('Добро пожаловать в игру 21','\n')
download(4)
clear()

#Заполнение класса пользователя и создание ботов
count = int(input("введите количество игроков: "))
bots = []
for i in range(count-1):
    bots.append(bot())
my_name = str(input('Введите ваше имя: '))
my_creampie = int(input('Введите вашу денежку: '))
my_gender = str(input('Введите ваш пол (гендер): '))
me = user(my_creampie, my_name, my_gender)
clear()
print('\n''  Saving','\n')
download(1)
clear()

#Начало игры
print("Ваш статус: ","\n")
me.show()
print('\n')
download(4)
print('\n')
menu()

#Игра
clear()
me.your_bet()
me.take_card()
keyboard.add_hotkey('S', me.take_card_2)
keyboard.add_hotkey('A', show_my_state)
keyboard.add_hotkey('X', lambda: the_end(count))
keyboard.add_hotkey('Z', inst)
print('\n' 'Начинается раздача карт.')
download(2)
clear()
print('\n''Ваш счет: ', me.points, '\n' 'Если хотите взять еще карту нажмите -  S','\n''Чтобы закончить игру и вскрыть неизвестную карту нажмите - X')
keyboard.wait('esc')