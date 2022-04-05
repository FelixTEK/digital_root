#FELIXTEK 2022
droot = 0 #digital root variable
num = 0 #number that you want to find a digital root of variable
orignum = 0 #originally inputted number that you specified in the variable num
digits = [] #all digits of your number
persistence = 1 #additive persistence of your digital root finding method

def digitalrootcalc():
  global droot #digital root variable
  global num
  global orignum
  global digits
  global persistence #additive persistence
  if num == 0:
    num = int(input("Please insert your integer.\n> ")) #desired integer
    orignum = num
    digits = list(int(d) for d in str(num)) #all digits of the specified integer above, kept in a list
  elif num >= 10:
    num = droot
    droot = 0
    digits = list(int(d) for d in str(num)) #all digits of the specified integer above, kept in a list
  for i in range(0, len(digits)): #calculation of digital root
        droot = droot + digits[i];
    
def drootchecker():
  digitalrootcalc()
  global persistence
  if droot >= 10:
    persistence = persistence + 1
    drootchecker()
  elif droot <10:
    print("{0} has additive persistence {1} and digital root of {2};" .format(orignum,persistence,droot))

if __name__ == "__main__": #main function
  drootchecker()
