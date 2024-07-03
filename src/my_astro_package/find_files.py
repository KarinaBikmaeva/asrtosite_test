import glob 
def find_png_files(data_path):
    """Возвращает список путей к PNG-файлам в указанном каталоге.

    Args:
        data_path (str): Путь к каталогу с изображениями.

    Returns:
        list: Список путей к PNG-файлам.
    """
    events_mask = data_path / '*'
    file_names = glob.glob(str(events_mask))
    return file_names