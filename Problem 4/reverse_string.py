"""
Complete the following python code to reverse the string entered by the user.

Name: Sean Killian
Lab Time: Thursday @ 2pm
"""

def reverse_string():
    # YOUR CODE HERE
    
    texts = []
    
    while True:
        text = input()
        if text.lower() in ["done", "d"]:
            break
        texts.append(text)
    
    for text in texts:
        reversed_text = text[::-1]
        print(reversed_text)

if __name__ == "__main__":
    reverse_string()