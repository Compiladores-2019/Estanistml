from estanistml import var, env, Symbol, parse, eval

run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, h, op = map(Symbol, 'x y a b c f g h op'.split())



class TestGrammar:
    
    def test_quote_is_converted_to_sexpr(self):
        aux = parse("macro word")
        print (str(aux))
        assert True == False
