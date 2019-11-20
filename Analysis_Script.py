import os
import csv
import pdb
import sys
import datetime
from matplotlib import pyplot
import tkinter as Tkinter
import tkinter.filedialog as tkFileDialog

#File Section window, limited to only show .csv files
rootwindow = Tkinter.Tk()
rootwindow.withdraw()
data_file=tkFileDialog.askopenfilename(parent=rootwindow,
                                                  filetypes=[("csv", "*.csv")],
                                                   title="Select csv analysis file")
#quits if no file selected
if data_file=="":
    print("No File Selected")
    input("Press Enter to quit: ")
    sys.exit()

data=open(data_file, 'rt')
calc_dict={}
zero_values={}
count=0
for line in csv.reader(data):
    if count==0:
        count+=1
        continue
    #if denominator (population) is not zero, stores dates against prescription %
    if line[6]!="0.0":
        if line[3] not in calc_dict.keys():
            calc_dict[line[3]]={}
        calc_dict[line[3]][line[4]]=float(line[7])
    else:
        #if 0 population store in a seperate "error" dict
        if line[3] not in zero_values.keys():
            zero_values[line[3]]=[]
        zero_values[line[3]]+=[line[4]]
    count+=1

#if there are 0 population practices, write them to a text file so people know what was excluded
if len(zero_values.keys())!=0:
    zero_text=open("Zero_Pop.txt","wt")
    zero_text.write("The Following Practices had 0 population report and so were excluded\n")
    for key, value in zero_values.items():
        zero_text.write("{}\n".format(key))
        for date in value:
           zero_text.write("{}\n".format(date)) 
    zero_text.close()


#Gets a sorted list of options for the dropdown
OPTIONS=[GP for GP in calc_dict.keys()]
OPTIONS=sorted(OPTIONS)
#Adds choices to dropdown and selects first one as default
dropVars=Tkinter.StringVar(rootwindow)
dropVars.set(OPTIONS[0])
choices=Tkinter.OptionMenu(rootwindow,dropVars,*OPTIONS)
choices.pack()
#close dropdown after selection
def select():
    rootwindow.quit()
#closes dropdown and quits script after clicking cancel
def cancel():
    rootwindow.quit()
    rootwindow.withdraw()
    print("Selection Cancelled")
    input("Press Enter to Quit:")
    sys.exit()
button = Tkinter.Button(rootwindow, text="Select", command=select)
button.pack()
button2 = Tkinter.Button(rootwindow, text="Cancel", command=cancel)
button2.pack()
#shows the previously hidden rootwindow
rootwindow.deiconify()
rootwindow.title("Select GP Practice")
rootwindow.geometry("300x100")
#Runs the selection loop
rootwindow.mainloop()
#gets the selection name and stores it in variable practice
practice=dropVars.get()
#hides the rootwindow (selection window)
rootwindow.withdraw()

dates=["-".join(key.split("-")[:2]) for key in calc_dict[practice].keys()]
values=[value for value in calc_dict[practice].values()]
pyplot.figure(figsize=(20,10))
pyplot.title("Percentage of prescriptions that were Antibiotics for {}".format(practice),fontsize=18)
pyplot.ylabel("Percentage")
pyplot.xlabel("Date")
pyplot.plot(dates, values)
pyplot.xticks(rotation=90)

pyplot.savefig('{} - Trend'.format(practice))
pdb.set_trace()
pass
