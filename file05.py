def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    c = 0
    for x in data:
        if x.isdigit():
            c += 1        
    lst =[c, len(data) - c]
    return lst 

# Read data from file
f = open('txt_file/data05.txt', encoding='UTF-8')
d_file = f.read()
print(main(d_file))