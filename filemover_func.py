#       Version         Python 3.6
#
#       Author          Mathew Perrow
#
#       Description     Program to select a folder
#                       and iterate through files in folder
#                       and move any files that have been 
#                       created or modified in the last 24 hours
#                       to another selected folder
#
import filemover_main
import filemover_gui
import shutil
import time
import os
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog




def center_window(self, w, h): 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
                                                                                #Begins scan and catches user imput error
def begin_Scan(self):
    try:
        lst_files(self)
    except OSError:
        tk.messagebox.showerror('Invalid entry','Please check filepath')


def ask_directory(self):                                                        #Initiates folder selection and inserts selected folder into text box
    directory = filedialog.askdirectory(initialdir = 'C:/' ,title='Select Folder')
    self.txt_foldscan.insert(1,directory)
    

def ask_destination(self):
    directory1 = filedialog.askdirectory(initialdir = 'C:/' ,title='Select Folder')
    self.txt_foldrec.insert(1,directory1)
       
    
def lst_files(self):                                                            #Grabbing strings in text boxes 
    dir_folder= self.txt_foldscan.get()                                         #making list of files in dir_folder 
    dest_folder= self.txt_foldrec.get()
    dirlist = os.listdir(dir_folder)               
    for i in range(len(dirlist)):                                               #Iterating through list and running find_mod_files by index for length of index
        find_mod_files(self,dir_folder + '/{}'.format(dirlist[i]),dest_folder)

                                                                            
def find_mod_files(self,path,dest_folder):                                      #Using current seconds since epic and seconds since last modification since epic
    epic = time.time()                                                          #if seconds since last epic 24 hours ago (yest_epic) is less than modification time
    yest_epic = epic - 86400
    mod_time = os.path.getmtime(path)                                           #seconds since last epic(mod_time) than copy file
    if mod_time > yest_epic:        
        copy_file(self,path,dest_folder)                        
    return

def copy_file(self,path,dest_folder):                                           #Copies file modified or created in last 24 hours to destination folder
    shutil.copy(path,dest_folder)            
    return
    
def reset(self):                                                                #Clears text boxes 
    self.txt_foldscan.delete(0,END)
    self.txt_foldrec.delete(0,END)


def ask_quit(self):
    tk.messagebox.askquestion("Exit program", "Okay to exit application?")
    answer = tk.messagebox.askquestion("Exit program", "Okay to exit application?")
    if answer == 'yes':
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass
