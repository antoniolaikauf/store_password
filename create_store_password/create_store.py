import os
import json

# funzione per trasformare parola in caratteri unicode byte
def encoding_parola(parola):
   parola=list(parola.encode('utf-8'))
   return parola

dati=[]
while True:
    # id statement per creare ile se non esiste 
    # mettere nelle tonde il percorso dove si vuole mettere il file e il suo nome 
    if os.path.isfile('create_store_password/text.json'):
         query_for_user=input('se vuoi inserire una nuova password prema y\nse vuole leggere una password prema r\nse vuole chiudere il programma prema n\n')
        #  se utente vuole uscire dal programma
         if query_for_user=='n':break
        #  se utente vuole leggere una password 
         elif query_for_user=='r' and len(dati)>0:
            # mettere nelle tonde il percorso dove si vuole mettere il file e il suo nome 
            # aprire file e controllare se c'è una corrispondenza 
            with open('create_store_password/text.json', 'r') as f:
               controllo_password=input('inserisci la parola di controllo per far si che il programma ti ridia la vera password\n')
               dati = json.load(f)
               for line in dati:
                  if line['password_controllo'] == encoding_parola(controllo_password):
                     password=bytes(line['password']).decode('utf-8')
                     print(f"la tua password è: {password}")
                     break
         #se utente vuole salvare una password
         elif query_for_user=='y' :
           controllo_password=input('\ninserisci una password per far si che la tua vera password faccia riferimento a questa \n')
           password_ufficiale=input('inserisci la tua password che vuoi salvare  \n') 
           # mettere nelle tonde il percorso dove si vuole mettere il file e il suo nome 
           with open('create_store_password/text.json', 'w') as f:
            #  inserimento dei dati 
             frase={"password_controllo":encoding_parola(controllo_password), "password": encoding_parola(password_ufficiale)}
             dati.append(frase)
             text=json.dump(dati,f)
             continue
        #    controllo se esiste una password nel file 
         elif len(dati)==0:
            print('devi salvare prima una password')
            continue
    # se file non esiste
    else :
         # mettere nelle tonde il percorso di dive si vuole mettere il file e il suo nome 
        with open('create_store_password/text.json', 'w') as f:
           print('ottimo abbiamo creato il file dove salveremo le password\nora cosa vuoi fare?')
        continue