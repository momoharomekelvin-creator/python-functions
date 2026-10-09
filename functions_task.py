def is_even(numbers):
    if number % 2 == 0:

        return true
    else:
         return false


         print(is_even(7))
         print(is_even(8))








def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return false
        else:
            return true



            print(is_prime(6))








def subtract(first,second):
    return abs(first - second)

print(subtract(5,20))












def divide(first,second):
    if second == 0:
        return 0
    else:
        return first / second

print(divide(20,5))











def factor_of_number(number):

    count = 0
    for i in range(1,number + 1):
        if number % i == 0:
         count = count + 1
    return count

print(factor_of_number(9))











def is_square(number):
    return number*number

print(is_square(9))












def is_palindrome(number):

    first = number // 10000
    second = (number // 1000) % 10
    fourth = (number // 10) % 10
    fifth = number % 10

    if first == fifth and second == fourth:
        return True
    else:
        return False

result = is_palindrome(54145)
print(result)
    










def factorial_of(number):
    result = 1 
    for i in range (number,0,-1):
        result = result*i
    return result 
answer = factorial_of(10)
print(answer)







