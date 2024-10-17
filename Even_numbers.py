def sum_of_even_numbers ():
    
    user_input = input ("Please enter a list of numbers separated by spaces: ")


    numbers = list (map(int, user_input.split()))


    even_sum = 0


    for num in numbers:
    
        if num %2 == 0:
            
            even_sum += num
            
            
    print (f"The sum of even numbers in the list is: {even_sum}")

sum_of_even_numbers()