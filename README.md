




# Описание кода

## Введение
Данный код представляет собой набор функций для анализа изображений астроцитов. Он содержит функции для создания датафрейма из изображений, подсчета количества областей на изображениях, построения графиков зависимости количества областей от времени и создания матрицы огня из бинарных изображений.

## Импорт библиотек
```
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import random
import pathlib
from pathlib2 import Path
import glob
```

## Функции

### find_png_files
```
def find_png_files(data_path):
events_mask = data_path / '*'
file_names = glob.glob(str(events_mask))
return file_names
```
Функция находит все файлы с расширением .png в указанной папке и возвращает список этих файлов.

### create_df_for_dataset_type
```
def create_df_for_dataset_type(data_path, dataset_type):
events_mask = str(data_path / dataset_type / '**' / '*.png')
file_names = glob.glob(events_mask)

data = []
for file_path in tqdm(file_names):
file_path = Path(file_path)
name = file_path.stem
name_parts, frame_id = name.split('_t')
image_name = str(file_path.relative_to(data_path))
status = file_path.parents[0].stem
image = cv2.imread(str(file_path))
data_size = image.shape
data.append([image_name, name, dataset_type, data_size, str(file_path), status, int(frame_id)])

columns = ['image_name', 'name', 'dataset_type', 'data_size', 'file_path', 'status', 'frame_id']
df = pd.DataFrame(data, columns=columns)
return df.sort_values(by = 'frame_id')
```
Функция создает датафрейм для указанного типа набора данных (папки). Она находит все файлы с расширением .png в указанной папке и создает записи в датафрейме для каждого изображения. Записи включают информацию о имени, типе набора данных, размере изображения и пути к файлу.

### find_count_area
```
def find_count_area(df, dataset_type, types_images_events="events"):
df_type = df[df['status'] == types_images_events]
regions_count = []

for index, row in df_type.iterrows():

image_path = row['file_path']
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
image_array = np.array(image)
_, thresh = cv2.threshold(image_array, 175, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
regions_count.append(len(contours))

df_areas = pd.DataFrame({
'video': dataset_type,
'image_index': df_type['frame_id'],
'area': regions_count
})

return df_areas
```
Функция подсчитывает количество областей на каждом изображении в указанном типе набора данных. Для этого она использует алгоритм пороговой фильтрации для преобразования изображения в бинарное и находит контуры на полученном изображении. После подсчета количество контуров записывается в датафрейм.

### build_graph
```
def build_graph(dataset_type, df_areas):
folder_name = Path(dataset_type).name
fig = plt.figure(figsize=(7.27, 3.56), dpi=300)
time = df_areas['image_index'] / 120
areas = df_areas['area']

x_min, x_max = time.min(), time.max()
plt.plot(time, areas, color='#D87093', linewidth=2)
plt.xlabel(f'Время, мин.')
plt.ylabel('Количество областей')
plt.title(f'Количество областей в зависимости от времени \n {folder_name}')
plt.xlim(x_min, x_max)
plt.show()
return fig
```
Функция строит график зависимости количества областей от времени для указанного типа набора данных. На графике отображается количество областей на оси y и время в минутах на оси x.

### save_graph
```
def save_graph(fig, dataset_type, save_path):
folder_name = Path(dataset_type).name
fig.savefig(f"{save_path}/{folder_name}.png", format='png')
fig.savefig(f"{save_path}/{folder_name}.svg", format='svg')
plt.close(fig)
```
Функция сохраняет график как файл PNG и SVG.

### calculate_fire_matrix_from_binary_images
```
def calculate_fire_matrix_from_binary_images(df, types_images_events="events"):
df_type = df[df['status'] == types_images_events]
images_array = []
for index, row in df_type.iterrows():
image_path = row['file_path']
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
image_array = np.array(image)
images_array.append(image_array)
fire_matrix = np.zeros_like(images_array[0])
for image in images_array:
fire_matrix = np.maximum(fire_matrix, image)
return fire_matrix
```
Функция создает матрицу огня по бинарным изображениям. Она находит все изображения для указанного типа набора данных, каждое изображение преобразует в массив и объединяет полученные массивы в результирующую матрицу.

