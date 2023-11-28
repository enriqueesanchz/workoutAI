import threading
import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fs = 20 # Hz
data = []
is_running = True  # Bandera para controlar la ejecución del hilo de generación de datos

def generate_data(fs):
    while is_running:
        new_data = random.randint(0, 100)
        data.append(new_data)
        time.sleep(1/fs)

def update_plot(frame):
    plt.clf()
    plt.plot(data[-100:])
    plt.title('Cambios en los datos en tiempo real')
    plt.xlabel('Muestras')
    plt.ylabel('Valor')

# Crear e iniciar el hilo de generación de datos
generate_thread = threading.Thread(target=generate_data, args=(fs,))
generate_thread.start()

# Configurar la animación en el hilo principal
animation = FuncAnimation(plt.gcf(), update_plot, interval=200,
                            cache_frame_data=True, save_count=100)  # Intervalo en milisegundos

# Mostrar la ventana del gráfico
plt.show()

# Esperar a que el hilo de generación de datos se ejecute por un tiempo (por ejemplo, 10 segundos)
time.sleep(10)

# Detener el hilo de generación de datos
is_running = False

# Esperar a que el hilo de generación de datos termine
generate_thread.join()

# Detener la animación
animation.event_source.stop()

# Cerrar la ventana del gráfico
plt.close()
