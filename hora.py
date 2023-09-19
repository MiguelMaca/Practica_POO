class Reloj:
    def hora_predeterminada(self):
        self.hora=00
        self.minuto=00
        self.segundo=00
    def __init__(self, hora, minuto, segundo):
        self.hora=hora
        self.minuto=minuto
        self.segundo=segundo
    def leer(self):
        Hora = int(input("Ingrese la hora: "))
        while Hora > 24 or Hora < 0:
            print("Valor no valido")
            Hora = int(input("Ingrese la hora: "))
        Minutos = int(input("Ingrese los minutos: "))
        while Minutos > 60 or Minutos < 0:
            print("Valor no valido")
            Minutos = int(input("Ingrese los minutos: "))
        Segundos = int(input("Ingrese los segundos: "))
        while Segundos > 60 or Segundos < 0:
            print("Valor no valido")
            Segundos = int(input("Ingrese los segundos: "))
        self.hora=Hora
        self.minuto=Minutos
        self.segundo=Segundos
    def mostrar(self):
        print(self.hora,":",self.minuto,":",self.segundo)
    def a_segundos(self):
        total_s=(((self.hora*60)+self.minuto)*60)+self.segundo
        print("El total de segundos tras la media noche es:",total_s)
    def segundos_desde_hora(self):
        segundo_minuto=(self.segundo*100)/60
        minuto_hora=(((segundo_minuto*0.01)+self.minuto)*100)/60
        segun_hora=self.hora+(minuto_hora*0.01)
        print("Las horas pasadas es:",segun_hora)

reloj=Reloj(00,00,00)
reloj.leer()
reloj.mostrar()
reloj.a_segundos()
reloj.segundos_desde_hora()