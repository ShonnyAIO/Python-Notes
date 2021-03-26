# 1 de Abril = Sabado, Sum(martes 4 de dicho mes)
# OPCION D
Mes = 30
Semana = 30 // 7
Martes = 4
Total = 0
for i in range(0,Semana):
    Total = Total + Martes
    Martes = Martes + 7
# 4 + 11 + 18 + 25 
print(Total)