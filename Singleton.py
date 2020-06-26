class Config:  
    def __init__(self):
        self.confname = 'My Name is Used, Conf Used'
        pass
      
    def __new__(cls):  
        if not hasattr(cls, '_config'):  
            cls._config = super(Config, cls).__new__(cls)
            print('\nConfiguration Loaded - Once and For All')

        else:  
            print('\nConfiguration Already Loaded - Config Class Already instantiated')
        return cls._config


config_1 = Config()
print (config_1.confname)

##config_2 = Config()
##print (config_2.confname)

#config_2.confname = "My Name is Lict, Conf Lict"
#print (config_1.confname)
