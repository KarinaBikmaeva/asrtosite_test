from pathlib2 import Path 
import find_area 
import df_create 
import calculate_matrix 
import build_chart 
import save_chart 
import build_mat 
import save_mat 
def analysis(data_path, save_path, types_images_events="events"): 
  
    for dataset_path in Path(data_path).iterdir(): 
        dataset_type = dataset_path.name  # Имя папки как dataset_type 
        df = df_create.create_df_for_dataset_type(data_path, dataset_type) 
        df_areas = find_area.find_count_area(df, dataset_type, types_images_events=types_images_events) 
        fire_matrix =  calculate_matrix.calculate_fire_matrix_from_binary_images(df, 'events') 
 
         
        fig_graph = build_chart.build_graph(dataset_type, df_areas) 
        save_chart.save_graph(fig_graph, dataset_type, save_path) 
 
        fig_matrix = build_mat.build_matrix(dataset_type, fire_matrix) 
        save_mat.save_matrix(fig_matrix, dataset_type, save_path)
