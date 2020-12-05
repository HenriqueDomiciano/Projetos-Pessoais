from bs4 import BeautifulSoup 
import requests,lxml,re,telepot
bot= telepot.Bot('929250745:AAG2ehDPbfqufytHOU0w3BPHIIuNFGm1ceo')
response=bot.getUpdates()
print(response)
anterior=[]
teste = []
texto='' 
for r in range (len(response)):
    texto=''
    user_id=response[r]
    user_id=user_id['message']
    user_id=user_id['from']
    user_id=user_id['id']

    if not(user_id in anterior):

        value = requests.get(r'http://www.pra.ufpr.br/portal/ru/ru-centro-politecnico/')

        value_new= value.text

            #soup=BeautifulSoup(value_new,'lxml')
            #cardapiododia=soup.find('div', id= 'post')
            
        soup=BeautifulSoup(value_new,'lxml')
        cardapio=soup.find('div', id='post')
        teste=cardapio.find_all('p')

        for x in range (2,6):
            texto=texto+(BeautifulSoup.get_text(teste[x]))
        
        bot.sendMessage(user_id,texto)
        anterior.append(user_id)
print(anterior)