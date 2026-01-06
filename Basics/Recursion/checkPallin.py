def pallin(start, data):
    
    if start >= len(data)/2:
        return True
    if data[start] != data[len(data)-start-1]:
        return False
    return pallin(start+1, data)


data='Hello'
data1 = 'madam'
print(pallin(0,data1))
    

