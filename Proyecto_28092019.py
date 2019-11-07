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
global act, v, velocidad, rpm, hz, apagado, pid, hz2;	
	ctn=0;
	filtro=0;
	filtro2=0;
	ctn2=0;
	ctn3=0;
	flag=0;
	flag_p=0;
	control=0.0;
	while 1:
	
		if (GPIO.input(7)==0):
			if (GPIO.input(11)==1 and flag==0):
				flag=1;
			if (GPIO.input(11)==0 and flag==1):
				ctn=ctn+1;
				flag=0;
			flag_p=1;
			if (ctn>100):
				rpm=0;
				rpm2=0;
				hz=0;
				hz2=0;
		if (GPIO.input(7)==1):
			if (flag_p==1):
				filtro=ctn+filtro;
				filtro2=ctn+filtro2;
				ctn3=ctn3+1;
				ctn2=ctn2+1;
				if (ctn2>=20):
					filtro=filtro/20.0;
					
					filtro=(filtro*138.0*4.0)/1000.0;  #244
					filtro=(1000.0/filtro);
					hz=filtro;
					rpm=filtro*60*0.25;				
					filtro=0;
					ctn2=0;
				if (ctn3>=300):
					filtro2=filtro2/300;
					filtro2=(filtro2*138.0*4.0)/1000.0;  #244
					filtro2=(1000.0/filtro2);
					hz2=filtro2;
					rpm2=filtro2*60*0.25;				
					filtro2=0;
					ctn3=0;
					print (hz2*60)/4
				ctn=0;
				flag_p=0;
				
		

				
def sms(tmr):
	
		
			
def main():
	thread.start_new_thread(vel,(0.2,));
	ventana.mainloop()	

main();




