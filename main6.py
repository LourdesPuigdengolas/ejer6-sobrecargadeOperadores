from viajero_frec import Viajero
import csv

if __name__=='__main__':
       
        DatosViajeros= []  #inicializar lista vacia
        with open("datos_de_viajero.csv") as archivo:
                reader = csv.reader(archivo, delimiter=',')
                for fila in reader:
                        unViajero= Viajero(fila[0], fila[1], fila[2], fila[3], int(fila[4]))
                        DatosViajeros.append(unViajero)
        
        '''viajeroMayor= Viajero(0,0,0,0,0)
        
        for i in range(len(DatosViajeros)):
                if DatosViajeros[i] > viajeroMayor.__millasAcum:
                        viajeroMayor= DatosViajeros[i]'''

        print(f"--- MENU: ---")
        print(f"[1]. Ver el/los viajero/s con mayor cantidad de millas acumuladas. ")
        print(f"[2]. Acumluar millas")
        print(f"[3]. Canjear millas")
        print(f"[0]. Salir")
        opcion= int(input("Ingrese el numero de opción que desea: "))
        
        while opcion != 0:  
               
                if opcion == 1:
                        for i in range(len(DatosViajeros)):
                                m=0                     
                                mayor=Viajero.mayorCantMillas_gt_(DatosViajeros[i],m)
                        print(f'El viajero con más millas acumuladas es: {mayor}')
                       
                elif opcion == 2: 
                        for i in range(len(DatosViajeros)):
                                v=Viajero
                                Viajero.acumMillas__ad__(DatosViajeros, v)
                                millasRecorridas= int (input('Ingrese cantidad de millas recorridas: '))
                                acumuladas= int(DatosViajeros[i].acumularMillas(millasRecorridas))
                elif opcion ==3:
                        for i in range(len(DatosViajeros)):
                                millasACanjear= int(input('Ingrese la cantidad de millas que desea canjear: '))
                                DatosViajeros[i].canjearMillas__sub__(millasACanjear)

                        
                opcion= int(input("Ingrese el numero de opción que desea: "))
