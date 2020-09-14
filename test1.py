def showBeach():
  beach = '/Users/vanessalandayan/Downloads/CPS109/mediasources-4ed/beach.jpg'
  beachPic = makePicture(beach)
  show(beachPic)
  
def sumOrds(string):
  sum = 0
  for x in string:
    num = ord(x)
    sum += num
  return sum

def catChrs(stringOfDigits):
  alpha = 'abcdefghij'
  for x in stringOfDigits:
     x = int(x)
     print alpha[x],
     
def sumRed(picture, n):
  pixels = getPixels(picture)
  sum = 0
  for x in pixels:
    redVal = getRed(x)
    sum += redVal
    
  return sum

def sumRedByIndex(picture, index1, index2):
  pixels = getPixels(picture)
  sum = 0
  for x in range(index1, index2+1, 1):
    redVal = getRed(pixels[x])
    sum += redVal
  return sum
    
def flipCase(string):
  pile = ''
  for x in string:
    if str.islower(x) == true:
      pile += str.upper(x)
    elif str.isupper(x) == true:
      pile += str.lower(x)
  print pile

def mirror2(string):
  pile = ''
  for x in range((len(string)-1), -1, -1):
    pile += (string[x]*2)
  for x in range(0, len(string), 1):
    pile += (string[x]*2)
  print pile 
  
def encode2(string, key):
  alpha1 = 'abcdefghijklmnopqrstuvwxyz'
  alpha2 = ''
  count = 0
  for letter in alpha1:
      if count == 5:
        alpha2 += key
        count += 1
      if letter not in key:
        alpha2 = alpha2 + letter
        count += 1
  
  secret = ''
  for letter in string:
    i = alpha1.find(letter)
    secret += alpha2[i]
  return secret
  
        
  
        
  
  
    
  