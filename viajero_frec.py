class Viajero:
    __numViajero= " "
    __dni= " "
    __nombre= " "
    __apellido= " "
    __millasAcum = " "
    def __init__(self, numViajero, dni, nombre, apellido, millasAcum): #)constructor
     self.__numViajero = numViajero
     self.__dni = dni
     self.__nombre= nombre
     self.__apellido= apellido
     self.__millasAcum= millasAcum
   
   
  
    def getMillas(self):
      return self.__millasAcum
    
    def acumularMillas(self, millasRecorridas):
       self.__millasAcum+= millasRecorridas
       print(f' Las millas acumuladas son: {self.__millasAcum}')
       return self.__millasAcum
    
    def canjearMillas__sub__(self, millasACanjear, acumuladas):
        if millasACanjear <= acumuladas:
          acumuladas-=millasACanjear
          print(f'millas canjeadas')
          return acumuladas
        else:
         print(f'No tienes suficientes millas! elige un monto menor o igual a {acumuladas}.')

    def __gt__(self, other):
      return self.__millasAcum > other.__millasAcum
    
    def mayorCantMillas_gt_(self,m): 
      if self.__millasAcum > m: #comprara con un viajero none
        m= self.__millasAcum
      return self.__nombre 
    
    def acumMillas__ad__(self, v):
      v+=self.__millasAcum
      return v
    

