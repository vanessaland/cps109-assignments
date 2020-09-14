#3
def twoscomplement(binarystring):
  comp = ''
  for num in binarystring:
     if num == '0':
       comp += '1'
     if num == '1':
       comp += '0'
 
  num = ''
  for digit in comp:
    num = digit+num
    
  counter = 0
  twoscomp = ''
  
  for digit in num:
  
    if counter == 0 and digit == '0':
   
      digit = '1'     
      twoscomp = digit+twoscomp      
      counter += 1
      continue  
    if counter == 0 and digit == '1':
      digit = '0'
      twoscomp = digit+twoscomp
        
    if counter > 0:
      twoscomp = digit+twoscomp
    
  print twoscomp
    
#4
def intToBinaryString(n):
  string = ''
  
  while n != 0:
  
    string = (str(n%2))+string
    n = int(n/2)
    
  spaces = 16 - len(string)
  print '0'*spaces + string
  
#5
def doubleAmplitude(soundfile):
  sound = makeSound(soundfile)
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample,value * 2)
  play(sound)
  
#6
def doublehalf(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, value*2)
    if value < 0:
      setSampleValue(sample, value*0.5)
  explore(sound)

#Yes, you can still understand the words

def zeronegative(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value < 0:
      setSampleValue(sample, 0)
  explore(sound)

#Yes, you can still understand the words
#I think that this function removed made it so that the samples with less pressure than the background air pressure is now equal to the background air pressure.

#7
def minValue(sound):
  smallest = 0
  for sample in getSamples(sound):  
    value = getSampleValue(sample)
    if value < smallest:
      smallest = value
  print smallest
  
#8
def countZeros(sound):
  counter = 0
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value == 0:
      counter += 1
  return counter
  
#9
def clip(sound, maxvalue):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > maxvalue:
      setSampleValue(sample, maxvalue)
    if value < (maxvalue*-1):
      setSampleValue(sample, (maxvalue*-1))
  explore(sound)
#Yes, the sentence is still understandable

#10
def falseIncreaseVolume(sound, increment):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, (value+increment))
  explore(sound)
#The sound wave just moved up on the vertical axis. The sentence is still understandable.      