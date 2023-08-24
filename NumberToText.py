#converting number to text form, i.e. "20" to "Twenty"

d0to9 = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
d10to19 = {"1":"eleven", "2":"twelve", "3":"thirteen", "4":"fourteen", "5":"fifteen", "6":"sixteen", "7":"seventeen", "8":"eighteen", "9":"nineteen"}
d10s = { "1":"ten", "2":"twenty", "3":"thirty", "4":"fourty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty", "9":"ninety"}
noPlaces = {}

def last_digit(digits):
    #takes single digit, returns 0 to 9 value
    return d0to9[digits]

def tens_and_teens(digits):
    #takes two digits in array
    #determines if last two digits are between 11 and 19, returns value in teens or 10s value if not
    num = int(digits[0] + digits[1])
    if (10 < num < 20):
        return d10to19[str(digits[1])]
    elif (num%10 == 0):
        return d10s[digits[0]]
    else:
        return d10s[digits[0]] + " " + last_digit(digits[1])

def hundreds(digits):
    #takes 3 digits in array
    #gives value from hundreds place downwards
    num = int(digits[0] + digits[1] + digits[2])
    if(num%100 == 0):
        return d0to9[digits[0]] + " hundred"
    else:
        return d0to9[digits[0]] + " hundred and " + tens_and_teens(digits[1:len(digits)])

def thousands(digits):
    #takes 4 to 6 digits in array
    #gives value from thousands place downwards
    num_str = ""
    for digit in digits:
        num_str += digit
    num = int(num_str)
    thousands_str = ""
    if (num%1000 == 0):
        return

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

    """
    #print(number_array)
    
    if (number_int < 10):
        #print("in range 0 to 9")
        number_text = d0to9.get(number)
        print(number_text)

    elif (9 < number_int < 20):
        #print("in range 10 to 19")
        number_text = d10to19.get(number_array[1])

        print(number_text)

    elif(19 < number_int < 100):
        #print("in range 20 to 99")
        if (number_int % 10 == 0):
            number_text = d10s.get(number_array[0])
        else:
            number_text = d10s.get(number_array[0]) + " " + d0to9.get(number_array[1])

        print(number_text)

    elif(99 < number_int < 1000):
        #print("in range 100 to 999")
        if (number_int % 100 == 0):
            number_text = d0to9.get(number_array[0]) + " hundred"
        elif (number_int % 100 < 10):
            number_text = d0to9.get(number_array[0]) + " hundred and " + d0to9.get(number_array[2])
        elif (9 < number_int%100 < 20):
            number_text = d0to9.get(number_array[0]) + " hundred and " + d10to19.get(number_array[2])
        elif ((number_int%100)%10 == 0):
            number_text = d0to9.get(number_array[0]) + " hundred and " + d10s.get(number_array[1])
        else:
            number_text = d0to9.get(number_array[0]) + " hundred and " + d10s.get(number_array[1]) + " " + d0to9.get(number_array[2])

        print(number_text)
    elif (999 < number_int < 1000000):
        print("in progress")
        print("in range 1000 to 999,999")
        number_length = len(number_array)
        last_3 = [number_array[number_length-3],number_array[number_length-2],number_array[number_length-1]]
        print(last_3)
        thousands = []
        for i in range(0, number_length-3):
            thousands.append(number_array[i])
        print(thousands)


    else:
        print("out of range")
"""

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