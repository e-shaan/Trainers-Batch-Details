import datetime
import calendar

#batch_start_data : Batch Start Date in String Format -  "2021-02-19"
#days : A string of first three letters of the days   -  "MonWedFri" 
#sessions : Number of sessions in the batch, integer -   6

def get_date(batch_start_date , days , sessions):

    #print(batch_start_date , days , sessions)

    
    batch_start_date =datetime.datetime.strptime(batch_start_date, "%Y-%m-%d").strftime("%d/%m/%y")
    batch_start_date = datetime.datetime.strptime(batch_start_date, '%d/%m/%y')

    batch_start_day = calendar.day_name[batch_start_date.weekday()]
    batch_start_day = batch_start_day[0:3]
    
    sessions = int(sessions)+1


    if str(batch_start_day) not in days:
       sessions = sessions +1 

 
    while sessions!=0:
        if sessions == 3:
            batch_stop_date = batch_start_date + datetime.timedelta(1)
            #stop_day = calendar.day_name[date.weekday()]

        batch_start_date = batch_start_date + datetime.timedelta(1)
        batch_start_day = calendar.day_name[batch_start_date.weekday()]
        batch_start_day = batch_start_day[0:3]


        if batch_start_day in days:
            sessions = sessions -1 


    batch_stop_date = batch_stop_date.strftime("%d/%m/%y")
    batch_next_date = batch_start_date.strftime("%d/%m/%y")


    print(batch_stop_date , batch_next_date)

    batch_stop_date =datetime.datetime.strptime(batch_stop_date, "%d/%m/%y").strftime("%Y-%m-%d")
    batch_next_date =datetime.datetime.strptime(batch_next_date, "%d/%m/%y").strftime("%Y-%m-%d")


    print(batch_stop_date , batch_next_date)
 


    return batch_stop_date , batch_next_date


#get_date("2021-02-19" , "MonWedFri" , 6)   