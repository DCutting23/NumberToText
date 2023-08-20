#converting number to text form, i.e. "20" to "Twenty"

d0to9 = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
d10to19 = {"10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", "15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen", "19":"nineteen"}
d10s = {"2":"twenty", "3":"thirty", "4":"fourty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty", "9":"ninety"}

if __name__ == "__main__":
    print ("program start")
    while (True):
        number = input("number to convert: ")
        if (number.isdigit()):
            print ("is digit")
            break
        else:
            print("please enter an integer")
    print (number)
    number_array = []
    for char in number:
        number_array.append(char)
    number_int = int(number)

    print(number_array)
    
    if (number_int < 10):
        print("in range 0 to 9")
        number_text = d0to9.get(number)
        print(number_text)

    elif (9 < number_int < 20):
        print("in range 10 to 19")
        number_text = d10to19.get(number)
        print(number_text)

    elif(19 < number_int < 100):
        print("in range 20 to 99")
        if (number_int % 10 == 0):
            number_text = d10s.get(number_array[0])
        else:
            number_text = d10s.get(number_array[0]) + " " + d0to9.get(number_array[1])
        print(number_text)

    elif(99 < number_int < 1000):
        print("in range 100 to 999")
        if (number_int % 100 == 0):
            number_text = d0to9.get(number_array[0]) + " hundred"
        elif (number_int % 100 <)


    else:
        print("out of range")