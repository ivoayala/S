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
	global act, velocidad, apagado, pid;
	
	if (opcion==0):

		apagado=1;
		hz=0;
	if (opcion==1):

		apagado=0;
	
def Btn_mtr_on():
	enviar(1); 
	
def Btn_mtr_off():
	enviar(0); 
	
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
				
		v=velocidad.get();
		v=float(v);
					#print v
		if (v>rpm):
			if ((v-rpm)>100):
				dif=((v-rpm)/2000.00)*0.005
				control=control+dif;
			if ((v-rpm)<100):
				dif=((v-rpm)/2000.00)*0.00001
				control=control+dif;
		if (v<rpm):
			if ((rpm-v)>100):
				dif=((rpm-v)/2000.00)*0.005
				control=control-dif;
			if ((rpm-v)<100):
				dif=((rpm-v)/2000.00)*0.00001
				control=control-dif;
		if (control>=100):
			control=100;
		if (control<=0):
			control=0;
		pid=100.00-control;
		#print pid
		if (apagado==0):
			
			act.ChangeDutyCycle(pid);
		if (apagado==1):
			pid=0;
			act.ChangeDutyCycle(100);
			hz=0;
		

				
def sms(tmr):
	global rpm, hz;	
	ctn=0;
	datog= np.array([0]*200);
	while 1:
		datog[ctn]=(hz*60)/4;
		tam=len(datog);
		line.set_data(range(0,tam), datog)
		fig.canvas.draw()
		ctn=ctn+1;
		if (ctn>199):
			ctn=0;
			datog= np.array([0]*200);
		time.sleep(0.5);	
		
			
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



