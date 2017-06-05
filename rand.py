import random
import time

ran_sack=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
lowcaps=''.join(map(str,ran_sack))
#print(lowcaps)
ran_sample=['0','1','2','3','4','5','6','7','8','9']
nums=''.join(map(str,ran_sample))
#print(nums)
ran_symbol=['!','@','#','%','^','&','*','(',')',':','{','}','|','<','>','/','\',']
symbol=''.join(map(str,ran_symbol))
symbol2=''.join(map(str,ran_symbol))
symbol3=''.join(map(str,ran_symbol))
#print(symbol)
ran_caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
caps=''.join(map(str,ran_caps))
#print(caps)

for i in range(0,1):
    lowcaps = random.sample(lowcaps,4)
    nums = random.sample(nums,4)
    symbol= random.sample(symbol,4)
    caps= random.sample(caps,4)
    symbol2= random.sample(symbol2,4)
    symbol3= random.sample(symbol3,8)
    pw = ''.join(map(str,lowcaps+nums+symbol+caps))
    pw2 = ''.join(map(str,nums+symbol+lowcaps+caps))
    pw3 = ''.join(map(str,caps+nums+symbol+lowcaps))
    pw4 = ''.join(map(str,symbol2+lowcaps+nums))
    pw5 = ''.join(map(str,symbol3+caps+lowcaps))
    
    
    
    #print("Here are a few random choices.")
    #print("1.",pw)
    #print("2.",pw2)
    #print("3.",pw3)
    #print("4.",pw4)
    #print("5.",pw5)
    print("Please wait, randomizing your new password.")
    time.sleep(2)
    a=pw
    b=pw2
    c=pw3
    d=pw4
    e=pw5
    created=(d[1]+a[2:3]+c[5:8]+b[11:12]+e[5]+c[3:10]+b[0:2]+a[3:7]+a[5:3]+d[2]+c[8:4])
    print("21 characters is a strong password. However, you can trim it.\n Choose between 10 and 21 characters if you would like to trim your password.")
    print("If not, your 21 character password is: ")
    print(created)
    newlen = eval(input("How many characters long should the string be? (Between 10 and 21):  "))


#if the user wants the length to be a number between 10 and 15 print the
#string according to the users wants.
def ten():
    ten = (created[0:10])
    print(ten)
    print("This string is",len(ten),"characters long.")
def eleven():
    eleven = (created[0:11])
    print(eleven)
    print("This string is",len(eleven),"characters long.")
def twelve():
    twelve = (created[0:12])
    print(twelve)
    print("This string is",len(twelve),"characters long.")
def thirteen():
    thirteen = (created[0:13])
    print(thirteen)
    print("This string is",len(thirteen),"characters long.")
def fourteen():
    fourteen = (created[0:14])
    print(fourteen)
    print("This string is",len(fourteen),"characters long.")
def fifteen():
    fifteen = (created[0:15])
    print(fifteen)
    ("This string is",len(fifteen),"characters long.")
def sixteen():
    sixteen = (created[0:16])
    print(sixteen)
    print("This string is",len(sixteen),"characters long.")
def seventeen():
    seventeen = (created[0:17])
    print(seventeen)
    print("This string is",len(seventeen),"characters long.")
def eighteen():
    eighteen = (created[0:18])
    print(eighteen)
    print("This string is",len(eighteen),"characters long.")
def nineteen():
    nineteen = (created[0:19])
    print(nineteen)
    print("This string is",len(nineteen),"characters long.")
def twenty():
    twenty = (created[0:20])
    print(twenty)
    print("This string is",len(twenty),"characters long.")

if newlen == 10:
    ten()
    
elif newlen == 11:
    eleven()
    
elif newlen ==12:
    twelve()
    
elif newlen == 13:
    thirteen()
    
elif newlen == 14:
    fourteen()
    
elif newlen == 15:
    fifteen()
    
elif newlen == 16:
    sixteen()
    
elif newlen == 17:
    seventeen()
    
elif newlen == 18:
    eighteen()
    
elif newlen == 19:
    nineteen()
    
elif newlen == 20:
    twenty()
    
elif newlen == 21:
    print(created)
    
else:
    print("Goodbye")






    
    #import random

##ran_sack=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
#lowcaps=''.join(map(str,ran_sack))
#print(lowcaps)
#ran_sample=['0','1','2','3','4','5','6','7','8','9']
#nums=''.join(map(str,ran_sample))
#print(nums)
#ran_symbol=['!','@','#','%','^','&','*','(',')']
#symbol=''.join(map(str,ran_symbol))
#ran_caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#caps=''.join(map(str,ran_caps))
#for i in range(0,3):
 #   #print(ran_sample+ran_sack+ran_symbol)
 #   ran_sack = random.sample(ran_sack,3)
  #  ran_sample = random.sample(ran_sample,3)
  #  ran_symbol= random.sample(ran_symbol,3)
   # ran_caps= random.sample(ran_caps,2)
   # pw = str(ran_sack+ran_sample+ran_symbol+ran_caps)
   # print("This would be a simple password, but it needs to be randomly sorted.")
#print(lowcaps+nums)    
