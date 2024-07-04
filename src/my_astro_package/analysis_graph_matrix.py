from pathlib2 import Path
import pandas as pd
from .df_create import create_df_for_dataset_type 
from .find_area import find_count_area
from .build_chart import build_graph
from .save_chart import save_graph
from .calculate_matrix import calculate_fire_matrix_from_binary_images
from .build_mat import build_matrix
from .save_mat import save_matrix
import pandas as pd
from pathlib import Path

def analysis(data_path, save_path):
    """Анализирует данные, строит графики, матрицу и сохраняет результаты.

    Args:
        data_path (Path): Путь к директории с данными.
        save_path (Path): Путь к директории для сохранения результатов.

    Returns:
        pd.DataFrame: DataFrame с результатами.
    """
    all = []
    regions_count = []

    for dataset_path in Path(data_path).iterdir():
        dataset_type = dataset_path.name
        df = create_df_for_dataset_type(data_path, dataset_type)
        df_areas = find_count_area(df, dataset_type)
        fire_matrix = calculate_fire_matrix_from_binary_images(df)

        fig_graph = build_graph(dataset_type, df_areas)
        save_graph(fig_graph, dataset_type, save_path)

        fig_matrix = build_matrix(dataset_type, fire_matrix)
        save_matrix(fig_matrix, dataset_type, save_path)

        df_areas['video'] = dataset_type
        df_areas['time'] = df_areas['image_index'] / 120
        all.append(df_areas)
    df_areas = pd.concat(all, ignore_index=True)
    df_areas.to_excel(save_path / 'graphs2.xlsx', index=True)
    return df_areas

