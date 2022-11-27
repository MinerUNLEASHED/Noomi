# import sys
# import subprocess
# print('\n'*100)
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade','pip'])
# print('\n'*100)
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'bs4'])
# print('\n'*100)
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
# print('\n'*100)
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lxml'])
# print('\n'*100)


import time
import random
import requests
print('\n'*100)
print('Running Servers.')
time.sleep(1)
print('\n'*100)
print('Running Servers..')
time.sleep(1)
print('\n'*100)
print('Running Servers...')
time.sleep(1)
print('\n'*100)
print('Organizing Data')
time.sleep(1)
print('\n'*100)
print('.')
time.sleep(1)
print('\n'*100)
print('.  .')
time.sleep(1.2)
print('\n'*100)
print('.  .  .')
time.sleep(1.4)
print('\n'*100)
print('.  .  .  .')
time.sleep(1.6)
print('\n'*100)
print('Done!')
time.sleep(1)
print('\n'*100)


print('Hello!')
print('This is The Noomi Set Creator')
option = 'here'
print('\n'*100)
if option == 'here':
    howmany = int(input('How Many Terms Are In Your Set? '))
    print('\n'*100)
    set = {}
    for i in range(howmany):
        key = input(f'Card {i+1} Term: ')
        value = input(f'Card {i+1} Definition: ')
        print('\n'*100)
        set[key] = value
    
    

print('Okay - Thanks For The Terms! Now, Let\'s Study!')
print('At Any Time, Type quit to to stop the studying')
time.sleep(5)
print('\n'*100)


while True:
    keylist = list(set.keys())
    answerlist = list(set.values())
    question = random.choice(keylist)
    real_question = ''
    for i in question:
        real_question = i
    answer = set[question]
    print(real_question)
    print('\n')
    human_answer = input('Answer: ')
    if human_answer == answer:
        print("Correct!")
    elif human_answer == 'quit':
        print("Okay-The Program Has Been Stopped - Here Is A List Of Your Vocabulary Terms(In Case You Want To Import These Terms Somewhere Else)")
        for i in range(howmany):
            print(f'{keylist[i]}\t{answerlist[i]}')
        break
    else:
        print('\n')
        print('Incorrect!')
        print(f'The Correct Answer Is: {answer}')
        time.sleep(3)
    print('\n'*100)
        
