#converting number to text form, i.e. "20" to "Twenty"

d0to9 = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
d10to19 = {"1":"eleven", "2":"twelve", "3":"thirteen", "4":"fourteen", "5":"fifteen", "6":"sixteen", "7":"seventeen", "8":"eighteen", "9":"nineteen"}
d10s = { "1":"ten", "2":"twenty", "3":"thirty", "4":"fourty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty", "9":"ninety"}

def numint(digits): #int from list of digits
    num_str = ""
    for digit in digits:
        num_str += digit
    return int(num_str)

def slz(digits): #strips leading 0s
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
    #takes two digits in a list
    #determines if last two digits are between 11 and 19, returns value in teens or 10s value if not
    num = numint(digits)

    if (num < 10):
        return last_digit(slz(digits))
    else:
        if (10 < num < 20):
            return d10to19[str(digits[1])]
        elif (num%10 == 0):
            return d10s[digits[0]]
        else:
            return d10s[digits[0]] + " " + last_digit(digits[1])

def hundreds(digits):
    #takes 3 digits in a list
    #gives value from hundreds place downwards
    num = numint(digits)

    if (num < 100):
        return tens_and_teens(slz(digits))
    else:
        if(num%100 == 0):
            return d0to9[digits[0]] + " hundred"
        else:
            return d0to9[digits[0]] + " hundred and " + tens_and_teens(digits[1:len(digits)])

def thousands(digits):
    #takes 4 to 6 digits in a list
    #gives value from thousands place downwards
    num = numint(digits)

    if (num < 1000):
        return hundreds(slz(digits))
    else:
        thousands_digits = []
        thousands_str = ""
        for i in range(len(digits)-3):
            thousands_digits.append(digits[i])
        thousands_num = numint(thousands_digits)
        
        hundreds_digits = []
        hundreds_str = ""
        for i in range(len(digits)-3, len(digits)):
            hundreds_digits.append(digits[i])
        hundreds_num = numint(hundreds_digits)

        if (hundreds_num == 0):
            return hundreds(thousands_digits) + " thousand"
        else:
            return hundreds(thousands_digits) + " thousand " + hundreds(hundreds_digits)

def millions(digits):
    #takes 7 to 10 digits in a list
    #gives value from millions place downwards
    num = numint(digits)
    if (num < 1000000):
        return thousands(slz(digits))
    else:
        millions_digits = []
        for i in range(len(digits)-6):
            millions_digits.append(digits[i])
        millions_num = numint(millions_digits[i])

        thousands_digits = []
        for i in range(len(digits)-6, len(digits)):
            thousands_digits.append(digits[i])
        thousands_num = numint(thousands_digits)

        if (thousands_num == 0):
            return thousands(millions_digits) + " million"
        else:
            return thousands(millions_digits) + " million " + thousands(thousands_digits)

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

    number_array = slz(number_array)

    if (len(number_array) < 10): #checks for number in 0 to 9 range
        print(millions(number_array))
    else:
        print("number to high")