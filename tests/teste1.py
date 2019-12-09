from estanistml import var, env, Symbol, parse, eval #, lex
from hyperpython import h
import estanistml.runtime

run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, op, alexandre, mo, jao, cristo, classe,ID= map(Symbol, 'x y a b c f g op alexandre mo jao cristo classe ID'.split())

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
        assert parse(src) == ['module', ['define', x, ["html", "h1", {alexandre: 2} , ["bar"]]]]

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


    def test_macro_full(self):
        src = 'macro op(x){ div(classe = "foo", ID = "bar") { h1 "title"} }'
        src1 = 'macro op(x){ div(classe = "foo", ID = "bar") { h1 (y = "ipslon") "title"} }'
        src2 = 'macro op(x){ div(classe = "foo", ID = "bar") { h1 "title" h2 "teste"} }'
        src3 = 'macro op(x){ div(classe = "foo", ID = "bar") { h1 (y = "ipslon", c = "cê") "title" h2 "teste"} }'
        tree = parse(src)
        tree1 = parse(src1)
        tree2 = parse(src2)
        tree3 = parse(src3)
        print(pretty(tree))
        print(pretty(tree1))
        print(pretty(tree2))
        print(pretty(tree3))
        assert parse(src) == ['module', ['macro', op, [x], ['html', 'div', {classe: 'foo', ID: 'bar'}, [['html', 'h1', {}, ['title']]]]]]
        assert parse(src1) == ['module', ['macro', op, [x], ['html', 'div', {classe: 'foo', ID: 'bar'}, [['html', 'h1', {y:'ipslon'}, ['title']]]]]]
        assert parse(src2) == ['module', ['macro', op, [x], ['html', 'div', {classe: 'foo', ID: 'bar'}, [['html', 'h1', {}, ['title']], ['html', 'h2', {}, ['teste']]]]]]
        assert parse(src3) == ['module', ['macro', op, [x], ['html', 'div', {classe: 'foo', ID: 'bar'}, [['html', 'h1', {y: "ipslon", c: "cê"}, ['title']], ['html', 'h2', {}, ['teste']]]]]]

    def test_full_define(self):
        src = 'x = h1 (alexandre = 2, mo = 1) "bar";'
        src2 = 'x = h1 (alexandre = 2, mo = 1, jao = 24, cristo = 13) "bar";'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['define', x, ["html", "h1", {alexandre: 2, mo: 1}, ["bar"]]]]
        assert parse(src2) == ['module', ['define', x, ["html", "h1", {alexandre: 2, mo: 1 , jao: 24, cristo: 13}, ["bar"]]]]

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
        
    def teste_multiples_children(self):
        src = 'y = h2 (x = 1) {"bar"};'
        tree = parse(src)
        print(pretty(tree))
        assert parse(src) == ['module', ['define',y, ["html", "h2", {x:1} , ['bar']]]]
        
    def teste_multiples_children_advanced(self):
        src2 = 'y = h2 (x = 1) {h1 (a = 2, b = 1) "bar"};'
        tree = parse(src2)
        print (pretty(tree))
        assert parse(src2) == ['module', ['define',y, ["html", "h2", {x:1} , [["html", "h1", {a: 2, b: 1}, ["bar"]]]]]]
        
class TestRuntime:
    def test_define_html(self):
        env = {}
        eval(parse('x = h1 "hello";'), env)
        print(env)
        a = h('h1', {}, ['hello'])
        assert env[x] == str(a)
    
    def teste_define_full_html(self):
        env = {}
        eval(parse('x = h1 (classe="foo", ID="bar") "hello";'), env)
        print(env)
        a = h('h1', {'classe':'foo', 'ID':'bar'}, ['hello'])
        assert env[x] == str(a)
    
    def teste_macro_full_html(self):
        env = {}
        eval(parse('macro op(x){ div(classe = "foo") {"title"}}'),env)
        src = h('div', {'classe':'foo'}, ['title'])
        print(env[op])
        assert env[op]== (op, [x],[str(src)])


def pretty(x):
    try:
        return x.pretty()
    except AttributeError:
        return str(x)