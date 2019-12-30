while True:
    try:
        age = int(input('What is your age? '))
        12 / age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter number higher than 0')
    else:
        print('thank you')
        break


def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum(1, '2'))
