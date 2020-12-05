import re
with open(r"C:\Users\Dell\Documents\carros.txt",'r') as f:
    lines=  f.readlines()
    lines = [line.replace('     ', '') for line in lines]
    for linha in lines :
         print (linha)
         values=re.compile(r'\d\d\d\d\d\d-\d')
         valor=values.search(str(linha))
         car=valor.group()
         with open (r"C:\Users\Dell\Documents\codigoFipe.txt",'w')as fw:
            fw.write(car)


         