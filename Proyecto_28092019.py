import RPi.GPIO as GPIO
import time, Tkinter, thread
from Tkinter import*
from struct import*
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')
import numpy as np


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN)

act=GPIO.PWM(3, 1168);
act2=GPIO.PWM(5, 7500);  #2500
act.start(100);
act2.start(50);
apagado=0;
rpm=0.0;
hz=0.0;
hz2=0.0;
pid=0;

def enviar(opcion):

	
def Btn_mtr_on():

	
def Btn_mtr_off():

	
def vel(tmr):

		

				
def sms(tmr):
	
		
			
def main():
	thread.start_new_thread(vel,(0.2,));
	thread.start_new_thread(sms,(0.5,));
	ventana.mainloop()

ventana = Tkinter.Tk()
ventana.title("Proyecto Diplomado")
ventana.geometry("797x443+0+0")
frame_00 = Frame(ventana, width=697, height=443, bg="#8a8a8a")
frame_00.place(x=100, y=0)
frame_00_1 = Frame(frame_00, width=690, height=440, bg="#9a9a9a")
frame_00_1.place(x=0, y=0)
btn_00 = Button(frame_00_1, text="Activar MOTOR", command=Btn_mtr_on,width=12,height=1)
btn_00.place(x=10, y=20)
btn_01 = Button(frame_00_1, text="Apagar Motor", command=Btn_mtr_off,width=12,height=1)
btn_01.place(x=10, y=50)
velocidad = Tkinter.Scale(frame_00_1, from_=3165, to=0, label="V",width=40, length=300, resolution=0.1)
velocidad.place(x=10, y=100)

fig, ax = plt.subplots(figsize=(5.2, 4))
plt.ion()
line, = ax.plot([], [])
Figure = FigureCanvasTkAgg(fig, master=frame_00)
ax.set_ylim([0, 5000])
ax.set_xlim([0, 200])
Figure.get_tk_widget().place(x=150, y=10)
ax.grid(which='major',linestyle='-', linewidth='0.5', color='red')
ax.grid(which='minor',linestyle=':', linewidth='0.5', color='black')


main();
ventana.close()



