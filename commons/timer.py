from __future__ import print_function
import numpy as np
import time
import platform
# pyver = platform.python_version()


def timer_dec(original_function):
    '''
    Use as a decorator i.e @timer_dec before a function
    :param original_function:
    :return:
    '''
    ENABLE = True
    def new_function(*args, **kwargs):
        ts = time.time()
        res = original_function(*args, **kwargs)
        te = time.time()
        if ENABLE:
            elapsed = te - ts
            # hms = '{:02.0f}:{:02.0f}:{:.2f}'.format(divmod(elapsed, 60*60)[0], *divmod(elapsed, 60))
            hms = '{:02.0f}:{:06.3f}'.format(*divmod(elapsed, 60))
            print(original_function.__name__ + ", run time:       {}".format(hms))
        return res
    return new_function




def timeme(fun, n, msg=''):
    '''
    Use to time a function. i.e Timeme(my function, 2, 'hello') will show average time of 2 runs.
    '''
    t = time.time()
    for i in range(n):
        fun()
    print(msg + ' - ' 'average time {} runs: {:.3f} seconds'.format(n, (time.time() - t) / n))


def nprint(m, sign='-', precision=3, max_line_width=1000, separator=' '):
    xx = np.array2string(m, sign=sign, precision=precision, max_line_width=max_line_width, separator=separator) # formatter={'float_kind': lambda x: "%4.4f" % x}
    print(xx)

def fprint(s='', v=None, precision=6):
    def truncate(number, position):
        '''Return number with dropped decimal places past specified position.'''
        return number - number % (10 ** -position)
    print(s + ' ' + '{:2.5f}'.format(truncate(v, precision)))


class Timer:
    '''
    Use to print the "msg" then run the block and when it ends it'll write "done" and the time it has taken to complete
    For example:
    with timer('started my function'):
        my_func()
    '''
    def __init__(self, msg=''):
        self.msg = msg
        print(self.msg + '... ', end='')

    def __enter__(self):
        self.entime = time.time()
    def __exit__(self, *args):
        elapsed = time.time() - self.entime
        hms = '{:02.0f}:{:06.3f}'.format(*divmod(elapsed, 60))
        print('done {}.'.format(self.msg) + ' ' + "run time:       {}".format(hms))