### build_matrix
```
def build_matrix(dataset_type, fire_matrix):
folder_name = Path(dataset_type).name
fig, ax = plt.subplots(figsize=(7.27, 3.56), dpi=300)
print(f'Fire Matrix for {folder_name}')
ax.imshow(fire_matrix, cmap='gray')
ax.axis('off')

rows, cols = fire_matrix.shape
border_color = 'black'
border_width = 2
rect = patches.Rectangle((0, 0), cols-1, rows-1, linewidth=border_width, edgecolor=border_color, facecolor='none')
ax.add_patch(rect)

scalebar = ScaleBar(dx = 0.196,units = "um",location='lower right', scale_loc="top", border_pad=0.2,sep=1, length_fraction = 0.3)
ax.add_artist(scalebar)
plt.show()
return fig
```
Функция строит изображение матрицы огня для указанного типа набора данных. На изображении отображается матрица огня и добавляется шкала для измерения размеров.

### save_matrix
```
def save_matrix(fig, dataset_type, save_path):
folder_name = Path(dataset_type).name
fig.savefig(f"{save_path}/{folder_name}.png", format='png')
fig.savefig(f"{save_path}/{folder_name}.svg", format='svg')
plt.close(fig)
```
Функция сохраняет изображение матрицы огня как файл PNG и SVG.

### analysis
```
def analysis(data_path, save_path, types_images_events="events"):
for dataset_path in Path(data_path).iterdir():
dataset_type = dataset_path.name
df = create_df_for_dataset_type(data_path, dataset_type)
df_areas = find_count_area(df, dataset_type, types_images_events=types_images_events)
fire_matrix = calculate_fire_matrix_from_binary_images(df, 'events')

fig_graph = build_graph(dataset_type, df_areas)
save_graph(fig_graph, dataset_type, save_path)

fig_matrix = build_matrix(dataset_type, fire_matrix)
save_matrix(fig_matrix, dataset_type, save_path)
```
Функция анализирует все папки в указанном пути данных. Для каждой папки она создает датафрейм, подсчитывает количество областей, строит график зависимости количества областей от времени и создает изображение матрицы огня. График и изображение сохраняются.

### create_result_dataframe
```
def create_result_dataframe(data_path, dataset_type, types_images_events="events"):
regions_count = []
all = []
for dataset_path in Path(data_path).iterdir():
dataset_type = dataset_path.name
df = create_df_for_dataset_type(data_path, dataset_type)
df_areas = find_count_area(df, dataset_type, types_images_events=types_images_events)
regions_count = df_areas['image_index']

df_areas['frame_id'] = df['frame_id']
time = df_areas['frame_id'] / 120

df_areas = pd.DataFrame({
'video': dataset_type,
'time': time,
'area': regions_count
})
all.append(df_areas)
df_areas = pd.concat(all, ignore_index=True)
df_areas.to_excel(f'C:\\Users\\HP\\Documents\\scientific_programming\\astro\\graphs2.xlsx', index=True)

return df_areas
```
Функция создает датафрейм с результатами анализа для всех папок в указанном пути данных. Для каждой папки она создает датафрейм с информацией о времени, количестве областей и путях к файлам и сохраняет его в формате Excel.

## Использование кода
Файл `data_path` содержит путь к папке с данными. Путь `save_path` указывается для сохранения графиков и матриц огня.

Пример использования кода:
```
data_path = Path('C:/Users/HP/Documents/scientific_programming/astro/Task_Astrocytes')
save_path = Path(r'C:\Users\HP\Documents\scientific_programming\astro\graphs2')

analysis(data_path, save_path, 'events')
create_result_dataframe(data_path, dataset_type,"events")
```
