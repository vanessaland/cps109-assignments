def addition(a, b) :
  c = a + b
  return c

def pickAndShow() :
  f = pickAFile()
  p = makePicture(f)
  show(p)  
 
def pickAndPlay() :
  file = pickAFile()
  sound = makeSound(file)
  play(sound)
  
def pickAndPlayLoop(n) :
  file = pickAFile()
  sound = makeSound(file)
  for i in range(n) :
    play(sound)
  return file

def showNamed(file) :
  pic = makePicture(file)
  show(pic)
  
def playNamed(file) :
  sound = makeSound(file)
  play(sound)

def playAndshow(soundfile, picfile) :
  sound = makeSound(soundfile)
  pic = makePicture(picfile)
  show(pic)
  play(sound)
  
def concat(s1, s2, s3) :
  mid = ' silly '
  return s1 + mid + s2 + mid + s3