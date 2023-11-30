import os
import threading
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from sense_hat import SenseHat

data = [[],[],[],[],[],[]]

def generate_data():
    ARCHIVO = "datos.csv" # nombre del archivo
    t = []
    t_sample = []
    t_ini = time.time()
    t_ant = t_ini
    sense = SenseHat()
    muestras = 100

    for _ in range(muestras):
        t_actual = time.time()
        acceleration = sense.get_accelerometer_raw()

        #datos de aceleración en Gs
        data[0].append(acceleration['x'])
        data[1].append(acceleration['y'])
        data[2].append(acceleration['z'])
        gyroscope = sense.get_gyroscope_raw()
        #datos de velocidad rad/s
        data[3].append(gyroscope['x'])
        data[4].append(gyroscope['y'])
        data[5].append(gyroscope['z'])

        t.append(t_actual-t_ini)
        t_sample.append(t_actual-t_ant)

        t_ant = t_actual

    datos_imu = pd.DataFrame(list(zip(t,data[0],data[1],data[2],data[3],data[4],data[5])),
                            columns =['t', 'accel_x','accel_y','accel_z','gyro_x','gyro_y','gyro_z'])

    intentos = 0
    while os.path.isfile(ARCHIVO):
        #En caso de que exista un fichero con dicho nombre, le pone un numero al final (consecutivo)
        print("El archivo", ARCHIVO, "ya existe")
        intentos += 1
        if intentos > 1:
            ARCHIVO = ARCHIVO[:-1]
        ARCHIVO = ARCHIVO+str(intentos)

    print("Se guardará el archivo con nombre: ", ARCHIVO)
    # Crea un archivo csv y guarda los datos
    datos_imu.to_csv(ARCHIVO, index=False)


def update_plot(frame):
    plt.clf()
    plt.plot(data[0][-100:])
    plt.plot(data[1][-100:])
    plt.plot(data[2][-100:])
    plt.title('Cambios en los datos en tiempo real')
    plt.xlabel('Muestras')
    plt.ylabel('Valor')

# Crear e iniciar el hilo de generación de datos
generate_thread = threading.Thread(target=generate_data)
generate_thread.start()

# Configurar la animación en el hilo principal
animation = FuncAnimation(plt.gcf(), update_plot, interval=200, 
                        cache_frame_data=True, save_count=100)  # Intervalo en milisegundos

# Mostrar la ventana del gráfico
plt.show()

# Esperar a que el hilo de generación de datos termine
generate_thread.join()

# Detener la animación
animation.event_source.stop()

# Cerrar la ventana del gráfico
plt.close()
