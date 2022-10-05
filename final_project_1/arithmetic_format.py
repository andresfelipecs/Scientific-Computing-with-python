import re


def order(list_int, op_list, list_str, a):

    # dividing between top numbers and bottom numbers
    top_numbers = []
    bot_numbers = []
    for i, value in enumerate(list_int, 2):
        if i % 2 == 0:
            top_numbers.append(value)
        elif i % 2 != 0:
            bot_numbers.append(value)

    # transform from nested lists and from str to punctuation
    # first: converting list objects to str objects, nested list
    list2_str = []
    for x in op_list:
        for i in x:
            list2_str.append(i)

    top_numbers_str = []
    bot_numbers_str = []

    for i in top_numbers:
        top_numbers_str.append(str(i))
    for i in bot_numbers:
        bot_numbers_str.append(str(i))

    for i, j in zip(top_numbers_str, bot_numbers_str):
        if len(i) > len(j):
            if len(i) == 2:
                print(f'{i:>4}', end='    ')
            elif len(i) == 3:
                print(f'{i:>5}', end='    ')
            elif len(i) == 4:
                print(f'{i:>6}', end='    ')
        elif len(j) > len(i):
            if len(j) == 2:
                print(f'{i:>4}', end='    ')
            elif len(j) == 3:
                print(f'{i:>5}', end='    ')
            elif len(j) == 4:
                print(f'{i:>6}', end='    ')
        elif len(j) == len(i):
            if len(i) == 1:
                print(f'{i:>3}', end='    ')
            elif len(i) == 2:
                print(f'{i:>4}', end='    ')
            elif len(i) == 3:
                print(f'{i:>5}', end='    ')
            elif len(i) == 4:
                print(f'{i:>6}', end='    ')

    print('\n', end='')

    for i, j, o in zip(top_numbers_str, bot_numbers_str, op_list):
        for z in o:
            if len(i) > len(j):
                if len(i) == 2:
                    print(f'{z:<1}', end='')
                    print(f'{j:>3}', end='    ')
                elif len(i) == 3:
                    print(f'{z:<1}', end='')
                    print(f'{j:>4}', end='    ')
                elif len(i) == 4:
                    print(f'{z:<1}', end='')
                    print(f'{j:>5}', end='    ')
            elif len(j) > len(i):
                if len(j) == 2:
                    print(f'{z:<1}', end='')
                    print(f'{j:>3}', end='    ')
                elif len(j) == 3:
                    print(f'{z:<1}', end='')
                    print(f'{j:>4}', end='    ')
                elif len(j) == 4:
                    print(f'{z:<1}', end='')
                    print(f'{j:>5}', end='    ')
            elif len(j) == len(i):
                if len(j) == 1:
                    print(f'{z:<1}', end='')
                    print(f'{j:>2}', end='    ')
                elif len(j) == 2:
                    print(f'{z:<1}', end='')
                    print(f'{j:>3}', end='    ')
                elif len(j) == 3:
                    print(f'{z:<1}', end='')
                    print(f'{j:>4}', end='    ')
                elif len(j) == 4:
                    print(f'{z:<1}', end='')
                    print(f'{j:>5}', end='    ')
    print('\n', end='')

    for i, j, o in zip(top_numbers_str, bot_numbers_str, op_list):
        for z in o:
            x = '-'
            if len(i) > len(j):
                if len(i) == 2:
                    print(f'{x*4}', end='    ')
                elif len(i) == 3:
                    print(f'{x*5}', end='    ')
                elif len(i) == 4:
                    print(f'{x*6}', end='    ')
            elif len(j) > len(i):
                if len(j) == 2:
                    print(f'{x*4}', end='    ')
                elif len(j) == 3:
                    print(f'{x*5}', end='    ')
                elif len(j) == 4:
                    print(f'{x*6}', end='    ')
            elif len(j) == len(i):
                if len(j) == 1:
                    print(f'{x*3}', end='    ')
                elif len(j) == 2:
                    print(f'{x*4}', end='    ')
                elif len(j) == 3:
                    print(f'{x*5}', end='    ')
                elif len(j) == 4:
                    print(f'{x*6}', end='    ')
    print('', end='\n')
  
    if a == True:
      for i, j, o in zip(top_numbers_str, bot_numbers_str, op_list):
          for z in o:
              if len(i) > len(j):
                  if len(i) == 2:
                      if z == '+':
                          print(f'{int(i)+int(j):>4}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>4}', end='    ')
                  elif len(i) == 3:
                      if z == '+':
                          print(f'{int(i)+int(j):>5}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>5}', end='    ')
                  elif len(i) == 4:
                      if z == '+':
                          print(f'{int(i)+int(j):>6}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>6}', end='    ')
              if len(j) > len(i):
                  if len(j) == 2:
                      if z == '+':
                          print(f'{int(i)+int(j):>4}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>4}', end='    ')
                  elif len(j) == 3:
                      if z == '+':
                          print(f'{int(i)+int(j):>5}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>5}', end='    ')
                  elif len(j) == 4:
                      if z == '+':
                          print(f'{int(i)+int(j):>6}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>6}', end='    ')
              elif len(j) == len(i):
                  if len(j) == 1:
                      if z == '+':
                          print(f'{int(i)+int(j):>3}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>3}', end='    ')
                  if len(j) == 2:
                      if z == '+':
                          print(f'{int(i)+int(j):>4}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>4}', end='    ')
                  elif len(j) == 3:
                      if z == '+':
                          print(f'{int(i)+int(j):>5}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>5}', end='    ')
                  elif len(j) == 4:
                      if z == '+':
                          print(f'{int(i)+int(j):>6}', end='    ')
                      elif z == '-':
                          print(f'{int(i)-int(j):>6}', end='    ')

