from estanistml import var, env, Symbol, parse, eval, lex
from estanistml.runtime import h

run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, op = map(Symbol, 'x y a b c f g op'.split())



class TestGrammar:
    def test_simple_example(self):
        src = 'x = 42;'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['define', x, 42]]

    def test_simple_example2(self):
        src = 'x = h1 "bar";'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['define', x, ["html", "h1", {}, ["bar"]]]] 

    def test_simple_example3(self):
        src = 'macro f(x) {42}'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['macro', f, [x], 42]] 

        #aux = parse('macro joao (obj) { div (class=\"foo\" id=\"bar\"0) }')
        #aux = parse('import {joao} from joao')
        #print (aux.pretty())
        #assert aux == ["macro", "joao","obj","div","class","foo", "id" , "bar"]


class TestRuntime:
    def test_define_html(self):
        env = {}
        eval(parse('x = h1 "hello";'), env)
        print(env)
        assert env[x] == h('h1', {}, ['hello'])

def pretty(x):
    try:
        return x.pretty()
    except AttributeError:
        return str(x)