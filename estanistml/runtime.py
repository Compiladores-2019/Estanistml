import math
import operator as op
from collections import ChainMap
from types import MappingProxyType
from .symbol import Symbol
from hyperpython import h

def eval(x, env=None):
    """
    Avalia expressão no ambiente de execução dado.
    """
    
    # Cria ambiente padrão, caso o usuário não passe o argumento opcional "env"
    if env is None:
        env = ChainMap({}, global_env)
    
    # Avalia tipos atômicos
    if isinstance(x, Symbol):
        return env[x]
        
    elif isinstance(x, (int, float, bool, str)):
        return x

    # Avalia formas especiais e listas
    head, *args = x
    
    # Comando (if <test> <then> <other>)
    # Ex: (if (even? x) (quotient x 2) x)
    if head == Symbol.IF:
        return NotImplemented
    
    #import submule from module
    # return ['import', args, str(str(name))]
    # imp : "import" "{" args "}" "from" name
    
    elif head == 'import':
    
        submodulos, modulo = args
        a =__import__(modulo)
        print(a)
        aux ={}
        for sub in submodulos:
           result = {str(sub): getattr(a,str(sub))}
           aux.update(result)
        env[modulo] = aux
        return aux
    
    # Módulo module
    elif head == 'module':
        for cmd in args:
            eval(cmd, env)
        return None 
        
    # Comando x = 42;
    elif head == 'define':
        name, value = args
        env[name] = eval(value, env)
        return value

    # Comando html;
    elif head == 'html':
        tag, attrs, children = args
        attrs = {str(k): eval(v, env) for k, v in attrs.items()}
        children = [eval(x, env) for x in children]
        a = h(tag, attrs, children)
        return a
    
    # comando macro
    elif head == 'macro':
        tag, argumentos, expr = args
        
        def macro(*args):
            vars = dict(zip(argumentos, args))
            local_env = ChainMap(vars, env)
            return eval(expr, local_env)
        
        env[tag] = macro
        return macro

    else:
       return NotImplemented

def env(*args, **kwargs):

    kwargs = {Symbol(k): v for k, v in kwargs.items()}
    if len(args) > 1:
        raise TypeError('accepts zero or one positional arguments')
    elif len(args):
        if any(not isinstance(x, Symbol) for x in args[0]):
            raise ValueError('keys in a environment must be Symbols')
        args[0].update(kwargs)
        return ChainMap(args[0], global_env)
    return ChainMap(kwargs, global_env)


def _make_global_env():

    dic = {
        **vars(math), # sin, cos, sqrt, pi, ...
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'begin':   lambda *x: x[-1],
        'car':     lambda x: head,
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'expt':    pow,
        'equal?':  op.eq,
        'even?':   lambda x: x % 2 == 0,
        'length':  len, 
        'list':    lambda *x: list(x), 
        'list?':   lambda x: isinstance(x, list), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, (float, int)),  
		'odd?':   lambda x: x % 2 == 1,
        'print':   print,
        'procedure?': callable,
        'quotient': op.floordiv,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
    }
    return MappingProxyType({Symbol(k): v for k, v in dic.items()})

global_env = _make_global_env() 

