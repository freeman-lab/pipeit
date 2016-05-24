class Pipeline(object):

    def __init__(self):
        self._data = None

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def source(self, func):
        def wrapper(**kwargs):
           self._data = func(**kwargs)
           if self._data is None:
                raise ValueError("a pipe function must return something")
           return self
        self[func.__name__] = wrapper

    def pipe(self, func):
        check_input(func)
        def wrapper(**kwargs):
            self._data = func(data=self._data, **kwargs)
            if self._data is None:
                raise ValueError("a pipe function must return something")
            return self
        self[func.__name__] = wrapper

    def sink(self, func):
        check_input(func)
        def wrapper(**kwargs):
            output = func(data=self._data, **kwargs)
            if output is not None:
                return output
        self[func.__name__] = wrapper

    @property
    def data(self):
        return self._data
    

def check_input(func):
    if func.func_code.co_argcount == 0:
        raise ValueError("a pipe function must have an 'data' argument")
    if not 'data' in func.func_code.co_varnames:
        raise ValueError("a pipe function must have an 'data' argument")

    