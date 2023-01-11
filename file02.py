def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(data)

# Read data from file
f = open('txt_file/data02.txt', encoding='UTF-8')
d_file = f.read()
print(main(d_file))