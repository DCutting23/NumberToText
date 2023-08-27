#converting number to text form, i.e. "20" to "Twenty"

d0to9 = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
d10to19 = {"1":"eleven", "2":"twelve", "3":"thirteen", "4":"fourteen", "5":"fifteen", "6":"sixteen", "7":"seventeen", "8":"eighteen", "9":"nineteen"}
d10s = { "1":"ten", "2":"twenty", "3":"thirty", "4":"fourty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty", "9":"ninety"}
noPlaces = {}

def slz(digits):
    i = 0
    while(i < len(digits)):
        if (digits[i] == "0"):
            digits.pop(i)
            i-=1
        else:
            break
        i += 1
    return digits
def last_digit(digits):
    #takes single digit, returns 0 to 9 value
    return d0to9[digits[0]]

def tens_and_teens(digits):
    #takes two digits in array
    #determines if last two digits are between 11 and 19, returns value in teens or 10s value if not
    num_str = ""
    for digit in digits:
        num_str += digit
    num = int(num_str)
    if (num < 10):
        print("passing down")
        return last_digit(slz(digits))
    else:
        if (10 < num < 20):
            return d10to19[str(digits[1])]
        elif (num%10 == 0):
            return d10s[digits[0]]
        else:
            return d10s[digits[0]] + " " + last_digit(digits[1])

def hundreds(digits):
    #takes 3 digits in array
    #gives value from hundreds place downwards
    num_str = ""
    for digit in digits:
        num_str += digit
    num = int(num_str)
    if (num < 100):
        print("passing down")
        return tens_and_teens(slz(digits))
    else:
        if(num%100 == 0):
            return d0to9[digits[0]] + " hundred"
        else:
            return d0to9[digits[0]] + " hundred and " + tens_and_teens(digits[1:len(digits)])

def thousands(digits):
    #takes 4 to 6 digits in array
    #gives value from thousands place downwards
    thousands_digits = []
    thousands_str = ""
    for i in range(len(digits)-3):
        thousands_digits.append(digits[i])
    for digit in thousands_digits:
        thousands_str += digit
    thousands_num = int(thousands_str)
    
    hundreds_digits = []
    hundreds_str = ""
    for i in range(len(digits)-3, len(digits)):
        hundreds_digits.append(digits[i])
    for digit in hundreds_digits:
        hundreds_str += digit
    hundreds_num = int(hundreds_str)

    if (hundreds_num == 0):
        return hundreds(thousands_digits) + " thousand"
    else:
        return hundreds(thousands_digits) + " thousand " + hundreds(hundreds_digits)

    

"""
def millions():
    #gives value from millions place downwards
"""

if __name__ == "__main__":
    print ("program start")

    #takes and validates user input as int
    while (True):
        number = input("number to convert: ")
        if (number.isdigit()):
            break
        else:
            print("please enter a positive integer")

    #creates array from user input
    number_array = []
    for char in number:
        number_array.append(char)

    #removes leading 0s
    i = 0
    while(i < len(number_array)):
        if (number_array[i] == "0"):
            number_array.pop(i)
            i-=1
        else:
            break
        i += 1

    if (len(number_array) < 2): #checks for number in 0 to 9 range
        print(last_digit(number_array[0]))
    elif(len(number_array) < 3): #checks for number in 10 to 99 range
        print(tens_and_teens(number_array))
    elif(len(number_array) < 4): #checks for number in 100 to 999 range
        print(hundreds(number_array))
    elif(len(number_array) < 7): #checks for number in 1000 to 999 999 range
        print(thousands(number_array))
    else:
        print("hit else")