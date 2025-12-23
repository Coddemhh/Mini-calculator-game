#import module
import time
from random import randint
import os

#def operations and clear
def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def times(x,y):
    return x*y

def div(x,y):
    return x//y

def clearscreen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

#start up
print('Welcome to the speed calculating game.')
time.sleep(2)
print('In this game, you will be given a math question every round, you have to calculate them not using any outer assistance.')
time.sleep(3)
print('Be fast! You only got a few strikes if you get them wrong! Also, taking too long may also add a strike on your name! You will play until you used up all your strikes or finish the level.')
time.sleep(3)
print('The questions get harder over time! Stay strong!')
time.sleep(2)

#mode selection, description
print('Now, select the mode you are going to play in, easy,hard,demon,unlimited.')

mode = input('Select between hard,easy,demon and unlimited mode(Input description to get more information):')
mode = mode.lower()
while True:    
    if mode == 'exit':
        print('Thank you for playing.')
        exit()                                                                        
    elif mode == 'description':
        print('''
            Mode selection:
            There are four modes: easy, hard, demon, and unlimited.
            For easy mode, there are only plus and minus operation for the player to operate.
            And the strike number is also higher, with 5, time limit is also longer, recommended for stupid people.
            For hard mode, multiplication and division will also be present in the question.
            The number of strikes is reduced to 3. But to compensate, time limit will be increased.   
            For demon mode, it is a even harder version of hard mode, with even less time allowed for each round,
            and less strikes.
            For unlimited mode, it is a version of hard mode where you can play unlimited rounds, as long as you don't use up all the strikes.                                    
            ----------------------------------------------------------------------------------------------------------------
            To exit the game manually, just input 'exit' at any time.
            ----------------------------------------------------------------------------------------------------------------
            Credits:
            This game is coded by Patrick,in 11-2025.
            ----------------------------------------------------------------------------------------------------------------
            History:
            Alpha 1.0(7pm 14-11-2025): First version
            Alpha 1.1(8pm 14-11-2025): Fixed problems on strike counting, improve clarity, added data validation, improved performence
            Beta 1.0(1am 15-11-2025): added grading system, added mode 'unlimited' and 'demon', fixed manual quitting failure problem
            Beta 1.1(8pm 4-12-2025): added answer validation, clearscreen
            ----------------------------------------------------------------------------------------------------------------
            Creater comments:
            It's late at night now so i will probably make i lot of mistakes and miss some functions i promised to include.
            This is my first project and i hope it goes well.(11pm 13-11-2025)
            ''')
    elif mode == 'hard' or mode == 'easy' or mode == 'joe' or mode == 'demon' or mode == 'unlimited':                        
        break
    mode = input('Select between hard,easy,demon and unlimited mode(Input description to get more information):')

#setting up some varaibles, dicts
round_count = 0
total_time = 0
min_time = 100
ops = ['+','-','*','//']

oper_dict = {
    '+':add,
    '-':minus,
    '*':times,
    '//':div
}

if mode == 'joe':
    while True:
        print('YOU DONT DESERVE TO LIVE.......................')#joe i love u 
elif mode == 'easy':
    time_limit = 4
    strike_count = 5
    upper = 20
    op_count = 1
    round_limit = 30
elif mode == 'hard' or mode == 'unlimited':
    time_limit = 6
    strike_count = 3
    upper = 30
    op_count = 3
    if mode == 'hard':
        round_limit = 50
    else:
        rount_limit = 10**10
elif mode == 'demon':
    time_limit = 5
    strike_count = 2
    upper = 50
    op_count = 3
    round_limit = 70


#main part lets go
ans = ''
ori = strike_count
sta = 'cor'
time_taken = 0

while strike_count >= 1 and round_count < round_limit:
    time.sleep(1.2)
    clearscreen()
    if (round_count % 5 == 0) and (round_count != 0):
        upper = upper + 20
    first = randint(1,upper)
    second = randint(1,upper)
    op = ops[randint(0,op_count)]
    while op == '//' and first % second != 0:
        second = randint(1,upper)
    if op in oper_dict:
        actual = oper_dict[op](first,second)
    print()
    print('Strikes you have left:',strike_count)
    print('The time taken for last question:',time_taken,'seconds')
    print('Your questions is:',str(first)+op+str(second))
    start = time.time()
    ans = input('Your answer:')
    while type(ans) == str:
        try:
            ans = int(ans)
        except ValueError:
            if ans == 'exit':
                print('Thank you for playing.')
                exit()
            print('Wrong data type')
            ans = input('Your answer:')
    end = time.time()
    time_taken = end - start
    time_taken = round(time_taken,2)      #strikes
    if (ans == actual) and (time_taken < time_limit):
        sta = 'cor'
        if (time_taken < min_time) and (sta == 'cor'):
            min_time = time_taken
    elif (time_taken > time_limit) and (ans == actual):
        sta = 'incor'
        strike_count -= 1
        print('You have gotten it right but you took too long!')
    else:
        sta = 'incor'
        strike_count -= 1
        print('You have gotten it wrong!')
    total_time += time_taken
    round_count += 1

#generating results
grade = ''
mark = 0
total_time = round(total_time,2)
avg_time = total_time/round_count
avg_time = round(avg_time,2)
accu = (round_count-(ori-strike_count))/round_count
accu = round(accu*100,1)
grades = ['Joe','B','A','S']     #cri:min time(0-2),avg time(0-2),accu(1-4)=total 8
if accu == 100:
    grade = 'Perfecto!'
mark += int(accu//25)+1
if avg_time < 4:
    mark += 1
    if avg_time < 3:
        mark += 1
if min_time < 2:
    mark += 1
    if avg_time < 1:
        mark += 1
grade = grades[(mark//2)-1]

print()
if strike_count == 0:
    print('Unfortunately, you have used up all your strikes...')
elif round_count >= round_limit:
    print('Congrats! You beat the level!')
time.sleep(2)
print('Here are your results:')
time.sleep(2)
print('You have played',str(round_count),'rounds.')
time.sleep(2)
print('You use a total time of:',str(total_time),'seconds.')
time.sleep(2)
print('With an average time of:',str(avg_time),'seconds.')
time.sleep(2)
print('You only used',str(min_time),'seconds in one of the questions! How amazing!')
time.sleep(2)
print('Your accuracy is:',str(accu)+'%')
time.sleep(2)
print('Your grade is',end='')
for i in range(20):
    print('.',end='')
print()
time.sleep(2)
print(grade)
time.sleep(2)
print('At last, thank you for playing!')
exit()

























