
try:
    import functools
    import datetime
    import os
    import sys
    import logging
    from abc import  ABC, ABCMeta,abstractmethod
except Exception as e:
    print("Some Modules are Missing {}".format(e))


class MetaClass(type):

    """ Meta class """

    _instance = {}

    def __call__(cls, *args, **kwargs):

        """ Implementing Singleton Design Pattern  """

        print("**kwargs", kwargs)

        name = kwargs.get("name", None)
        if not name.__str__:
            raise ValueError ("name should be string ")

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

    def __init__(cls, name, base, attr):

        """ Defining Your Own Rules  """

        if cls.__name__[0].isupper():

            """ Create class only if First Letter is Capital    """

            for k, v in attr.items():
                if hasattr(v, '__call__'):

                    if v.__name__[0] == '_' or v.__name__[0].islower():

                        """  check name function starts with _ or lower case  """

                        if v.__doc__ is None:

                            """  Check is User has provided Documentation """

                            raise ValueError("Make sure to Provide Documentation check {}".format(v.__name__))
                        else:

                            """ if function has Doccumentation pass """

                            pass
                    else:

                        """ function name starts with upper case throw error  """

                        raise ValueError("Function should start with Lower case :{}".format(v.__name__))
        else:
            raise ValueError("Class Name  should start with Capital Letter :{} ".format(cls.__name__[0]))

class log(object):

    """ Create a Log File regarding Execution Time memory Address size etc """

    def __init__(self, func):
        """ Constructor  """
        self.func = func

    def __call__(self, *args, **kwargs):
        """ Wrapper Function """

        start = datetime.datetime.now()     # start time
        Tem = self.func(*args, **kwargs)    # call Function
        FunName = self.func.__name__        # get Function Name
        end = datetime.datetime.now()       # End time

        message = """                       # Form Message
            
            Function : {}
            Execution Time : {}
            Address : {}
            Memory: {} Bytes
            Date: {}
            
            """.format(FunName,
                       end-start,
                       self.func.__name__,
                       sys.getsizeof(self.func),
                       start)

        cwd = os.getcwd()                       # get CWD
        folder = 'Logs'                         # Create Folder Logs
        newPath = os.path.join(cwd, folder)     # change Path

        try:
            """ try to create directory """
            os.mkdir(newPath)                   # create Folder

        except Exception as e:

            """ Directory already exists """

            logging.basicConfig(filename='{}/log.log'.format(newPath), level=logging.DEBUG)
            logging.debug(message)

        return Tem


class Test(metaclass=MetaClass):

    __slots__ = ["name"]            # Hacker wont be able to add elements at run time

    def __init__(self, name):

        """ Constructor """

        self.name = name
        super(Test, self).__init__()

    def method(self):

        """ Method """
        print("Hello World ")


if __name__ == "__main__":
    obj = Test(name="Soumil")
    print(obj)
