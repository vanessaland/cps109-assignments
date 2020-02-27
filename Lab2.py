def bingo(name, money) :
  print (name + ' called Bingo and won $' + str(money) + '!')

def runner(number, mile, time) :
  print ('Runner #' + str(number) + ' passed mile ' + str(mile) + ' at time ' + str(time))

def invertedpyramid(character) :
  b = ' '
  s = character
  print 9 * s
  print 1 * b + 7 * s
  print 2 * b + 5 * s
  print 3 * b + 3 * s
  print 4 * b + 1 * s

def textsquare(ch, n) :
  print (ch*n)
  for x in range(n-2) :
     print (ch + ' '*(n-2) + ch)
  print (ch*n)

def justConsonants(string) :
  vowels = 'AEIOUYaeiouy'
  for x in string:
    if x not in vowels:
      print x,
  print
   
def justConsonants2(string) :
  vowels = 'aeiouy'
  for x in string :
    if x.lower() not in vowels:
      print x,
  print  
  
def dup1(s) : 
   target = ''
   for letter in s :
     target = target + letter
   return target 
   
def dup2(s) : 
  target = ''
  for letter in s :
    target = target + s
  return target
  
def dup3(s) : 
  target = ''
  for letter in s :
    target = letter + target + letter 
  return target

def dup4(s) : 
  target = ''
  for letter in s :
    target = letter + target 
  return target
  
def dup5(s) : 
  target = ''
  for letter in s :
      target = letter + '-' + target + '-' + letter
  return target
  
def separate(string):
  vowels = 'AEIOUYaeiouy'
  
  print ('Vowels:'),
  for x in string:
    if x in vowels:
      print x,
  print
  
  print ('Consonants:'),
  for x in string:
    if x not in vowels:
      print x,
  print
  
def buildCipher(key) :
  alpha1 = 'abcdefghijklmnopqrstuvwxyz' 
  alpha2 = key
  for letter in alpha1 :
    if letter not in key : 
      alpha2 = ""
  return alpha2

def encode(string, alpha2) :
  alpha1 = 'abcdefghijklmnopqrstuvwxyz' 
  secret = ''
  for letter in string :
    i = alpha1.find(letter)
    secret = secret + alpha2[i] 
  return secret

def encode2(string, alpha2) :
  alpha1 = 'abcdefghijklmnopqrstuvwxyz'
  secret = ''
  for letter in string :
    if letter not in alpha1:
      secret = secret + ''
    else:
      i = alpha1.find(letter)
      secret = secret + alpha2[i]
  return secret
  