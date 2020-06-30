class Config:  
    def __init__(self):
        self.confname = 'My Name is Used, Conf Used'
      
    def __new__(cls):
        if not hasattr(cls, '_config'):
            cls._config = super(Config, cls).__new__(cls)
            print('\nConfiguration Loaded - Once and For All')

        else:
            print('\nConfiguration Already Loaded - Config Class Already instantiated')
        return cls._config


config_1 = Config()
print (config_1.confname)

config_2 = Config()
print (config_2.confname)

print('\n')

config_1.confname = "My Name is Lict, Conf Lict"
print ('CONF 1 : ' + config_1.confname)
print ('CONF 2 : ' + config_2.confname)
