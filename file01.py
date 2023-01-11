def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
     """
    lst = data.split(',')        
    return print(lst)

# Read data from file
f = open('txt_file/data01.txt', encoding='UTF-8')
d_file = f.read()
main(d_file)