import cv2
import numpy as np


 
def calculate_fire_matrix_from_binary_images( df, types_images_events = "events"):
    """Рассчитывает матрицу активности астроцитов на основе бинарных изображений.

    Args:
        df (pandas.DataFrame): Датафрейм с данными для изображений.
        types_images_events (str, optional): Тип событий, которые следует учитывать ("events" или "images"). По умолчанию "events".

    Returns:
        numpy.ndarray: Матрица активности астроцитов.
    """
    df_type = df[df['status'] == types_images_events]
    images_array = []
    for index, row in df_type.iterrows():
        image_path = row['file_path']
        image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
        image_array = np.array(image)
        images_array.append(image_array)
    # Инициализировать матрицу нулями
    fire_matrix = np.zeros_like(images_array[0])
    for image in images_array: 
        # Объединить результирующую маску с fire_matrix
        fire_matrix = np.maximum(fire_matrix, image)
        
    return fire_matrix