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



main();
ventana.close()



