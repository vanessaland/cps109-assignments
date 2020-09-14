#-------------------------------------------------------------------------------------------------------
#Vanessa Landayan
#26 November 2018
#CPS109 - Assignment 2

#Declare global variables for the photos used for the template and the searchImage----------------------
tinywaldo = makePicture('/Users/vanessalandayan/Downloads/CPS109/Assignment2/tinywaldo.jpg')
tinyscene = makePicture('/Users/vanessalandayan/Downloads/CPS109/Assignment2/tinyscene.jpg')

#Declare global variables for the width and height of the template and searchImage----------------------
templateHeight = getHeight(tinywaldo)            
templateWidth = getWidth(tinywaldo)             
searchHeight = (getHeight(tinyscene) - templateHeight) + 1       
searchWidth = (getWidth(tinyscene) - templateWidth) + 1        

#This function returns an integer,which is the sum of the absolute value of the differences in luminance
def compareOne(template, searchImage, x1, y1): 
 sumOfDiff = 0 
 for x in range(templateWidth):   
  for y in range(templateHeight):
    pixel1 = getPixel(template, x, y)
    pixel2 = getPixel(searchImage, x1 + x , y1 + y)
    lum1 = getRed(pixel1)+getGreen(pixel1)+getBlue(pixel1)
    lum2 = getRed(pixel2)+getGreen(pixel2)+getBlue(pixel2)
    sumOfDiff = sumOfDiff + abs(lum1 - lum2)
 return sumOfDiff

#This function returns a 2D array called 'matrix',which contains the computed template match score for--
#all of the positions in the searchImage
def compareAll(template, searchImage): 
 matrix = [[i for i in range(searchWidth)] for j in range(searchHeight)]
 for y in range(searchHeight):    
  for x in range(searchWidth):     
   matrix[y][x] = compareOne(template, searchImage, x, y)   
 return matrix

#This function returns the coordinates of the position in 'matrix' where the value is minimum-----------
def find2Dmin(matrix):   
  min = matrix[0][0] 
  mincol = 0     
  minrow = 0 
  for x in range(searchWidth):   
   for y in range(searchHeight): 
    if min > matrix[y][x]:   
     min = matrix[y][x] 
     mincol = y
     minrow = x 
  return (minrow, mincol)

#This function puts a rectangle on the searchImage so that it would surround the target image with a----
#width of 3pixels
def displayMatch(searchImage, x1, y1, w1, h1, color):
  addRect(searchImage, x1, y1, w1, h1, color)
  addRect(searchImage, x1-1, y1-1, w1+2, h1+2, color)
  addRect(searchImage, x1-2, y1-2, w1+4, h1+4, color)

#This is a helper function that converts a color picture to grayscale-----------------------------------  
def grayscale(picture): 
  pixels = getPixels(picture)  
  for pixel in pixels:
   R = getRed(pixel)
   G = getGreen(pixel)
   B = getBlue(pixel)
   newColor = (R+G+B)/3  
   setColor(pixel, makeColor(newColor,newColor,newColor))
  return picture 

#This is the driver function that takes in the images and calls the other functions and shows the match-
def findWaldo(targetJPG, searchJPG): 
  template = grayscale(targetJPG)  
  searchImage = grayscale(searchJPG)
  x, y = find2Dmin(compareAll(template, searchImage))   
  displayMatch(searchImage, x, y, templateWidth, templateHeight, green)    
  show(searchImage) 