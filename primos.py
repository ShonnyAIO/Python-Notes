class A:
    def __init__(self, n):
        self.numero_de_casos = n
        self.Lista=[]
    
    def pedir_numeros(self):
        for i in range(self.numero_de_casos):
            self.Lista.append(int(input()))
    
    def salida(self):
        while(True):
            x = self.Lista[self.numero_de_casos-1] ; primo=True

            for i in range(2, x):
                if(i>x/2): break
                if(x%i == 0): primo=False; print(f"{x} es compuesto {i} {int(x/i)}"); break
            
            if(primo): print(f"{x} es primo")
            self.numero_de_casos-=1
            if(self.numero_de_casos==0): 

a = A(int(input())); a.pedir_numeros(); a.salida()