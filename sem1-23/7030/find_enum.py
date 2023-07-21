def find(char, string) :
    """Return the first i such that string[i] == char

    Parameters:
        char (string): The character being searched for.
        string (string): The string being searched.

    Return:
        int: Index position of 'char' in 'string',
             or -1 if 'char' does not occur in 'string'.
    """
    for i, c in enumerate(string) :
        if c == char :
            return i
    return -1

# Example use
print(find('m', 'spam'))
print(find('s', 'spam'))
print(find('x', 'spam'))
