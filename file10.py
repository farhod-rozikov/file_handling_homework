def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    lst = data.split('\n')
    lst_len = []
    for i in lst:
        lst_len.append(len(i))     
    return max(lst_len)

# Read data from file
f = open('txt_file/data10.txt', encoding='UTF-8')
d_file = f.read()
print(main(d_file))