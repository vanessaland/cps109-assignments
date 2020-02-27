def p19_duplicateString(s) :
    # notice the accumulator called 'pile'
    pile = ' '
    for letter in s :
       pile = pile + letter
    return pile
    
def p20_reverse(s) :
    #accumulating the letters at the front
    pile = ""
    for letter in s :
       pile = letter + pile
    return pile + s
    
def mirrorhalf(s) :
  pile = ""
  for i in range(len(s) / 2) :
    pile = pile + s[i]
  for i in range(len(s) /2, -1, -1, -1) :
    pile = pile + s[i]
  return pile

