# Reverse a String in Python Using a For Loop | Python Interview Question #1
"""var1 ="HelloWorld!"

reversed_str = "";
for char in var1:
    reversed_str = char + reversed_str;
print(reversed_str);"""

# using function to reverse a string 

def reverse_string(input_str)-> str:
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")
    revesed_str=""
    for char in input_str:
        revesed_str = char + revesed_str
    return revesed_str

if __name__ == "__main__":
        try:
            user_input = input("Enter a string to reverse: ")
            result = reverse_string(user_input)
            print(f"Rersed string: {result}")
        except TypeError as e :
                print(f"Error: {e}")    
        