from pathlib2 import Path
import pandas as pd
from .df_create import create_df_for_dataset_type
from .find_area import find_count_area 

def create_result_dataframe(data_path, save_path):
    """Создает DataFrame с результатами анализа и сохраняет его в Excel.

    Args:
        data_path (str): Путь к директории с данными.
        save_path (str, optional): Путь к файлу для сохранения результата. 
                                        Defaults to 'graphs2.xlsx'.

    Returns:
        pd.DataFrame: DataFrame с результатами.
    """
    regions_count = []
    all = []

    for dataset_path in Path(data_path).iterdir():
        dataset_type = dataset_path.name
        df = create_df_for_dataset_type(data_path, dataset_type)
        df_areas = find_count_area(df, dataset_type)
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
    df_areas.to_excel(save_path, index=True)
    return df_areas