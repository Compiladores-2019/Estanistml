# Projeto Final de Compiladores 2/2019

## Linguagem Estanisml

Linguagem template feita em Lark que traduz seu código para HTML.

### Exemplo

```
macro main(obj) {
   div (class="foo" id="bar") {
        h1 $obj.title1
        h2 $obj.title2
        p $obj.parag
        a $obj.link
        title $obj.title
        strong $obj.text
        em $obj.italico
    }
}
```

## Instalação e Execução

Install Docker-compose

### Run

> make build

> make run

### Run test

> python3 -m pytest tests/teste1.py

## Autores

| Nome | GitHub | Matricula | 
|------|--------|-----------| 
|Guilherme Leal| [@gleal17](https://github.com/gleal17) | 15/0128312 |
|João Pedro Soares| [@jpcirqueira](https://github.com/jpcirqueira) |15/0132344|
|Lucas Alexandre|[@lucasA27](https://github.com/lucasA27) | 15/0136862|
|Moacir Mascarenha|[@moacirmsj](https://github.com/MoacirMSJ)|17/0080366 |
