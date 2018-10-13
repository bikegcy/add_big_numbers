import re


def get_str_number(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.readlines()
            if len(contents) > 1:
                raise ValueError('There are more than one number in the file.')
            else:
                if re.match('^[0-9]+$', contents[0]):
                    return contents[0]
                else:
                    raise ValueError('The number in the file is not valid.')
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        raise FileNotFoundError(msg)


def add_big_number(num1, num2):
    # Make num2 is the longer one
    if len(num1) > len(num2):
        temp = num1
        num1 = num2
        num2 = temp
    res = ''
    n1 = len(num1)
    n2 = len(num2)
    diff = n2 - n1
    carry = 0

    for i in range(n1 - 1, -1, -1):
        sum = int(ord(num1[i]) - ord('0')) + int(ord(num2[i+diff]) - ord('0')) + carry
        res += str(sum % 10)
        carry = sum // 10

    for i in range(n2 - n1 - 1, -1, -1):
        sum = int(ord(num2[i]) - ord('0')) + carry
        res += str(sum % 10)
        carry = sum // 10

    if carry:
        res += str(carry)
    res = res[::-1]
    return res


if __name__ == "__main__":
    filename1 = 'number1.txt'
    filename2 = 'number2.txt'
    filename3 = 'wrongNumber.txt'

    num1 = get_str_number(filename1)
    num2 = get_str_number(filename2)
    # num3 = getStrNumber(filename3)

    print(add_big_number('12321', '91111'))
    print(add_big_number('111', '999'))
    print(add_big_number('11111111111111111', '12345678987654321'))
    print(add_big_number(get_str_number(filename1), get_str_number(filename2)))

