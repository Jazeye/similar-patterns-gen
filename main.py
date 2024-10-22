import random
import string

def detect_pattern(char):
    """
    Detects the type of character and returns the appropriate pool of characters.
    
    Args:
    - char: A single character to detect.
    
    Returns:
    - A string containing a pool of possible characters for that type.
    """
    if char.isdigit():
        return string.digits  # '0-9'
    elif char.islower():
        return string.ascii_lowercase  # 'a-z'
    elif char.isupper():
        return string.ascii_uppercase  # 'A-Z'
    else:
        return string.punctuation  # Special characters (symbols)


def generate_similar_pattern(base_pattern, n):
    """
    Generates a list of strings with patterns similar to the given base pattern.
    
    Args:
    - base_pattern: A string of any characters.
    - n: Number of strings to generate.
    
    Returns:
    - A list of strings based on the base pattern's structure.
    """
    result = []
    
    for _ in range(n):
        generated = ""
        for char in base_pattern:
            # Detect the type of character and choose a random character from that type
            possible_chars = detect_pattern(char)
            generated += random.choice(possible_chars)
        result.append(generated)
    
    return result


# Main function to interact with the tool
def main():
    print("Pattern-based List Generator")
    print("Provide a base pattern (e.g., 'aB1!', '1234', 'abcd', 'A12#').")
    
    base_pattern = input("Enter the base pattern: ")
    n = int(input("Enter the number of items to generate: "))
    
    generated_list = generate_similar_pattern(base_pattern, n)
    
    print(f"\nGenerated {n} items based on the pattern '{base_pattern}':")
    for item in generated_list:
        print(item)


if __name__ == "__main__":
    main()
