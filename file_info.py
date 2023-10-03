# Путь к директории, которую мы хотим сканировать
# directory_to_scan = 'my_directory'
# Сохранение информации в JSON
# save_file_info_to_json(directory_to_scan, 'file_info.json')
# Сохранение информации в CSV
# save_file_info_to_csv(directory_to_scan, 'file_info.csv')
# Сохранение информации в Pickle
# save_file_info_to_pickle(directory_to_scan, 'file_info.pickle')


import os

class FileInfo:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.is_dir = os.path.isdir(path)
        self.size = self._calculate_size()

    def _calculate_size(self):
        if self.is_dir:
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(self.path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(filepath)
            return total_size
        else:
            return os.path.getsize(self.path)

    def to_dict(self):
        return {
            "path": self.path,
            "name": self.name,
            "is_dir": self.is_dir,
            "size": self.size
        }