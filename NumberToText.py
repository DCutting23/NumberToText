#converting number to text form, i.e. "20" to "Twenty"

d0to9 = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
d10to19 = {"0":"ten", "1":"eleven", "2":"twelve", "3":"thirteen", "4":"fourteen", "5":"fifteen", "6":"sixteen", "7":"seventeen", "8":"eighteen", "9":"nineteen"}
d10s = {"2":"twenty", "3":"thirty", "4":"fourty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty", "9":"ninety"}

if __name__ == "__main__":
    print ("program start")
    while (True):
        number = input("number to convert: ")
        if (number.isdigit()):
            print ("is digit")
            break
        else:
            print("please enter a positive integer")
    #print (number)
    number_array = []
    for char in number:
        number_array.append(char)
    number_int = int(number)

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