from time import sleep

def primeira_atividade():
    print("Primeira atividade iniciada")
    sleep(2)
   

def segunda_atividade():
    print("Segunda atividade iniciada")
    sleep(2)
    

def terceira_atividade():
    print("Terceira atividade iniciada")
    sleep(2)
    

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print("Pipeline finalizada")

if __name__ == "__main__":
    pipeline()