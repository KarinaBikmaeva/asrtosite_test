### Описание

`my_astro_package` - это пакет Python, предоставляющий инструменты для анализа изображений астроцитов.

### Установка

Чтобы установить пакет `my_astro_package` из GitHub и начать его использовать, следуйте данной инструкции:

1. **Скачивание пакета:**

   Загрузите пакет `my_astro_package` с GitHub (скачайте zip-архив).

2. **Распаковка архива:**

   Распакуйте скачанный архив в любую удобную директорию на вашем компьютере.

3. **Установка пакета в режиме разработки:**

   Откройте командную строку (или терминал) и перейдите в директорию, куда вы распаковали архив. Затем выполните команду:

   ```
   pip install -e .
   ```
**Использование:**

1. **Импорт функций:**

   ```python
   from my_astro_package import find_png_files
   from my_astro_package import create_df_for_dataset_type
   from my_astro_package import find_count_area
   from my_astro_package import build_graph
   from my_astro_package import save_graph
   from my_astro_package import calculate_fire_matrix_from_binary_images
   from my_astro_package import build_matrix
   from my_astro_package import save_matrix
   from my_astro_package import analysis
   from my_astro_package import create_result_dataframe
   ```
2. **Инициализация путей:**

   ```python
   from pathlib2 import Path
   data_path = Path('C:/Users/HP/Desktop/Task_Astrocytes')
   save_path = = Path('C:/Users/HP/Desktop/graph')

3. **Анализ графика и матрицы:**
 При вызове данной функции:
   *  создается DataFrame (таблицу данных), извлекающую информацию об астроцитах из изображений.
   *  вычисляет матрицу событий.Эта матрица представляет собой двумерный массив, где каждый элемент указывает на наличие или отсутствие кальциевых событий астроцитов в определенном месте изображения. В аргументах используется 'events', так как именно в этой папке можно проследить кальциевую активность астроцитов. А также вывод изображения на основе этой матрицы.
   *  создает график "количество областей на кадре в зависимости от времени".
   *  сохраняет график в файл.

   ```python
   from my_astro_package import analysis

   data_path = Path('C:/Users/HP/Desktop/Task_Astrocytes')
   save_path = Path(r'C:\Users\HP\Desktop\graphs2') 
   analysis(data_path, save_path, 'events')
   ```

**Для получения документации по указанному модулю, классу, функции, переменным можно использовать функцию help()**

![2024-07-03_16-26-06](https://github.com/KarinaBikmaeva/astrosite_test/assets/171484912/22584ef6-840f-4884-ac0c-ec099ef32aa8)

**Примеры вывода графиков и изображений:**

![2024-07-03_16-26-26](https://github.com/KarinaBikmaeva/astrosite_test/assets/171484912/13cf5376-1db3-49a4-ae10-92cf4ba7bca9)

![2024-07-03_16-27-06](https://github.com/KarinaBikmaeva/astrosite_test/assets/171484912/7df03d2b-46ee-48e4-9fa4-3d9f6a0ed005)

