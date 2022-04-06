#FELIXTEK 2022
droot = 0 #digital root variable
num = 0 #number that you want to find a digital root of variable
orignum = 0 #originally inputted number that you specified in the variable num
digits = [] #all digits of your number
persistence = 1 #additive persistence of your digital root finding method
numtyp = "" #type of number e.g. binary, octal, decimal(int), and hexadecimal
maxdigitalrootvalue = 9 #digital roots never exceed 9.   
runagainvar = True #variable which asks if the user wants to re-execute the program

def datatypsel(): #data type selection
  global num
  global orignum
  global numtyp
  global digits
  num = input("Please insert your number.\n> ") #desired value
  orignum = num
  num = num.lower()
  digits = list(num)
  if ("x" in digits) or ("a" in digits or "b" in digits or "c" in digits or "d" in digits or "e" in digits or "f" in digits):
    print("Your value is a hexadecimal value.")
    if ("x" not in digits):
      num = num + "x"
    num = int(num, 16)
    numtyp = "hex"

  elif ("o" in digits) and ("8" not in digits and "9" not in digits):
    print("Your value is an octal value.")
    num = int(num, 8)
    numtyp = "oct"

  elif ("b" in digits) and ("8" not in digits and "9" not in digits and "7" not in digits and "6" not in digits and "5" not in digits and "4" not in digits and "3" not in digits and "2" not in digits):
    print("Your value is a binary value.")
    num = int(num, 2)
    numtyp = "bin"  
  
  elif ("8" not in digits and "9" not in digits) and ("7" in digits or "6" in digits or "5" in digits or "4" in digits or "3" in digits or "2" in digits):
    numtyp = input("Is this a hexadecimal number, an octal number, or a decimal number? [HEX/DEC/OCT]\n> ").lower()
    if numtyp == "hex":
        num = ("0x"+num)
        num = int(num, 16)
        print("Your value is a hexadecimal value.")
    elif numtyp == "oct":
        num = ("0o"+num)
        num = int(num, 8)
        print("Your value is an octal value.")
    elif numtyp == "dec":
        num = int(num)
        print("Your value is a decimal value.")
  
  elif "8" not in digits and "9" not in digits and "7" not in digits and "6" not in digits and "5" not in digits and "4" not in digits and "3" not in digits and "2" not in digits:
    numtyp = input("Is this a hexadecimal number, an octal number, a decimal number, or a binary number? (int)? [HEX/DEC/OCT/BIN]\n> ").lower()
    if numtyp == "hex":
        num = ("0x"+num)
        num = int(num, 16)
        print("Your value is a hexadecimal value.")
    elif numtyp == "oct":
        num = ("0o"+num)
        num = int(num, 8)
        print("Your value is an octal value.")
    elif numtyp == "dec":
        num = int(num)
        print("Your value is a decimal value.")
    elif numtyp == "bin":
        num = ("0b"+num)
        num = int(num, 2)
        print("Your value is a binary value.")
  else:
    numtyp = input("Is this a hexadecimal number, or a decimal number (normal int)? [HEX/DEC]\n> ").lower()
    if numtyp == "hex":
        num = ("0x"+num)
        num = int(num, 16)
        print("Your value is a hexadecimal value.")
    elif numtyp == "dec":
        num = int(num)
        print("Your value is a decimal value.")

def digitalrootcalc(): #calculation of digital root
  global droot
  global num
  global orignum
  global digits
  global persistence
  global maxdigitalrootvalue
  if droot > maxdigitalrootvalue:
      num = droot
      droot = 0
  digits = list(int(d) for d in str(num)) #the converted value that was converted to int will be re-digited to make calculation easier.
  for i in range(0, len(digits)): #calculation of digital root
        droot = droot + digits[i];
    
def drootchecker():
  digitalrootcalc()
  global persistence
  global droot
  global orignum
  if droot >= 10:
    persistence = persistence + 1
    drootchecker()
  elif droot <10:
    print("{0} has additive persistence {1} and digital root of {2};\n" .format(orignum,persistence,droot))

def runagain():
  global runagainvar
  asktorun = input("Do you want to run again? (Y/N)\n> ").upper()
  if asktorun == "Y":
    runagainvar = True
    print("\n")
  elif asktorun == "N":
    runagainvar = False
  else:
    print("Invalid response.\n")
    runagain()
    

if __name__ == "__main__": #main function
  while True:
    datatypsel()
    drootchecker()
    runagain()
    if runagainvar is False:
      break
