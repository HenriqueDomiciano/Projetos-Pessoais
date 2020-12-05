import numpy as np 
import matplotlib.pyplot as plt 
m=15
#mortes registradas desde 01/04
mortes_registradas=np.array([242,324,363,445,486,564,686,820,954,1068,1140,1223,1328,1532,1757,1947,2141,2361,2462,2587,2741,2906,3313,3670,4045,4271,4543,5063,5511,5901,6410,6750,7025,7343,7921,8588,9188,9992,10656,11123,11625,12404,13158,13993,14929,])
#casos registrados desde 01/04
casos_gerais=np.array([6880,8044,9194,10360,11254,12183,14034,16188,18145,19789,20962,22192,23430,25262,28610,30683,33682,36722,38654,40743,43079,45757,49492,52995,59196,62859,66501,72899,79361,85380,92109,96559,101147,108266,114715,126611,135693,145892,156061,162699,169143,177602,189157,202918,218223])
#casos diarios aumento 
casos_diarios=np.array([41,82,39,82,41,78,122,134,134,114,72,83,105,204,225,190,194,220,101,125,154,165,407,357,375,226,272,520,448,390,509,304,275,318,578,667,600,804,664,467,502,779,754,835,824])

time=np.linspace(1,len(mortes_registradas),len(mortes_registradas))
time2=np.linspace(1,len(mortes_registradas)+15,len(mortes_registradas)+15)
func1=np.polyfit(time,mortes_registradas,4)
func2=np.polyfit(time,casos_gerais,4)
func3=np.polyfit(time,casos_diarios,4)
funccase=np.poly1d(func2)
func=np.poly1d(func1)
funcdaydeath=np.poly1d(func3)


for k in range(40):
    m=m+k
    print(m,"-----",funccase(len(mortes_registradas)+k))
    m=15

print(funccase,'\n ',func)

#Grafico número de mortes registradas     
plt.figure("Mortes")
plt.ylabel("mortos por covid-19")
plt.xlabel("dias a partir de 01/04")
plt.grid(True,axis='y')
plt.yscale("linear")
plt.plot(time,mortes_registradas,color='b',label='registrados')
plt.plot(time2,func(time2),color='c',label='previsão')
plt.legend()

#Grafico numero de casos registrados
plt.figure("Casos Registrados")
plt.yscale('linear')
plt.grid(True,axis='y')
plt.ylabel("Casos Registrados")
plt.xlabel("dias a partir de 01/04")
plt.plot(time,casos_gerais,color='g',label="casos registrados")
plt.plot(time2,funccase(time2),color='c',label="curva esperada")
plt.legend()

#Grafico numeros diarios
plt.figure("Casos diarios de mortes")
plt.ylabel("Mortes registradas p/dia")
plt.xlabel("dias a partir de 01/04 ")
plt.grid(True,axis='y')
plt.yscale('linear')
plt.plot(time,casos_diarios,color="m",label='dados registrados ate o dia 15/05')
plt.plot(time2,funcdaydeath(time2),color='y',label='mortes diarias polinomial fit prediction')
plt.legend()

plt.show()
