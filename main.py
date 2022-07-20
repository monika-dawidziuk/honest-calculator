from sys import exit

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg = [msg_10, msg_11, msg_12]

memory = float(0)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        float_x = float(x)
        float_y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper in ["+", "-", "*", "/"]:
        check(float_x, float_y, oper)
    else:
        print(msg_2)
        continue

    if oper == "+":
        result = float_x + float_y
    elif oper == "-":
        result = float_x - float_y
    elif oper == "*":
        result = float_x * float_y
    elif oper == "/" and float_y != 0:
        result = float_x / float_y
    elif float_y == 0:
        print(msg_3)
        continue
    print(float(result))

    while True:
        print(msg_4)
        answer = input()
        if answer in ["y", "n"]:
            break

    if answer == "y":
        if is_one_digit(result):
            msg_index = 10
            while True:
                print(msg[msg_index - 10])
                answer_3 = input()
                if answer_3 == "y" and msg_index < 12:
                    msg_index = msg_index + 1
                    continue
                if answer_3 == "n":
                    break
                if answer_3 == "y" and msg_index >= 12:
                    memory = result
                    break
        else:
            memory = result

    while True:
        print(msg_5)
        answer_2 = input()
        if answer_2 == "y":
            break
        if answer_2 == "n":
            exit()
