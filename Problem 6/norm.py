"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Sean Killian
Lab Time: Thursday @ 2pm
"""

def norm():
    # Write your code here

    num_values = int(input())
    values = []
    
    for _ in range(num_values):
        value = float(input())
        values.append(value)
    
    max_value = max(values)
    
    normalized_values = [value / max_value for value in values]
    
    for value in normalized_values:
        print(f'{value:.2f}')

if __name__ == "__main__":
    norm()