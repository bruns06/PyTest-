#TODO fixare tempo, displaya sia tempo che giorno

from datetime import date
import time


#asks for input
    #choice = input("Would you wish to know date or time?\ntype d/t\nor press e to quit.\n")

#gets the date
da = date.today()
#gets the time
ti = time.localtime()
#sets time format scemo chi lgg egege xd
current_date = da.strftime("%m/%d/%Y")
current_time = time.strftime("%H:%M:%S" , ti)


    #if(choice == 'd'):
     #   print(date)
    #elif(choice == 't'):
     #   print(current_time)
    #elif(choice == 'e'):
     #   quit()
    #else:
     #   print('Wrong choice, pick either d for date or t for time\n')


