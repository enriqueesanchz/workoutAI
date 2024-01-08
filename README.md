# Workout excercises classification with AI
**Repositorio para el Proyecto 2 de la asignatura Aplicaciones IoT de 2º del Máster Universitario en Ingeniería de Telecomunicaciones de la Universidad de Sevilla**
Clasificacion de los siguientes ejercicios de gimnasio:
- Press Militar
- Bíceps Martillo
- Press Sentado
- Bíceps Unilateral
- Remo Bajo
- Jalón al Pecho
- Tríceps Polea
- Jalón Unilateral
- Tríceps Unilateral
- Press Inclinado

### Estructura de ficheros:
- El script para la toma de datos se encuentra en data/sample_data.py
- Los datos se encuentran en la carpeta data/csv
- Correspondientes al metodo 1 referenciado en la presentación, son los ficheros notebooks/walk.ipynb y notebooks/walk_dense.ipynb. El primero de ellos corresponde al original y el segundo a la versión final con accuracy más alta para este método.
- Correspondiente al método 2 referenciado en la presentación, el fichero notebooks/preprocess_info.ipynb explica distintos métodos para preprocesar los datos. El fichero notebooks/preprocess_and_train.ipynb preprocesa los datos con el método más preciso y entrena la red, alcanzando un accuracy del 0.99. Este último notebook es el entregado para el trabajo de la asignatura.
