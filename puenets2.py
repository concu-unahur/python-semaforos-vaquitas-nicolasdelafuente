import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

semaphore = threading.Semaphore(1)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):
    while(True):
      if (inicioPuente-1==self.posicion):
        semaphore.acquire()

      if(30==self.posicion):
        semaphore.release()
      
      self.avanzar()


class Puente():
  def dibujarPuente(self):
    print(' ' * inicioPuente + '=' * largoPuente)


puente1 = Puente()
puente2 = Puente()

vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')



while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  puente1.dibujarPuente()
  for v in vacas:
    v.dibujar()
  puente1.dibujarPuente()
  puente2.dibujarPuente()
  for v in vacas:
    v.dibujar()
  puente2.dibujarPuente()
  time.sleep(0.2)
