#FACE_EDIT
#This is a fun face changer for the picture of Jenny.
def faceEdit():
  pic = makePicture('/Users/vanessalandayan/Downloads/CPS109/mediasources-4ed/jenny2-green-small.jpg') 
  changeEyeColor(pic, 218, 129, 228, 137, black)
  mirrorVertical(pic, 247)
  hair(pic)
  lips(pic)
  powder(pic)
  show(pic)
#Function 6
#This function makes Jenny's face symmetrical by mirroring the photo at the centre of her face.
def mirrorVertical(pic, mirrorPoint):
  width = getWidth(pic)
  for y in range(0,getHeight(pic)):
    for x in range(0, mirrorPoint):
      leftPixel = getPixel(pic,x,y)
      rightPixel = getPixel(pic,width - x - 1,y)
      color = getColor(leftPixel)
      setColor(rightPixel,color)

#Function 7
#This function changes Jenny's eye color to any color.
def changeEyeColor(pic,sX,sY,eX,eY,endColor):
  for x in range(sX,eX):
    for y in range(sY,eY):
      px = getPixel(pic,x,y)
      setColor(px,endColor)

#Function 8
#This function changes Jenny's hair to pink, as if she dyed it.
def hair(pic):
  pixels = getPixels(pic)
  for pixel in pixels:
    Red = getRed(pixel)
    Green = getGreen(pixel)
    Blue = getBlue(pixel)
    Y = getY(pixel)
    if 100 < Red < 200 and Y < 240:
      setRed(pixel, Red*1.5)
      setGreen(pixel, Green*0.60)
      setBlue(pixel, Blue*1.1)

#Function 9
#This function changes the color of Jenny's lips for lipstick.
def lips(pic):
  pixels = getPixels(pic)
  for pixel in pixels:
    Red = getRed(pixel)
    G = getGreen(pixel)
    Y = getY(pixel)
    X = getX(pixel)
    if Red > 200 and 188 < Y < 214 and 221 < X < 276 and G < 160:
      setRed(pixel, Red*3)
      setGreen(pixel, G*0.5)

#Function 10
#This function brightens the high points of Jenny's face for powder.
def powder(pic):
  pixels = getPixels(pic)
  for pixel in pixels:
    Red = getRed(pixel)
    G = getGreen(pixel)
    B = getBlue(pixel)
    Y = getY(pixel)
    X = getX(pixel)
    if Red > 200 and 119 < Y < 240 and 190 < X < 305 and 190< G < 210:
      setRed(pixel, Red*1.1)
      setGreen(pixel, G*1.1)
      setBlue(pixel, B*1.1)
     
      
      