import abc

class AbstractFactory(metaclass=abc.ABCMeta):

    def getType(self):
        print('\nI AM A FACTORY')

    @abc.abstractmethod
    def getSpecificType(self):
        pass

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):

    def getSpecificType(self):
        print('I PRODUCE OUTFITS')

    def create_product_a(self):
        return 'Making Shoes'

    def create_product_b(self):
        return 'Making Jeans'


class ConcreteFactory2(AbstractFactory):

    def getSpecificType(self):
        print('I PRODUCE AUTOMOTIVE')

    def create_product_a(self):
        return 'Making Cars'

    def create_product_b(self):
        return 'Making Trucks'


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        print('\n')
        print(type(factory).__bases__)
        factory.getType()
        factory.getSpecificType()
        print (factory.create_product_a())
        print (factory.create_product_b())


if __name__ == "__main__":
    main()
