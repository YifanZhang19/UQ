def partition(char, string) :
    """Return 'string' split at 'char'.

    The returned result is a tuple consisting of three strings that
    partition 'string' at 'char' - i.e. the substring before the first occurrence
    of 'char', 'char', and the substring after the first occurrence of 'char'.
    If 'char' does not occur in 'string' then the first component returned
    is the entire 'string' and the last two components are empty strings.

    Parameters:
        char (string): The character used to partition string.
        string (string): The string being partitioned.

    Return:
        tuple<str, str, str>: sub-string before char, char, sub-string after char;
                              or 'string', "", "".
    """
    index = find(char, string)
    if index == -1 :
        return string, '', ''
    else :
        return string[:index], char, string[index+1:]
