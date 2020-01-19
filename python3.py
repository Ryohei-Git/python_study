#位置引数のタプル化、キーワード引数の辞書化、docstring、関数内関数、クロージャー

#—位置引数のタプル化—
#位置引数のタプル化
#*argsを使うとまとめてタプル化される
def say_something(*args):
    for arg in args:
        print(arg)

say_something('Hi','Mike','Nance')

#単体で引数を指定することも可能
def say_something(word,*args):
    print('word = ',word )
    for arg in args:
        print(arg)

say_something('Hi','Mike','Nance')

#下記のやり方でも可能
t = ('Mike','Nancy')
say_something('Hi',*t)

#—キーワード引数の辞書化—
#キーワード引数の辞書化
def menu(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
menu(entree='beef',drink='coffee')

#辞書型で書いて渡す方法
d = {
    'entree' : 'beef',
    'drink' : 'ice coffee',
    'dessert' : 'ice'
}

menu(**d)

#最初の引数がfood
#最初以外のキーワードのない引数が*args
#キーワード引数が**kwargsに入る
#順序を正しく書かないとエラーになる
def menu(food,*args,**kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana','apple','orange',entree='beef',drink='coffee')

#—doctoring—-
#Docstrings
def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    Returns:
        bool: The return value. True for success,False otherwise.

    """
    print(param1)
    print(param2)
    return True
#下記の記述で出力できる
print(example_func.__doc__)
help(example_func)

#—関数内関数—
#関数内関数
#関数内だけで使う関数の時使用する
def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a,b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)
#—クロージャー—
# クロージャー

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

#—デコレーター—
#デコレーター
#関数の前に実行したい関数を設定するイメージ
#@の後に実行したい関数を書く
#１つ作成すれば何度も使える

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:',func.__name__)
        print('args:',args)
        print('kwargs:',kwargs)
        result = func(*args, **kwargs)
        print('result:',result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)


#ラムダ、ジェネレータ
#ラムダ
#コード量を減らせる

l = ['Mon','tue','Wed','Tue','Fri','sat','Sun']

def change_words(words,func):
    for word in words:
        print(func(word))

#def sample_func(word):
#   return word.capitalize()

sample_func = lambda word:word.capitalize()
change_words(l,sample_func)

#直接書くこともできる
change_words(l,lambda word:word.capitalize())

#—ジェネレータ—
#ジェネレーター
#呼ばれたタイミングで順番に出力する。
#yield実行後関数を抜ける
#重い処理の間に書くことで分けて処理を行える
def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(g))
print(next(c))
print(next(g))
