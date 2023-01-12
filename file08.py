def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    lst = []
    for x in data:
        if x.isdigit():
            lst.append(int(x))        
    return max(lst)

# Read data from file
f = open('txt_file/data08.txt', encoding='UTF-8')
d_file = f.read()
print(main(d_file))