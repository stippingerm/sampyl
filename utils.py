import autograd.numpy as np
from autograd import grad
from itertools import count


def grad_logp(dlogp, x):
    """ dlogp should be a list of gradient logps, respective to each
        paramter in x
    """
    try:
        return np.array([each(*x) for each in dlogp])
    except TypeError:  # Happens when dlogp isn't iterable
        dlogp = [dlogp]
        return grad_logp(dlogp, x)


def default_start(start, logp):
    """ If start is None, return a zeros array with length equal to the number
        of arguments in logp
    """
    if start is None:
        default = np.ones(logp.__code__.co_argcount)
        return default
    else:
        return np.hstack([start])


def logp_var_names(logp):
    # Putting underscores after the names so that variables names don't
    # conflict with built in attributes
    names = logp.__code__.co_varnames[:logp.__code__.co_argcount]
    names = [each + "_" for each in names]
    return names
