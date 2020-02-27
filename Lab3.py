def buildCipher(key) :
  alpha1 = 'abcdefghijklmnopqrstuvwxyz'          
  alpha2 = key
  for letter in alpha1 :
    if letter not in key : 
      alpha2 = alpha2 + letter
  return alpha2

def encode(string, alpha2) :
  alpha1 = 'abcdefghijklmnopqrstuvwxyz' 
  secret = ''
  for letter in string :
      i = alpha1.find(letter)
      secret = secret + alpha2[i] 
  return secret
  
def encode2(message, key): 
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