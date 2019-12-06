from estanistml import var, env, Symbol, parse, eval #, lex
from hyperpython import h

run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, op = map(Symbol, 'x y a b c f g op'.split())



class TestGrammar:
    def test_simple_define(self):
        src = 'x = 42;'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['define', x, 42]]

    def test_define_with_param(self):
        src = 'x = h1 (alexandre = 2) "bar";'
        tree = parse(src)
        print(pretty(tree))
        aux = {'alexandre': 2}
        assert parse(src) == ['module', ['define', x, ["html", "h1", aux , ["bar"]]]]

    def test_simple_define_without_param(self):
        src = 'x = h1 "bar";'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['define', x, ["html", "h1", {}, ["bar"]]]] 

    def test_simple_macro(self):
        src = 'macro f(x) {42}'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['macro', f, [x], 42]] 

    def test_full_define(self):
        src = 'x = h1 (alexandre = 2, mo = 1) "bar";'
        src2 = 'x = h1 (alexandre = 2, mo = 1, jao = 24, cristo = 13) "bar";'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['define', x, ["html", "h1", {'alexandre': 2, 'mo': 1}, ["bar"]]]]
        assert parse(src2) == ['module', ['define', x, ["html", "h1", {'alexandre': 2, 'mo': 1 ,'jao': 24, 'cristo': 13}, ["bar"]]]]

    def teste_import_simple(self):
        src = 'import {x} from title'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['import', [x], 'title']]

    def teste_import_full(self):
        src = 'import {x, y} from title'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['import', [x, y], 'title']]

class TestRuntime:
    def test_define_html(self):
        env = {}
        eval(parse('x = h1 "hello";'), env)
        print(env)
        assert env[x] == h('h1', {}, ['hello'])
    
    def teste_define_full_html(self):
        #aux = h('h1', {'class': 'foo', 'id':'bar'}, ['hello'])
        #print(aux)
        env = {}
        eval(parse('x = h1 (class="foo", id="bar") "hello";'), env)
        print(env)
        assert env[x] == h('h1', {'class':'foo','id':'bar'}, ['hello'])
    
 

def pretty(x):
    try:
        return x.pretty()
    except AttributeError:
        return str(x)