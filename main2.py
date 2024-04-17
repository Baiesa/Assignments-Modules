# main2.py

import text_utils as tu

def main():
    input_string = input("Enter a string: ")

    reversed_string = tu.reverse_string(input_string)
    print("Reversed string:", reversed_string)

    capitalized_string = tu.capitalize_string(input_string)
    print("Capitalized string:", capitalized_string)

if __name__ == "__main__":
    main()