#リスト内包表記、辞書包括表記、集合内包表記、ジェネレータ内包表記

#—リスト内包表記—
#リスト内包表記
#2つ以上の時は使う場面を考える
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)
r = []

for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

#下記のように変形できる
r = [i for i in t if i % 2 ==0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i*j)

print(r)
#下記のように変形できる

r = [i * j for i in t for j in t2]
print(r)

#—辞書包括表記---
#辞書包括表記
#zip関数を使い辞書を作成する
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']
d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x,y in zip(w, f)}
print(d)

#—集合内包表記—
#集合内包表記
#リストとほぼ同様
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)
print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

#—ジェネレータ内包表記—
#ジェネレーター内包表記
def g():
    for i in range(10):
        yield i
g = g()

g = (i for i in range(10) if i %2 == 0)
#タプルにする場合
#g = tuple(i for i in range(10))
for x in g:
    print(x)

#スコープ、例外処理、独自例外
#—スコープ—
#名前空間とスコープ
animal = 'cat'

def f():
    #global と書くことでクローバル変数の中に値を入れることができる
    global animal
    print(animal)
f()

print('grobal',animal)


#—localsとglobals—
#下記の方法で変数を確認できる＼
animal = 'cat'

def f():
    animal = 'dog'
    print('local:',locals())
f()

print('grobal',globals())

#—例外処理—
#例外処理
#Pythonドキュメント5.4章のException hierarchyで例外処理を確認できる

l = [1, 2, 3]
i = 5

try:
    () + l
except IndexError as ex:
    #インデックスエラー
    #エラーを変数に入れる
    print("Don't worry:{}".format(ex))
except NameError as ex:
    #名前エラー
    print(ex)
except Exception as ex:
    #その他
    #全ての例外をキャッチする方法は推奨されていない
    print('other:{}'.format(ex))
finally:
    # 必ず実行される
    print('last')

#—else—
#例外処理
#Pythonドキュメント5.4章のException hierarchyで例外処理を確認できる

l = [1, 2, 3]
i = 5

try:
    l[0]
except IndexError as ex:
    #インデックスエラー
    #エラーを変数に入れる
    print("Don't worry:{}".format(ex))
except NameError as ex:
    #名前エラー
    print(ex)
except Exception as ex:
    #その他
    #全ての例外をキャッチする方法は推奨されていない
    print('other:{}'.format(ex))
else:
    #例外に何も問題がなかったときに処理される
    print('done')
finally:
    print('clean up')

#—独自例外—
#独自例外の作成
#raiseを使えば独自でエラーを作成できる
#独自エラーを作って例外を発生させることでエラーがわかりやすくなる
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('this is my fault. go next')

#import
#インポートする
#import lesson_package.utils
from lesson_package import utils#モジュールがわかるためこの記法か上の記法で書く
#from lesson_package.utils import say_twice このケースはあまり好まれない

#r = lesson_package.utils.say_twice('hello')
r = utils.say_twice('hello')
#r = say_twice('hello')
print(r)
