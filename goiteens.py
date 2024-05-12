def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = 0
            for _ in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return -1