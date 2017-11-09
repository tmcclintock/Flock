from abc import ABCMeta, abstractproperty


class BaseDatabaseSetup(metaclass=ABCMeta):

    @abstractproperty
    def name(self):
        return None

    @abstractproperty
    def server(self):
        return None

    @abstractproperty
    def parameters(self):
        return None


class DatabaseSetup(object):

    def __init__(self, name, server, parameters):
        self.name = name
        self.server = server
        self.parameters = parameters
