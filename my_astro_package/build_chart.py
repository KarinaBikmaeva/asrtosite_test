import matplotlib.pyplot as plt
from pathlib2 import Path
def build_graph(dataset_type, df_areas):    
    folder_name = Path(dataset_type).name
    fig = plt.figure(figsize=(7.27, 3.56), dpi = 300)
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