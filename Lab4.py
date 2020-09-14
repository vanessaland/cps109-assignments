def colourZero(picture):
  for p in getPixels(picture):
    setRed(p, 0)
    setGreen(p, 0)
    setBlue(p, 0)

def colour255(picture):
  for p in getPixels(picture):
    setRed(p, 255)
    setGreen(p, 255)
    setBlue(p, 255)

def blueify(picture):
  for p in getPixels(picture):
    if getBlue(p) > 100:
      Blue = getBlue(p)
      setBlue(p, Blue*2)
      
def gen_blueify(picture):
  for p in getPixels(picture):
    Blue = getBlue(p)
    Red = getRed(p)
    Green = getGreen(p)
    
    setBlue(p, Blue*2)
    setRed(p, Red/2)
    setGreen(p, Green/2) 
    
def negate(picture):
  for p in getPixels(picture):
    Red = getRed(p)*0.3
    Blue = getBlue(p)*0.1
    Green = getGreen(p)*0.6
    luminance = (Red + Blue + Green)
    setColor(p, makeColor(255-luminance, 255-luminance, 255-luminance))
    
def negative(picture):
  for p in getPixels(picture):
    Red = getRed(p)  
    Green = getGreen(p)
    Blue = getBlue(p)
    negColor = makeColor(255-Red, 255-Green, 255-Blue)
    setColor(p, negColor)

def grayScale(picture):
  for p in getPixels(picture):
    Red = getRed(p)*0.3
    Green = getGreen(p)*0.6
    Blue = getBlue(p)*0.1
    luminance = Red + Green + Blue
    setColor(p, makeColor(luminance, luminance, luminance))
    
def grayScaleNegative(picture):
  grayScale(picture)
  negative(picture)
  
def lightGrayScale(picture):
  for p in getPixels(picture):
    Red = getRed(p) + 75
    Green = getGreen(p) + 75
    Blue = getBlue(p) + 75
    luminance = Red*0.3 + Green*0.6 + Blue*0.1
    setColor(p, makeColor(luminance, luminance, luminance))
        
def lighterGrayScale(picture):
  for p in getPixels(picture):
    color = makeLighter(getColor(p))
    Red = getRed(p)*0.3
    Green = getGreen(p)*0.6
    Blue = getBlue(p)*0.1
    luminance = Red + Green + Blue
    setColor(p, makeColor(luminance, luminance, luminance))
    
def test6(picture):
  for pixel in getPixels(picture) :
    red = getRed(pixel)
    green = getGreen(pixel)
    blue = getBlue(pixel)
    color = makeColor(red, green, blue) 
    setColor(pixel, color)

    