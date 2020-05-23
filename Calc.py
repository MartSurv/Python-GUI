import tkinter as tk
import random
import time
import threading
import multiprocessing
from matplotlib import pyplot as plt

class Calculator:

    '''This is a Calculator class.'''

    def __init__(self):

        self.list = []
        self.thread_time = []
        self.process_time = []
        self.regular_time = []

    def suma(self):
        '''A function, which calculates the sum of a list'''
        self.total_sum = 0
        for i in range(0, len(self.list)):
            self.total_sum = self.total_sum + self.list[i]

    def sandauga(self):
        '''A function, which calculates the multiplication of a list'''
        self.total_mult = self.list[0]
        for i in range(self.list[0], len(self.list)):
            self.total_mult = self.total_mult * self.list[i]

    def maziausias(self):
        '''A function, which sorts the list'''
        self.list.sort()

    def make_threads(self):

        '''A function, which executes the calculations using multithreading.'''

        self.tr1 = threading.Thread(target=self.suma(), args=[])
        self.tr2 = threading.Thread(target=self.sandauga(), args=[])
        self.tr3 = threading.Thread(target=self.maziausias(), args=[])

        self.tr1.start()
        self.tr2.start()
        self.tr3.start()

        self.tr1.join()
        self.tr2.join()
        self.tr3.join()

    def make_process(self):

        '''A function, which executes the calculations using multiprocessing.'''

        self.pr1 = multiprocessing.Process(target=self.suma(), args=[])
        self.pr2 = multiprocessing.Process(target=self.sandauga(), args=[])
        self.pr3 = multiprocessing.Process(target=self.maziausias(), args=[])

        self.pr1.start()
        self.pr2.start()
        self.pr3.start()

        self.pr1.join()
        self.pr2.join()
        self.pr3.join()

    def go_standart(self):

        '''A function, which executes the calculations using regular Python execution method.'''

        self.suma()
        self.sandauga()
        self.maziausias()

class TheGUI(Calculator): # GUI klase, paveldejimas is Calculator klases

    '''This is the GUI class.'''

    def __init__(self, master=None):
        super().__init__()

        self.master = master
        master.title("Martynas_Survila_IF1900060")
        master.geometry('500x300')

        self.input_label = tk.Label(master, text="Enter amount to generate random numbers")
        self.input_label.grid(row=0, column=1, pady=5, padx=5)

        self.var1 = tk.StringVar()

        self.entry1 = tk.Entry(master, width=20, textvariable=self.var1)
        self.entry1.grid(row=2, column=1, pady=10)

        self.submit_button1 = tk.Button(master, text="Submit Regular", command=self.submit_regular, state='disabled')
        self.submit_button1.grid(row=3, column=0, pady=10, padx=5)

        self.submit_button2 = tk.Button(master, text="Submit Multithreading", command=self.submit_threads, state='disabled')
        self.submit_button2.grid(row=3, column=1)

        self.submit_button3 = tk.Button(master, text="Submit Multiprocessing", command=self.submit_process, state='disabled')
        self.submit_button3.grid(row=3, column=3)

        self.reset = tk.Button(master, text="Reset Values", command=self.resetValues, state='disabled')
        self.reset.grid(row=4, column=1, pady=10)

        self.make_plot = tk.Button(master, text="Make Plot", command=self.paint_plot, state='disabled')
        self.make_plot.grid(row=5, column=1)

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=6, column=1, pady=50)

        self.About = tk.Button(self.master, text="About", command=self.CreateNewWindow)
        self.About.grid(row=0, column=3)

        def toggle_state(*args):

            '''A callback function, which checks the user input and switches the state of the button.'''

            if self.entry1.get().isdigit() and len(self.entry1.get()) < 8:
                self.submit_button1['state'] = 'normal'
                self.submit_button2['state'] = 'normal'
                self.submit_button3['state'] = 'normal'
            else:
                self.submit_button1['state'] = 'disabled'
                self.submit_button2['state'] = 'disabled'
                self.submit_button3['state'] = 'disabled'
        
        self.var1.trace('w', toggle_state)

    def CreateNewWindow(self):

        '''A function, which handles the About section of the GUI. '''

        self.top = tk.Toplevel()
        self.top.title("About")
        self.label = tk.Label(self.top, text='Created by Martynas Survila', pady=10)
        self.label.grid(row=0, column=0)
        self.label2 = tk.Label(self.top, text='Usage rules:')
        self.label2.grid(row=1, column=0)
        self.label3 = tk.Label(self.top, text='*Floats, letters, symbols, negative numbers and other characters are not accepted*')
        self.label3.grid(row=2, column=0)
        self.label3 = tk.Label(self.top, text='*Maximum number length is 7 numbers*')
        self.label3.grid(row=3, column=0)
        self.label4 = tk.Label(self.top, text='*Plot can be drawn only after completing all submitions*')
        self.label4.grid(row=4, column=0)

    def resetValues(self):

        '''A function, which handles the Reset button of the GUI. '''

        self.reset['state'] = 'disabled'
        self.make_plot['state'] = 'disabled'
        self.regular_time = []
        self.thread_time = []
        self.process_time = []

    def submit_regular(self): # Regular mygtuko metodas su laiko skaiciavimu

        '''A function, which handles the Regular submit button of the GUI. '''

        self.reset['state'] = 'normal'
        if self.thread_time and self.process_time:
            self.make_plot['state'] = 'normal'

        self.list = random.sample(range(1, 1000000000), int(self.entry1.get()))

        self.num_amount = [len(self.list)]

        self.t1 = time.perf_counter()

        self.go_standart()

        self.t2 = time.perf_counter()
        self.x = self.t2 - self. t1
        self.regular_time.append(self.x)
        print(self.regular_time)

    def submit_threads(self):

        '''A function, which handles the Multithreading submit button of the GUI. '''

        self.reset['state'] = 'normal'
        if self.process_time and self.regular_time:
            self.make_plot['state'] = 'normal'

        self.list = random.sample(range(1, 1000000000), int(self.entry1.get()))

        self.t1 = time.perf_counter()

        self.make_threads()

        self.t2 = time.perf_counter()
        self.x = self.t2 - self. t1
        self.thread_time.append(self.x)
        print(self.thread_time)

    def submit_process(self):

        '''A function, which handles the Multiprocessing submit button of the GUI. '''

        self.reset['state'] = 'normal'
        if self.thread_time and self.regular_time:
            self.make_plot['state'] = 'normal'

        self.list = random.sample(range(1, 1000000000), int(self.entry1.get()))

        self.t1 = time.perf_counter()

        self.make_process()

        self.t2 = time.perf_counter()
        self.x = self.t2 - self. t1
        self.process_time.append(self.x)
        print(self.process_time)

class PlotChart(TheGUI):

    '''This is the Plot Chart class.'''

    def __init__(self, master=None):
        super().__init__(master=master)

    def paint_plot(self):

        '''A function, which handles the Make Plot submit button of the GUI. '''

        plt.plot(self.num_amount, self.thread_time, marker='o')
        plt.plot(self.num_amount, self.regular_time, marker='o')
        plt.plot(self.num_amount, self.process_time, marker='o')
        plt.xlabel('Numbers, amount')
        plt.ylabel('Time, seconds')
        plt.title('Statistics of given numbers sum, multiplication and sort')
        plt.legend(['Thread time', 'Regular time', 'Process time'])
        plt.show()

if __name__ == "__main__": # Driver code
    root = tk.Tk()
    my_gui = PlotChart(master=root)
    root.mainloop()