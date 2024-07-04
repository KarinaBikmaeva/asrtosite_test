
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
from pathlib2 import Path

def build_matrix(dataset_type, fire_matrix):
    """Создает тепловую карту активности астроцитов.

    Args:
        dataset_type (str): Имя папки с изображениями.
        fire_matrix (numpy.ndarray): Матрица активности астроцитов.

    Returns:
        matplotlib.figure.Figure: Тепловая карта.
    """
    folder_name = Path(dataset_type).name
    fig, ax = plt.subplots(figsize=(7.27, 3.56), dpi=300)
    print(f'Fire Matrix for {folder_name}')
    ax.imshow(fire_matrix, cmap='gray') 
    ax.axis('off')
    # Добавление рамки
    rows, cols = fire_matrix.shape
    border_color = 'black'  
    border_width = 2     
    rect = patches.Rectangle((0, 0), cols-1, rows-1, linewidth=border_width, edgecolor=border_color, facecolor='none')
    ax.add_patch(rect)
    # Шкала
    scalebar = ScaleBar(dx=0.196, units="um", location='lower right', scale_loc="top", border_pad=0.2, sep=1, length_fraction=0.3)
    ax.add_artist(scalebar)
    plt.show()
    return fig