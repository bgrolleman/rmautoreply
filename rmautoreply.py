#!/usr/bin/env python3


def respond_to_communication():
    '''Be negative to all communications.

    >>> respond_to_communication()
    'No'

    '''
    return ('No')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
