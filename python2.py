#タプル、辞書、比較演算子、論理演算子
#タプル
#新しい値の代入ができない
t = (1, 2, 3, 4, 5)
print(t[-1])
print(t.index(1))
print(t.count(1))
t = ([1, 2, 3],[4, 5, 6])
t[0][0] = 3 #タプルの中のリストには代入できる
print(t)
t = 1, 2, 3
t = 1, # タプル型になるためバグになりやすい
print(t)

t = (1) #１つだとint型になるためタプルは2つ以上の数字が入る
print(type (t))

new_tuple = (1, 2, 3) + (4, 5, 6) #結合
print(new_tuple)

#タプルのアンパック
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x,y)

min, max = 0, 100
print(min, max)

#普通の入れ替え
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i,j)

#変数の入れ替えが簡単に行える
a = 100
b = 200
a, b = b, a
print(a, b)


#—辞書型—
#辞書型
#キーと値が分かっているときに使える
d = {'x': 10, 'y': 20}
print(d['x'])
print(d['y'])

d['z'] = 200 #追加
print(d)

#他の作り方
dict(a=10,b=20)
dict([('a', 10),('b', 20)])

#辞書型のメソッド
print(d.keys())
print(d.values())
d2 = {'x': 1000,'j': 500}

d.update(d2) #アップデートする
print(d)
print(d.get('q')) #ない場合はNoneTypeを返す

d.pop('x') # 削除
print(d)
del d['y'] #削除
print(d)
d = {'a':100,'b':200}
#d.clear() 辞書の中身を消す　
print('a' in d) #リストの中に存在するか確認

#辞書のコピー
x = {'a': 1}
y = x
y['a'] = 1000
#参照渡しになる
print(x)
print(y)
#コピーを使えば正しくコピーできる
x = {'a':100}
y = x.copy()
x = {'a':1}
print(x)
print(y)

#—set—
#集合型
#重複が省かれる 共通点を見つけるときに使える
a = {1, 2, 3, 4, 4, 4, 5, 6}
print(a,type(a))

b = {2, 3, 3, 6, 7}
print(b)
print(a - b) #存在する数字が引かれる
print(a & b) #and
print(a | b) #or
print(a ^ b) #xor

s = {1, 2, 3, 4, 5}
# s[0] 並び順がないからエラーになる
s.add(6)
print(s)
s.remove(6)
s.clear()
print(s) #{}で返すと辞書かsetか分からなくなるためset()で表示される

#setの使用例
my_friend = {'A', 'B', 'C'}
A_friend = {'B', 'D', 'E', 'F'}
print(my_friend & A_friend)

f = ['apple','banana','apple','banana']
kind = set(f)
print(kind)

#—コメント—-
#コメント
print('xxxxx')
#"""で囲むとまとめてコメント化できる
"""
test
test
test
"""
print('xxxxx')

#コメントは基本的にコードの上に書くのがルール
#apple price
some_value = 100

#バックスラッシュをつけたら改行できる
#80文字以上続いている場合は次の行へ行くのがルール
s = 'aaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbbbb'

print(s)
#下記の書き方でも改行できる
s = ('aaaaaaaaaaaaa'
    + 'bbbbbbbbbbbbbb')

—if—
#if
x = 10
if x < 0:
    #スペースを4つ開けるのがルール
    print('negative')
elif x == 10:
    print('10')
else:
    print('positive')


a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

#—比較演算子と論理演算子—
#比較演算子と論理演算子
a = 1
b = 1

# a が b と等しい
print(a == b)

# a が b と異なる
print(a != b)

# a が b よりも小さい
print(a < b)

# a が b よりも大きい
print(a > b)

# a が b 以下である
print(a <= b)

# a が b 以上である
print(a >= b)

# a も b も真であれば真
print(a > 0 and b > 0)

# a または b が真であれば真
print(a > 0 or b > 0)

#in、None、while、input、for、range、enumerate、zip、関数定義、キーワード引数
#—in—
#in と　not in
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

#数字の比較では推奨されていない
if not a == b:
    print('Not equal')
