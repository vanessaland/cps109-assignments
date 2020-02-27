#COOL_TEMPLE
#This function calls various functions to make the temple look cool.
def coolTemple():
  temple = makePicture('/Users/vanessalandayan/Downloads/CPS109/mediasources-4ed/temple.jpg')
  mirrorDouble(temple)
  pinkBackground(temple)
  negativeHalf(temple)
  middleGrayTop(temple)
  middleBlackBottom(temple)
  show(temple)

#Function 11
#This function mirrors the picture horizontally and the bottom half vertically  
def mirrorDouble(picture):
 pixels = getPixels(picture)
 target = len(pixels) - 300
 for index in range(0,len(pixels)/2):
   pixel1 = pixels[index]
   color1 = getColor(pixel1)
   pixel2 = pixels[target]
   setColor(pixel2,color1)
   target = target - 1

#Function 12
#This function makes the sky pink by changing the RGB values.
def pinkBackground(picture) :
  for pixel in getPixels(picture) :
    red = getRed(pixel)
    green = getGreen(pixel)
    blue = getBlue(pixel)
    if 195 < blue < 215:
      color = makeColor(red*2, green*0.5, blue*0.75)
      setColor(pixel, color)

#Function 13
#This function makes the top half of the photo in negative.      
def negativeHalf(picture):
  pixels = getPixels(picture)
  for px in range (0, len(pixels)/2):
    i = pixels[px]
    red=getRed(i)
    green=getGreen(i)
    blue=getBlue(i)
    negColor=makeColor(255-red, 255-green, 255-blue)
    setColor(i,negColor)

#Function 14
#This function makes the middle of the top half of the photo into a grayscale.    
def middleGrayTop(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  for p in getPixels(picture):
    x = getX(p)
    y = getY(p)
    if (width/4) < x < ((width/4)*3):
      if 0 < y < (height/2):
        intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
        setColor(p,makeColor(intensity,intensity,intensity))

#Function 15
#This function makes the middle of the bottom half of the photo into black and white      
def middleBlackBottom(picture):
  pixels = getPixels(picture)
  width = getWidth(picture)
  height = getHeight(picture)
  for p in pixels:
    x = getX(p)
    y = getY(p)
    if (width/4) < x < ((width/4)*3):
      if (height/2) < y < (height-1):
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        luminance = (r+g+b)/3
        if luminance < 64:
          setColor(p,black)
        if luminance >= 64:
          setColor(p,white)
    



    
