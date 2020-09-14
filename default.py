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
