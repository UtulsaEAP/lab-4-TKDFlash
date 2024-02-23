"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Sean Killian
Lab Time: Thursday @ 2pm
"""

def inc_5():
    value_1 = int(input())
    value_2 = int(input())
    # Write your code here
    
    if value_2 < value_1:
        print("Second integer can't be less than the first.")
    else:
        current_value = value_1
        while current_value <= value_2:
            print(current_value, end=" ")
            current_value += 5
        print()


if __name__ == '__main__':
    inc_5()