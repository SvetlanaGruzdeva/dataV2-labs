"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

actions_list = ['plus', 'munis']
values_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
result_dict = {-5:'negative five', -4:'negative four', -3:'negative three', -2:'negative two', -1:'negative one', 0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}

if any(val not in values_dict.keys() for val in (a, c)) or b not in actions_list:
    print("I am not able to answer this question. Check your input.")
else:
    if b == 'plus':
        d = values_dict[a] + values_dict[c]
    else:
        d = values_dict[a] - values_dict[c]
print(f"{a} {b} {c} equals {result_dict[d]}")
    
print("Thanks for using this calculator, goodbye :)")
