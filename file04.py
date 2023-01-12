def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s =''
    for x in data:
        if not x.isdigit():
            s += x        
    return list(s)

# Read data from file
f = open('txt_file/data04.txt', encoding='UTF-8')
d_file = f.read()
print(main(d_file))