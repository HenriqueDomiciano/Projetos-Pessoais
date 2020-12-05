from bs4 import BeautifulSoup
import requests,lxml,csv,re


def organizar_procurar(tipo,classe,link,t):


        titulo1=link.find(tipo,{'class':classe})

        try:
            titulo1=titulo1.string
            titulo1=titulo1.strip('')
            titulo1=titulo1.strip('\n\t')
            titulo1=titulo1.strip('|')


            if classe =='OLXad-list-title' and t :
                    ano=re.compile(r'\d\d\d\d' )
                    ano=ano.search(str(titulo1))
                    ano=ano.group()
                    return (titulo1,ano)


        except AttributeError:
            pass 
        return titulo1


def search(palavra_procura):
    
    
    carro=[]
    precos,local,detalhes,url,titulo,ano=[],[],[],[],[],[]
    
    
    for num in range(1,6):
        search_page=requests.get('https://pr.olx.com.br/regiao-de-curitiba-e-paranagua/autos-e-pecas/carros-vans-e-utilitarios?o='+str(num)+'&q='+ palavra_procura)
        search_page=search_page.content
        soup= BeautifulSoup(search_page,'lxml')
        links=soup.find_all('a',{'class':'OLXad-list-link'},href=True)
        links=links + soup.find_all('a',{'class':'OLXad-list-link-featured'},href=True)
        
        
        for link in links :
            precos=(organizar_procurar('p','OLXad-list-price',link,False))
            local=(organizar_procurar('p','text detail-region',link,False))


            try:
                titulo,ano=(organizar_procurar('h2','OLXad-list-title',link,True))



            except ValueError:
                ano=0
                titulo==(organizar_procurar('h2','OLXad-list-title',link,False))


            url=(link['href'])
            detalhes=(organizar_procurar('p','text detail-specific',link,False))
            carro.append([precos,titulo,ano,detalhes,url,local])
        
        
        with open (r'C:\Users\Dell\Desktop\python'+ '\\' +palavra_procura+'car.csv','w',newline='') as f:
            row=['precos','titulo','detalhes','url','local']
            valor=csv.writer(f)
            valor.writerow(row)
            valor.writerows(carro)

search('Palio')