#下記の方がわかりやすい
if not a != b:
    print('Not equal')

#boolean型の否定をしたい場合ではよく使われる
is_ok = True
if is_ok:
    print('hello')
if not is_ok:
    print('hello')

#値が入っていればTrue,値が入っていない場合はFalseとして扱われる
is_ok = 1 # true
is_no = 0 # false
is_ok = 'ok' #true
is_no =  '' # false

if is_ok:
    print('OK!')
else:
    print('No!')

#—None—
#None

is_empty = None
#print(help(is_empty))

#推奨されていない
if is_empty == None:
    print('None')

#このやり方で比較する
#is オブジェクト同士が同じものか比べる
if is_empty is None:
    print('None')

print(1 == True) #true
print(1 is True) #false
print(True is True) #true

#—while—
#while
count = 0
while count < 5:
    print(count)
    #countを忘れたら無限ループになる
    count += 1

#breakでループを抜ける
#continueは次の行を飛ばしてループへ戻る
count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue

    print(count)
    count += 1

#while else
count = 0

while count < 5:
    print(count)
    count += 1
else:
    #breakで抜けない場合ループ終了後に実行される
    print('done')

#—-input—
#input
#文字を入力する関数
while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')

#複数の文字をリストに入れる
word = input('Enter:')
words = word.split(' ')
print(words,type(words))
print(words[0],type(words[0]))

#—for—
#for文
#インデックスを使う必要がない
some_list = [1, 2, 3, 4, 5]
for i in some_list:
    print(i)

#文字列を直接出力
for s in 'abcde':
    print(s)

#単語ごとに出力
for word in ['My', 'name', 'is', 'Mike']:
    print(word)

#for else
for fruit in ['apple', 'orange', 'banana']:
    print(fruit)
else:
    #breakしていない場合、ループの最後で実行される
    print('i ate all')

#—range—
#range関数
#この処理は下記のように修正できる
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    print(i)

#実行する数字を指定できる
#開始する数字、ループ回数、ステップ（飛ばす）を指定できる
for i in range(10):
    print(i)

#iを今後使わない場合は_(アンダースコア)を使う
for _ in range(10):
    print('Hello')

#enumerate関数
#リストにインデックスをつける
for i, fruit in enumerate(['apple', 'orange', 'banana']):
    print(i, fruit)

#—zip—
#zip関数
#インデックスを指定せず実行できる
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day,fruit,drink in zip(days, fruits, drinks):
    print(day, fruit,drink)

#—辞書型をfor文で使う—
#辞書をfor文で処理
#よく使われるから覚えておくと良い
d = {'x': 100, 'y': 200}
print(d.items())
for k,v in d.items():
    print(k,':',v)

#—関数定義—
#関数定義
#関数定義の下で関数を呼び出す
#なんども書くコードは関数定義しておく
def say_something():
    print('hi')

#関数を実行する
say_something()
# function型で表示される
print(type(say_something))

#下記の方法でも関数が実行できる
f = say_something
f()

#戻り値
def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)

#引数
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "i don't know"

result = what_is_this('red')
print(result)

#型の宣言はできるが文字列でも動作するためエラーがでない
# ->　は返り値の型を明示的にする
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num('a','b')
print(r)

#—キーワード引数—
#キーワード引数
#順番が変わっても正しく入る
def menu(entree, drink, dessert):
    print('entree =', entree)
    print('drink = ', drink)
    print('dessert =', dessert)
menu(drink='beer',dessert='ice',entree='beef')

#—デフォルト引数—
#デフォルト引数
#引数を渡さなかった場合の変数に入る値
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree =', entree)
    print('drink = ', drink)
    print('dessert =', dessert)
menu(entree='chicken')

#リストに値を追加して返す
#リストはデフォルト引数で与えないルール
#参照したリストに値を追加するためバグになりやすい
#下記の書き方は非推奨
def test_func(x,l=[]):
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)

#下記の書き方をすることで空のリストを扱える
def test_func(x,l = None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)

y = [1, 2, 3]
r = test_func(100,y)
print(r)