def arithmetic_arranger(list, a):

    number_list = []
    op_list = []
    # using regex to separate numbers from operations
    for i in list:
        # regex patterns
        pattern = '\d{1,4}'
        pattern_operation = '\-|\+'
        # regex methods
        numbers = re.findall(pattern, i)
        operation = re.findall(pattern_operation, i)

        number_list.append(numbers)
        op_list.append(operation)

    # converting list objects to str objects, nested list
    list_str = []
    for x in number_list:
        #print(x)
        for i in x:
            list_str.append(i)
    # converting strings to int
    list_int = [int(string) for string in list_str]

    order(list_int, op_list, list_str, a)


if __name__ == "__main__":

    a = True
    #list = ['2 + 1', '222 + 222', '3333 + 3323', '4444 - 4442', '22 + 22']

    list = input('\n Enter problem separated by comma (exp : 1+1,2-2,3+3...): \n\n').split(',')
    #list = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "125 - 4589"]

    try:
        length = 5
    except:
        lenght = 6
    try:
        for i in list:
            operation = re.findall('\-|\+', i)
    except:
        for i in list:
            operation = re.findall('\*|\/', i)
    try:
        for i in list:
            length_numbers = re.findall('\d{1,4}', i)
    except:
        for i in list:
            length_numbers = re.findall('\d{1,6}', i)

    for i in list:
        numbers = re.findall('\d{1,10}', i)

    for i in list:
        letters = re.findall('[a-z]', i)

    
    if len(numbers[0]) <= 4 and len(numbers[1]) <= 4:
      x = 1
    else:
      x = 0
      
    if len(list) <= length:
        if '+' in operation or '-' in operation:
            if not letters:
              if x == 1:
                print('-'*35)
                arithmetic_arranger(list, a)
                print('\n','-'*35)
              else:
                print('Error: Numbers cannot be more than four digits.')
            else:
                print('Error: Numbers must only contain digits.')
        else:
            print('Error: Operator must be "+" or "-".')
    else:
        print('Error: Too many problems.')
