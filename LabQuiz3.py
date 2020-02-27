def hypotenuse(a, b) :
  side1 = a * a
  side2 = b * b
  c = sqrt(side1 + side2)
  return c

def encode2(message, key) : 
     alpha1 = 'abcdefghijklmnopqrstuvwxyz' 
     alpha2 = ''
  
     for letter in alpha1 :
          if letter not in key :
               alpha2 = alpha2 + letter
  
     alpha2 = alpha2 + key
     message = message.lower()
  
     secret = ''
     for letter in message :
          if letter not in alpha1 :
               continue
          i = alpha1.find(letter)
          secret = secret + alpha2[i]
     return secret
     
def decode(ciphertext, key):
    message = ''
    alpha1 = 'abcdefghijklmnopqrstuvwxyz' 
    alpha2 = ''
    
    for letter in alpha1 :
      if letter not in key :
        alpha2 = alpha2 + letter
    
    alpha2 = alpha2 + key           
    ciphertext = ciphertext.lower()
    
    
    for letter in ciphertext :
      i = alpha2.find(letter)
      message = message + alpha1[i]
    return message