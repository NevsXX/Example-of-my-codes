import random
import time
import keyboard
import os
import sys

#боты
class bot:
    Names = ['Mabel','Mackenzie','Mia','Jaden','Jeffery','Jesus','Joseph Jostar','Juan','Horace','Hunter','George','Gordon','Carlos','Connor','Cody','clown Joker','rap rocker','Rayan Gosling']
    def __init__(self,name=Names[random.randint(0,19)],creampie=random.randint(1,20000),points=random.randint(6,30)):
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
        credit = int(input('Write your bet: '))
        self.creampie -= credit
        print('Your bet: ',credit,'\n''Your cash: ',self.creampie)
        return self.creampie, credit
    
#Подсчет результатов и конец игры    
def the_end(count):
    me.points += random.randint(6,11)
    if me.points > 21:
            print('\nYour points: ',me.points,'\n' 'You lose','\n' 'Your bet was lost')
            
    elif me.points == 21:
            me.creampie  += (credit * 2)
            print(me.name, 'Take 21 points and win!')
    while count>=0:
        count -= 1
        a = bot()
        if a.points == 21:
            a.creampie += (credit * 2)
            print(a.name, '- winner','\n',a.name, '- take 21 points','\n' 'You had: ',me.points,' points')
            break
        else:
            if a.points > 21:
                a.creampie -= credit
                break
            elif a.points < 21 and a.points > me.points:
                a.creampie += (credit * 2)
                print(a.name, '- winner, because it has the nearest number to 21: ',a.points,'points')
                break
            else:
                me.creampie  += (credit * 2)
                print(me.name,'\nYou win because you have',me.points,'\n' 'You take 2x CASH')
                break
    
#Начально меню
def menu():
    print('\n''Start 21 - press Q ','\n' 'Show my state - press A','\n''Exit from game - press ESC','\n' 'Instruction - press Z')
    keyboard.add_hotkey('Z', inst)
    keyboard.add_hotkey('A', show_my_state)
    keyboard.add_hotkey('esc', exit)
    keyboard.wait('Q')
        
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
    print('\n')
    me.show()

#Выход
def exit():
    clear()
    print('Goodbye')
    time.sleep(3)
    clear()
    sys.exit()

#Инструкция
def inst():
        print('\n''Start 21 - press Q ','\n' 'Show my state - press A','\n''Exit from game - press ESC','\n' 'Instruction - press Z')        

#Приветствие игры
a = 0
credit = 0
clear = lambda: os.system('cls')
clear()
print('Welcome to 21 game','\n')
download(4)
clear()

#Заполнение класса пользователя и создание ботов
try:
    count = int(input("Write the number of opponents: "))
    bots = [] 
    for i in range(count-1):
        bots.append(bot())
    my_name = str(input('Write your name: '))
    my_creampie = int(input('Write your cash: '))
    my_gender = str(input('Write your gender: '))
except:
    clear() 
    print('\nERROR\nData is entered incorrectly\nTry again')
    time.sleep(3)
    exit()
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
print('\n' 'disrtibution of cards')
download(2)
clear()
print('\nYour points: ', me.points, '\n' 'Take card -  S','\n''Open a closed card and finish the game - X')
keyboard.wait('esc')