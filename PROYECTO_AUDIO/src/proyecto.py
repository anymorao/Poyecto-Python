
import reproducir
import consola_io

def main():
        
        # creamos la ventana y le indicamos un titulo:
       
	#empieza el proyecto narrando una introduccion
	#reproducir.reproduce("1a.wav")
	#reproducir.limpiar()

	#Inicia el cuento y se espera que el usuario ingrese un numero
	reproducir.reproduce("1a.wav")

	#validacion de un numero
	t=1
	while t:
               
		 #num2 = raw_input("Escoja una opcion: 1,2,3,4 o 9 \n Su eleccion es: ")
		print("Escoja una opcion: 1,2,3,4 o 9 \n  ")
		num2=consola_io.getkey()
		print("Su eleccion es: "+num2)
		try:
			num2=int(num2)
			if(num2==9):
				main()
			elif(num2==1):
				reproducir.reproduce("2.wav")
				t2=1
				while t2:
					#num3 = raw_input("Escoja una opcion: 1,2,3,4,5 o 9 \n Su eleccion es: ")
					print("Escoja una opcion: 1,2,3,4,5 o 9 \n ")					
					num3=consola_io.getkey()
					print("Su eleccion es: "+num3)
					try:
						num3=int(num3)
						if(num3==9):
							main()
						elif(num3==1):
							reproducir.reproduce("6.wav")
							t2=0
						elif(num3==2):
							reproducir.reproduce("7.wav")
							t2=0
						elif(num3==3):		
							reproducir.reproduce("8.wav")
							t2=0
						elif(num3==4):
							reproducir.reproduce("9.wav")
							t2=0
						elif(num3==5):
							reproducir.reproduce("10.wav")
							t2=0
								
					except ValueError:
						pass
				t=0

			elif(num2==2):
				reproducir.reproduce("3.wav")
				t3=1
				while t3:
					#num4 = raw_input("Escoja una opcion: 1,2 o 9 \n Su eleccion es:  ")
					print("Escoja una opcion: 1,2 o 9 \n ")
					num4=consola_io.getkey()
					print("Su eleccion es: "+num4)
					try:
						num4=int(num4)
						if(num4==9):
							main()
						elif(num4==1):
							reproducir.reproduce("11.wav")
							t3=0
							t4=1
							while t4:
								#num5 = raw_input("Escoja una opcion: 1,2 o 9 \n Su eleccion es: ")
								print("Escoja una opcion: 1,2 o 9 \n ")
								num5=consola_io.getkey()
								print("Su eleccion es: "+num5)
								try:
									num5=int(num5)
									if(num5==9):
										main()
									elif(num5==1):
										reproducir.reproduce("12.wav")
										t4=0
									elif(num5==2):
										reproducir.reproduce("13.wav")
										t4=0
										t5=1
										while t5:
											#num6 = raw_input("Escoja una opcion: 1,2 o 9 \n Su eleccion es: ")
											print("Escoja una opcion: 1,2 o 9 \n ")
											num6=consola_io.getkey()
											print("Su eleccion es: "+num6)
											try:
												num6=int(num6)
												if(num6==9):
													main()
												elif(num6==1):
													reproducir.reproduce("14.wav")
													t5=0
												elif(num6==2):
													reproducir.reproduce("15.wav")
													t5=0
											except ValueError:
												pass


								except ValueError:
									pass




						elif(num4==2):
							reproducir.reproduce("7.wav")
							t3=0
					except ValueError:
						pass
				t=0
				
			elif(num2==3):
				reproducir.reproduce("4.wav")
				t=0
			elif(num2==4):		
				reproducir.reproduce("5.wav")
				main()
		
		except ValueError:
			pass
	print "\nY asi \ncolorin colorado \neste cuento se ha acabado"

#ejemplo limpiar pantalla: reproducir:limpiar 
if __name__ == "__main__":
            main()
