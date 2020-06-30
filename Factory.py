import os
import pandas as pd

class Loader():

    def __init__(self):
        self.filename = 'None'

    def load(self, data):
        self.filename, format = os.path.splitext(data)

        if format == '.csv':
            __loader = self._load_csv

        elif format == '.xlsx':
            __loader = self._load_xlsx

        else:
            print(format)
            raise ValueError(format)
        return __loader(data)
  
    def _load_csv(self, data):
        print ('\nLOADING CSV READER for ' + data)
        #return pd.read_csv(data)

    def _load_xlsx(self, data):
        print ('\nLOADING XL READER for ' + data)
        #return pd.read_excel(data)
  
loader = Loader()

loader.load('myfile.csv')
# pd.DataFrame 

loader.load('myfile.xlsx')
#pd.DataFrame



