def into_hex(number):

    hexi_decimal_mapping = {
        "0":"0",
        "1":"1",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9",
        "10":"A",
        "11":"B",
        "12":"C",
        "13":"D",
        "14":"E",
        "15":"F"
    }

    if(number > 16):

        array_result = []

        while(number > 16):

            result = number / 16

            remaining = number % 16

            if(result < 16):

                array_result.append(remaining)

                array_result.append(result)

            else:

                array_result.append(remaining)

            number = result
        
        i = len(array_result)-1

        final_result = ""

        while i >= 0:

            final_result += hexi_decimal_mapping[str(array_result[i])]

            i -= 1

        return final_result
    else:

        result = hexi_decimal_mapping[str(number)]

        return result
   
    
print(into_hex(4445))