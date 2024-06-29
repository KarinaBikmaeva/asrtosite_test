import glob 
def find_png_files(data_path):
    events_mask = data_path / '*'
    file_names = glob.glob(str(events_mask))
    return file_names