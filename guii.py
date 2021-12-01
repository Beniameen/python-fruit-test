import tkinter
import tkinter.messagebox
import tkinter.font
import json
import random
class ProgramGUI:

    def __init__(self):
        #Create main window
        self.main = tkinter.Tk()
        self.main.title('Food Quiz!')
        self.main.geometry('550x400')
        self.main.minsize(width=500, height=400)
        self.main.configure(bg='#5c9ead')
        self.main.iconbitmap('fruit.ico')
        self.font1 = tkinter.font.Font(family='Courier', size=24, weight='bold')
        self.font2 = tkinter.font.Font(family='Arials', size=24, weight='bold')

        #Load data from data.txt, show error message & terminate if file does not exist or is invalid
        try:
            self.__f = open('data.txt', 'r')
            self.data = json.load(self.__f)
            self.__f.close()

        except (FileNotFoundError, ValueError):
            tkinter.messagebox.showerror('Missing/Invalid file.')
            self.main.destroy()
            return
        
        #Define components, initiliase score and label variables 
        self.components = ['Calories','Fibre', 'Sugar', 'Vitamin C']
      
        self.name1 = tkinter.StringVar()
        self.name2 = tkinter.StringVar()
        self.componentLab = tkinter.StringVar()

        #Create frames
        
        self.questionBox = tkinter.Frame(self.main, bg='#5c9ead')
        self.buttonBox = tkinter.Frame(self.main, bg='#5c9ead')

        #Create buttons and labels
        tkinter.Label(self.questionBox, text='100 grams of', font=self.font2, bg='#5c9ead', fg='#fffdf7').pack()
        tkinter.Label(self.questionBox, textvariable=self.name1, font=self.font1, bg='#5c9ead', fg='#EFBC9B').pack()
        tkinter.Label(self.questionBox, text='contains more ', font=self.font2, bg='#5c9ead', fg='#fffdf7').pack()
        tkinter.Label(self.questionBox, textvariable=self.componentLab, font=self.font1, bg='#5c9ead', fg='#EFBC9B').pack()
        tkinter.Label(self.questionBox, text=' than 100 grams of  ', font=self.font2, bg='#5c9ead', fg='#fffdf7').pack()
        tkinter.Label(self.questionBox, textvariable=self.name2, font=self.font1, bg='#5c9ead', fg='#EFBC9B').pack()
        tkinter.Button(self.buttonBox, text= 'True' , padx=40, pady = 10 ,justify='left' ,command=lambda: self.checkAnswer(True)).pack(side='left') 
        tkinter.Button(self.buttonBox, text= 'False', padx=40, pady = 10 ,justify='right',command=lambda: self.checkAnswer(False)).pack(side='left')
        
        
        self.questionBox.pack(pady=10)
        self.buttonBox.pack(pady=20)

        #Show first question
        self.showQuestion()

        #Start main loop
        tkinter.mainloop()

    def showQuestion(self):
        #Create/update question attributes
        self.items = random.sample(self.data, 2)
        self.component = random.choice(self.components)
    
     
       

        #Update labels
        self.name1.set(self.items[0]['name'])
        self.name2.set(self.items[1]['name'])
        self.componentLab.set(self.component)
        
    def checkAnswer(self,answer):
       #determines whether the user clicked the correct button and shows a Correct/Incorrect messagebox.
       self.val1 =  self.items[0].get(self.component)
       self.val2 =  self.items[1].get(self.component)
       correct = self.val1 > self.val2
     
       if correct == answer :
            
            tkinter.messagebox.showinfo('Correct!', 'You got it right ')
    
       else:
            tkinter.messagebox.showerror('Incorrect!', 'You got it wrong' )
       
       #Generate new question
       self.showQuestion()

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
