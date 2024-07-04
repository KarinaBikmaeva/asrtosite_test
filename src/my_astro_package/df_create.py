import cv2
import pandas as pd
from tqdm import tqdm
from pathlib2 import Path
import glob

def create_df_for_dataset_type(data_path,dataset_type):
    """Создает датафрейм Pandas с метаданными для изображений в указанном каталоге.

    Args:
        data_path (str): Путь к каталогу с изображениями.
        dataset_type (str): Имя папки с изображениями.

    Returns:
        pandas.DataFrame: Датафрейм с метаданными для изображений.
    """
    events_mask =  str(data_path / dataset_type / '**' / '*.png')
    file_names = glob.glob(events_mask)
   
    data = []
    for file_path in tqdm(file_names):
        file_path = Path(file_path)
        name = file_path.stem
        name_parts, frame_id = name.split('_t')
        image_name = str(file_path.relative_to(data_path))
        status = file_path.parents[0].stem
        image = cv2.imread(str(file_path))
        data_size= image.shape
        data = ([image_name, 
                name, 
                dataset_type, 
                data_size, 
                str(file_path), 
                status, 
                int(frame_id)])
        data.append

    columns = ['image_name', 
               'name', 
               'dataset_type', 
               'data_size', 
               'file_path', 
               'status', 
               'frame_id']
    df = pd.DataFrame(data, columns=columns)
    return df.sort_values(by = 'frame_id')