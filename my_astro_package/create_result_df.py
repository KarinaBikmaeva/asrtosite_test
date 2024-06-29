import df_create
import find_area
from pathlib2 import Path
import pandas as pd

def create_result_dataframe(data_path, dataset_type, types_images_events="events"):
    """Создает датафрейм Pandas с результатами обработки изображений.

    Args:
        data_path (str): Путь к каталогу с изображениями.
        dataset_type (str): Имя папки с изображениями.
        types_images_events (str, optional): Тип событий, которые следует учитывать ("events" или "fire"). По умолчанию "events".

    Returns:
        pandas.DataFrame: Датафрейм с результатами обработки изображений.
    """
    regions_count = []
    all = []
    for dataset_path in Path(data_path).iterdir():
        dataset_type = dataset_path.name  # Имя папки как dataset_type
        df = df_create.create_df_for_dataset_type(data_path, dataset_type)
        df_areas = find_area.find_count_area(df, dataset_type, types_images_events=types_images_events)
        regions_count = df_areas['image_index'] 
        df_areas['frame_id'] = df['frame_id']
        time = df_areas['frame_id'] / 120
        df_areas = pd.DataFrame({
            'video': dataset_type,
            'time': time,
            'area': regions_count
        })
        all.append(df_areas)
    df_areas = pd.concat(all, ignore_index = True) 
    df_areas.to_excel(f'C:\\Users\\HP\\Documents\\scientific_programming\\astro\\graphs2.xlsx', index=True)
    return df_areas
