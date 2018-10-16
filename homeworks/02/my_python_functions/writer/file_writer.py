import os
import pickle as pkl

class FileWriter:
    
    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            self.path_ = path
            self.file = None
        else:
            raise Exception("Wrong path!")
        
    def _check_path(self, path):
        return os.path.exists(os.path.dirname(path))

    @property
    def path(self):
        return self.path_

    @path.setter
    def path(self,path):
        if self._check_path(path):
            self.path_ = path
        else:
            raise Exception("Wrong path!")

    @path.getter
    def path(self):
        return self.path_

    @path.deleter
    def path(self):
        self.path_ = None

    def print_file(self):
        with open(self.path, 'r') as f:
            print(f.read())
    
    def write(self, some_string):
        if self.file is not None:
            self.file.write(some_string)

    def __enter__(self):
        self.file = open(self.path, 'a')
        return self

    def __exit__(self,type,value,traceback):
        self.file.close()
        self.file = None
    
    def save_yourself(self, file_name):
        if self._check_path(file_name):
            with open(file_name,'wb') as f:
                pkl.dump(self,f)
    
    @classmethod
    def load_file_writer(cls, pickle_file):
        if cls._check_path(cls,pickle_file):
            with open(pickle_file,'rb') as f:
                return pkl.load(f)

    # 
    # возможно что то еще.
    # что намеренно упущенно. например что то для контекстного менеджера.
