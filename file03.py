def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s =''
    for x in data:
        if x.isdigit():
            s += x        
    return print(list(s))

# Read data from file
f = open('txt_file/data03.txt', encoding='UTF-8')
d_file = f.read()
main(d_file)