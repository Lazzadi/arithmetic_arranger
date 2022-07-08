def arithmetic_arranger(problems,bool=False):
  
  import re
  operand1 = []  
  operand2 = []
  operator = []
  separator = []
  result = []
  maxString = []  #Will hold the lenght of longest operand for formatting purposes
  numberRegex = re.compile(r'\d{1,4}') # Regex used to find operands
  operatorRegex = re.compile(r'[+-/*]') # Regex used to find operators
  charactersRegex = re.compile(r'[^0-9+ -/*]') # Regex used to return errors in case of different characters
  largeNumberRegex = re.compile(r'\d{5,}')  # Regex used to return errors in case of operands bigger than 9999

# Returns error if there are more than 5 problems  
  if (len(problems)>5):
    return('Error: Too many problems.')
    quit()
    
# Returns an error if there are any other characters aside from 0-9+-*/ and spaces        
  for equation in problems:
    if(charactersRegex.findall(equation)):
      return('Error: Numbers must only contain digits.')
      quit()

# Returns a different error if there are / or * operators
  for equation in problems:
    if(operatorRegex.findall(equation) == ['/'] or operatorRegex.findall(equation) == ['*']):
      return("Error: Operator must be '+' or '-'.")
      quit()

# Returns error if numbers are five digits or larger
  for equation in problems:
    if(largeNumberRegex.findall(equation)):
      return('Error: Numbers cannot be more than four digits.')
      quit()

# Loop adds operators, opperands, signs and results to respective lists   
  for equation in problems:
    N=numberRegex.findall(equation)
    if(operatorRegex.findall(equation) == ['+']):
      sum = int(N[0]) + int(N[1])
      sign = '+'
      operator.append(sign)
    else:
      sum = int(N[0]) - int (N[1])
      sign = '-'
      operator.append(sign)
      
# Find which of the operators is the longest so we can properly create the separators and place the operand later  
    if(len(N[0])>=len(N[1])):         
      max = len(N[0])
      maxString.append(max)
    else:
      max = len(N[1])
      maxString.append(max)

# Asigning the values to the diferent lists 
    operand1.append(N[0])
    operand2.append(N[1])
    result.append(str(sum))

# Creating the separators  
    dash = ''
    for x in range(0,max+2):
      dash = dash + '-'
    separator.append(dash)

# Printing results
  arranged_problems = ''
  
  for i in range(0,len(operand1)):
    arranged_problems = arranged_problems + (' ' * (len(separator[i])-len(operand1[i])) + operand1[i] + 4*' ')
  arranged_problems = arranged_problems.rstrip(' ')
  arranged_problems = arranged_problems + '\n'
  
  for i in range(0,len(operand1)):
    arranged_problems = arranged_problems + operator[i] + ' '*(len(separator[i]) - len(operand2[i])-1) + operand2[i] + 4*' '
  arranged_problems = arranged_problems.rstrip(' ')
  arranged_problems = arranged_problems + '\n'
  
  for i in range(0,len(operand1)):
    arranged_problems = arranged_problems + separator[i] + ' '*4
  arranged_problems = arranged_problems.rstrip(' ')
  if(bool == True):
    arranged_problems = arranged_problems + '\n'
    for i in range(0,len(operand1)):
      arranged_problems = arranged_problems + ' '*(len(separator[i])-len(result[i])) + result[i] + 4 * ' '
      
  arranged_problems = arranged_problems.rstrip(' ')
  return(arranged_problems)