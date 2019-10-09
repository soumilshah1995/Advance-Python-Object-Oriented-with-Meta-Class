__Author__ = 'Soumil Nitin Shah'
__Email__ = 'shahsoumil519@gmail.com'

try:

    import datetime
    import os
    import sys
    import logging

except Exception as e:

    print("Some Modules are Missing {}".format(e))


class Meta(type):

    """ Metaclass  """

    def __call__(cls, *args, **kwargs):
        instance = super(Meta, cls).__call__(*args, **kwargs)
        return instance

    def __init__(cls, name, base, attr):
        super(Meta, cls).__init__(name, base, attr)


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


class Test(metaclass=Meta):

    def __init__(self, *args, **kwargs):
        pass

    @log
    def methodA():
        print("Method A")
        return "1111"


if __name__ == "__main__":
    obj = Test()
    obj.methodA()
