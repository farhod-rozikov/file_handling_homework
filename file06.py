def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    lst = data.split('\n')
    lst_len = []
    for i in lst:
        lst_len.append(len(i))     
    return lst_len

# Read data from file
f = open('txt_file/data06.txt', encoding='UTF-8')
d_file = f.read()
print(main(d_file))