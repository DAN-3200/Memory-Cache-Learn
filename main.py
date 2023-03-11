import subprocess, time

def limpartela():
  subprocess.run("clear", shell= True)

for i in range(4):
  print("Loading{}".format("."*i))
  time.sleep(0.5)
  limpartela()

AppCons = {};
Date = {
  "domingo": 0,
  "segunda": 0,
  "terça": 0,
  "quarta": 0,
  "quinta": 0,
  "sexta": 0,
  "sabado": 0
};


loop = 0
while loop < 1:
  print("--- Memory Cache ---")
  dia = input(" Date: ")
  if dia.lower() not in AppCons:
    limpartela()
    for dat in Date:
      if dia.casefold() == dat.casefold(): 
        print("  @ {}".format(dat))
        print("  ----")
      
        tonel = []
        while True:
          box = []
          app = input("  App: ")
        
          memory = float(input("  Memory: "))
          box.append(app); box.append(memory)
      
          tonel.append(tuple(box))
          exit = str(input("   *finish the register?  "))
          if exit.casefold() == "sim" or exit.casefold() == "s" :
            break
          else:
            print("----") 
            continue
         
        AppCons[dat] = tonel
        x = input("   *Exit? ")
        if x.casefold() == "sim" or x.casefold() == "s" :
          for i in range(4):
              limpartela()
              print("Loading{}".format("."*i))
              time.sleep(0.5)
              
          loop += 2
        else:
          limpartela()
          continue
          
        
    if dia.lower() not in Date:
      print("  !Date Invalid",)
      
  else:
    print("  ! Invalido! Você não pode sobrescrer os @dados !", "\n")


else:
  limpartela()
  for key in AppCons.values(): # Média de consumo diario
    list = []
    for i in key:
      list.append(i[1])
    else:
      key.append(sum(list))

  weekCons = 0
  for key in AppCons.values():
    weekCons += key[-1]
  
  print("----- O U T P U T -----", "\n",AppCons, "\n")
  print(" & Consumo Semanal: {}".format(weekCons))

    
"""
  Consumo Semanal: ok
  Consumo Total por dia
  
  *Média de consumo por dia
  *Média consumo semanal por App
"""

