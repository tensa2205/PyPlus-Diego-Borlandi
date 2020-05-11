import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

#Variables globales
ahorcado = 'ahorcado'
ta_te_ti = 'ta te ti'
otello = 'otello'
#Esto guardo en el valor del diccionario


def main(args):
	layout = [
		[sg.Text('Nombre jugador'),sg.InputText(key='-NOMBRE-')],
		[sg.Button('Guardar nombre')],
		[sg.Text('Juegos')],
		[sg.Button('Ahorcado',size=(20,1),disabled=True,key='-AHORCADO-')],
		[sg.Button('TA - TE - TI',size=(20,1),disabled=True,key='-TATETI-')],
		[sg.Button('Otello',size=(20,1),disabled=True,key='-OTELLO-')],
		[sg.Button('Salir')]
	]
	window = sg.Window('Juegos.py', layout)

	jugadores = {} #Diccionario que guardará de forma clave -> nombre_jugador, valor -> juego.
	sigo_jugando = True
	while sigo_jugando:

		while True:
			event, values = window.read()
			if event in (None,'Salir'):
				sigo_jugando = False
				break #Salgo
			if event in ('Guardar nombre'):
				window['-AHORCADO-'].update(disabled = False)
				window['-TATETI-'].update(disabled = False)
				window['-OTELLO-'].update(disabled = False) #Habilito los botones.
				nombre = values['-NOMBRE-'] #Tomo el nombre.
				window['-NOMBRE-'].update('')

			if event in ('-AHORCADO-'):
				jugadores[nombre] =  ahorcado #guardo el nombre y el juego que jugó mi usuario.
				window.Minimize()
				hangman.main() #juego


			if event in ('-TATETI-'):
				jugadores[nombre] =  ta_te_ti #guardo el nombre y el juego que jugó mi usuario.
				window.Minimize()
				tictactoeModificado.main() #juego

			if event in ('-OTELLO-'):
				jugadores[nombre] =  otello #guardo el nombre y el juego que jugó mi usuario.
				window.Minimize()
				reversegam.main()
		window.close()

	archivo = open('JugadoresEnJSON.txt','w')
	json.dump(jugadores,archivo)
	archivo.close()

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

