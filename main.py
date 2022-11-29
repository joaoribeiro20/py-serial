import serial #Importa a biblioteca

while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        arduino = serial.Serial('COM4', 9600)
        print('Arduino conectado')
        break
    except:
        pass
while True: #Loop principal
    cmd = input('Digite "l" para ligar e "d" para desligar. ') #Pergunta ao usuário se ele deseja ligar ou desligar o led
    if cmd == 'l': #Se a resposta for "l", ele envia este comando ao Arduino
        arduino.write('l'.encode())
    elif cmd == 'd': #Senão, envia o "d"
        arduino.write('d'.encode())
    arduino.flush() #Limpa a comunicação
