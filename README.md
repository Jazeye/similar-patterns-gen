# Pattern-Based List Generator Tool

### Overview

The **Pattern-Based List Generator Tool** is a Python-based utility that generates random strings based on a user-defined input pattern. The tool takes in a pattern consisting of any combination of digits, lowercase letters, uppercase letters, and special characters, and generates random strings that follow the same structure.

### Features

- Generate patterns based on the structure of the input (digits, lowercase, uppercase, symbols).
- Randomized characters while maintaining the original pattern's format.
- Support for multiple character types:
    - `0-9` for digits
    - `a-z` for lowercase letters
    - `A-Z` for uppercase letters
    - Special symbols such as `!@#$%^&*()`
- Specify how many patterns you want to generate.

### Example Usage

### Input

Given the input pattern `aB1!`, the tool will generate strings where:

- `a` (a lowercase letter) is replaced by another random lowercase letter.
- `B` (an uppercase letter) is replaced by another random uppercase letter.
- `1` (a digit) is replaced by another random digit.
- `!` (a symbol) is replaced by another random symbol.

### Output

For an input of `aB1!` and a request to generate 5 patterns, possible outputs could be:

```csharp
Generated 5 items based on the pattern 'aB1!':
kL4$
hQ7#
mP9@
fS2%
jG8^
```

For an input pattern like `1234`, possible outputs could be:

```yaml
Generated 5 items based on the pattern '1234':
8493
2731
6214
9537
4085
```

### Installation

To use this tool, you need Python installed on your system. Follow the instructions below to set it up:

1. **Clone the repository:**
    
    ```bash
    git clone https://github.com/Jazeye/similar-patterns-gen.git
    cd similar-patterns-gen
    ```
    
2. **Run the tool:**
    
    ```bash
    python main.py
    ```
    

### Usage Instructions

Once the tool is running, follow these steps:

1. Provide a **base pattern** consisting of digits, letters, or symbols (e.g., `aB1!`, `1234`, `xY!2`).
2. Enter the number of patterns you want to generate.
3. The tool will output a list of randomized strings following the structure of your input.

**Example:**

```bash
Pattern-based List Generator
Provide a base pattern (e.g., 'aB1!', '1234', 'abcd', 'A12#').
Enter the base pattern: aB1!
Enter the number of items to generate: 5

Generated 5 items based on the pattern 'aB1!':
kL4$
hQ7#
mP9@
fS2%
jG8^

```

### Customization

You can extend or modify the tool to support more character types or specific rules. The following are currently supported:

- `0-9` for digits
- `a-z` for lowercase letters
- `A-Z` for uppercase letters
- Special characters like `!@#$%^&*()`

### License

This project is licensed under the MIT License. See the LICENSE file for details.
