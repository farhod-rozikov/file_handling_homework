def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s = 0
    for x in data:
        if x.isdigit():
            s += int(x)       
    return s

# Read data from file
f = open('txt_file/data07.txt', encoding='UTF-8')
d_file = f.read()
print(main(d_file))