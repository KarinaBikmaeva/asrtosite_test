
import matplotlib.pyplot as plt
from pathlib2 import Path
def save_graph(fig, dataset_type, save_path):
    folder_name = Path(dataset_type).name
    # Сохранение графика
    fig.savefig(f"{save_path}/{folder_name}.png", format='png')
    fig.savefig(f"{save_path}/{folder_name}.svg", format='svg')
    plt.close(fig)