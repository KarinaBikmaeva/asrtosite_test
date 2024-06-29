import matplotlib.pyplot as plt
from pathlib2 import Path
def save_matrix(fig, dataset_type, save_path):
    """Сохраняет изображения, построение по матрице  в файл PNG и SVG.

    Args:
        fig (matplotlib.figure.Figure): Фигура тепловой карты.
        dataset_type (str): Имя папки с изображениями.
        save_path (str): Путь к каталогу для сохранения результатов.
    """
    folder_name = Path(dataset_type).name
    # Сохранение графика
    fig.savefig(f"{save_path}/{folder_name}.png", format='png')
    fig.savefig(f"{save_path}/{folder_name}.svg", format='svg')
    plt.close(fig)
