from pathlib2 import Path
from .find_files import find_png_files
from .df_create import create_df_for_dataset_type 
from .find_area import find_count_area
from .build_chart import build_graph
from .save_chart import save_graph
from .calculate_matrix import calculate_fire_matrix_from_binary_images
from .build_mat import build_matrix
from .save_mat import save_matrix

def analysis(data_path, save_path):
    """Анализирует изображения, создает графики и тепловые карты активности астроцитов.

    Args:
        data_path (str): Путь к каталогу с изображениями.
        save_path (str): Путь к каталогу для сохранения результатов.
        types_images_events (str, optional): Тип событий, которые следует учитывать ("events" или "images"). По умолчанию "events".

    Returns:
        None
    """
    for dataset_path in Path(data_path).iterdir():
        dataset_type = dataset_path.name  
        df = create_df_for_dataset_type(data_path, dataset_type)  
        df_areas = find_count_area(df, dataset_type)  
        fire_matrix = calculate_fire_matrix_from_binary_images(df)  

        fig_graph = build_graph(dataset_type, df_areas)  
        save_graph(fig_graph, dataset_type, save_path)  

        fig_matrix = build_matrix(dataset_type, fire_matrix) 
        save_matrix(fig_matrix, dataset_type, save_path)  
