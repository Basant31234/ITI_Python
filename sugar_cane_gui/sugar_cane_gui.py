from tkinter import *
import csv 
import time


#counters
def large_counter():

		
		large_counter.counter +=1 
		print("large quantity:" , large_counter.counter)
		global large_intial_cost
		large_intial_cost=15
		global large_counterTcost
		large_counterTcost = large_counter.counter *large_intial_cost
		print("large cost:" , large_counterTcost)
		
	
large_counter.counter =0





def medium_counter():
		medium_counter.counter +=1 
		print("medium quantity:" , medium_counter.counter)
		global medium_intial_cost
		medium_intial_cost=10
		global medium_counterTcost
		medium_counterTcost = medium_counter.counter *medium_intial_cost
		print("medium cost:" , medium_counterTcost)
		return medium_counter.counter
		
medium_counter.counter =0


def small_counter():
		small_counter.counter +=1 
		print("small quantity:" , small_counter.counter)
		global small_intial_cost
		small_intial_cost=5
		global small_counterTcost
		small_counterTcost = small_counter.counter *small_intial_cost
		print("small cost:" , small_counterTcost)
	
small_counter.counter =0



win=Tk()
win.geometry('880x550')

# background photo

photo_1 = PhotoImage(file='Sugar cane in bamboo basket on white background__adobe_express.png')
photo_1 = photo_1.subsample(1,1)

label1 = Label( win, image = photo_1)
label1.place(x = 0, y = 0)

# buttons photo
photo_2 = PhotoImage(file='pngegg.png')
small = photo_2.subsample(6,6)
medium = photo_2.subsample(5,5)
large = photo_2.subsample(4,4)


# general labels

lab0=Label(win,text="***WELCOME  TO  ITI  CANE  JUICE  SHOP***",font=('Dancing Script SemiBold',18,'bold')).place(x=90,y=30)
CHOOSE=Label(win,text="Choose your size, please:",font=('Dancing Script SemiBold',17,'bold')).place(x=10,y=180)


# buttons and labels

B1  =Button(win ,height=150,width=80, bg="LemonChiffon",bd = '3', image=small,command = small_counter).place(x=60,y=250)
lab1=Label(win,text="Small\n 5 LE",font=('Dancing Script SemiBold',15,'bold')).place(x=70,y=410)

B2  =Button(win ,height=150,width=80, bg="LemonChiffon",bd = '3', image=medium,command = medium_counter).place(x=210,y=250)
lab2=Label(win,text="Medium\n 10 LE",font=('Dancing Script SemiBold',15,'bold')).place(x=220,y=410)

B3  =Button(win ,height=150,width=80, bg="LemonChiffon",bd = '3', image=large,command = large_counter).place(x=360,y=250)
lab3=Label(win,text="Large\n 15 LE",font=('Dancing Script SemiBold',15,'bold')).place(x=370,y=410)






#to excit
exit  =Button(win , text = "EXIT",bd='3',font=('Dancing Script SemiBold',15,'bold'),background="LemonChiffon",command=win.destroy)
exit.pack(side = BOTTOM)



win.mainloop()


# lists of data


size=["large","medium","small"]

qua=[]
qua.append(large_counter.counter)
qua.append(medium_counter.counter)
qua.append(small_counter.counter)



int_cost=[15,10,5]


co=[]
co.append(large_counterTcost)
co.append(medium_counterTcost)
co.append(small_counterTcost)


total_cost=sum(co)
myTime = time.ctime()

space=  ["","","",""]
TO_CO=  ["***TOTAL","PRICE**","",total_cost]
timey=  [myTime]



# write in the csv file

filename= "ITI_CANE_SHOP.csv"

with open(filename, 'w',newline='') as csvfile: 

	writer=csv.DictWriter(csvfile,fieldnames=['Size','Quantity',"cost/cup",'Total Cost'])
	writer.writeheader()
	
	csvwriter = csv.writer(csvfile) 
    
	for list in zip(size,qua,int_cost,co):			
		csvwriter.writerow(list) 
	
	csvwriter.writerow(space)
	csvwriter.writerow(TO_CO)
	csvwriter.writerow(timey)
	
	
	
