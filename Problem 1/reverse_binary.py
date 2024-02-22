"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Sean Killian
Lab Time: Thursday @ 2pm

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE

    binary = ""

    while user_num > 0:
        remainder = user_num % 2
        binary += str(remainder)
        user_num //= 2

    print(binary)

if __name__ == "__main__":
    reverse_binary()