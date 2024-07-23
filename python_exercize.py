a= 'ciao' 
if a=='ciao':
    print('vero')


    a=['harry','ron','hermione']
    if 'harry' in a:
        print('harry è presente')
    else:
        print('harry non è presente')    


maghi= ['harry','ron','hermione']   

for mago in maghi:
    if mago=='harry':
        break
    print(mago)


    for i in range(5):
        print(i)

import random 
print (random.randint(1,3))
print (random.choice(1,3))

import os
print(os.listdir())
os.rename('sono un file rinominato')
print(os.listdir())