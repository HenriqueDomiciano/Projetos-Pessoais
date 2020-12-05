with open(r'C:\Users\Dell\Desktop\Decodificador_3\Binary_to_String\example.txt','r') as f:
    data=f.read()

def try_mistake(string, paridade):
    t = 0
    x = list(string)
    for v in x:
        if v == '1':
            t += 1
    if t % 2 == 0 and paridade == '0':
        return True
    elif t % 2 == 1 and paridade == '1':
        return True

    return False


def transform(string1):
    result = []
    for i in range(0, len(string1), 10):
        string2 = string1[i:i+8]
        paridade = string1[i+8:i+9]
        if try_mistake(string2,paridade):
            result.append(chr(int(string2, 2)))
        else:
            result.append('e')
    result = ''.join(result)
    result = result.replace('\n',',')
    result = result.split(',')
    x = [m[::-1] for m in result]
    for m in range(len(x)):
        x[m]=x[m].rstrip()
        if 'e' in x[m] :
            x[m]='erro'
    for i in range(0,len(x),3):
        with open ('v.txt','a') as f:
            f.write('Tensao: '+ x[i]+'V ; Corrente : '+ x[i+1] +' ; Temperatura :'+ x[i+2]+'\n')
transform(data)