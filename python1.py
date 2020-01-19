#変数、print、文字列のライブラリ
#---変数宣言---
num = 1
Name = ‘mike’
is_ok = true

#変数の型がわかる
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

#自動で変換される例
num = 1
name = 'mike'
num = name

#キャストされる例
num = 1
name = '1'
num = int(name)
print(num,type(num))

#明示的にする※型が変わることが多いからあまり使われない
num: int = 1
name: str = '1'
num = int(name)
print(num,type(num))

print(‘hi’, ‘mike’, sep=‘,’)

#—数値を扱う—
#  四則演算
# 足し算　＋
# 引き算　ー
# 掛け算　＊
# 割り算　/
# 商　　　//
# べき乗　＊＊
round(数字,丸める桁数)
#math 数学関数
print(help(math)) 関数の使い方を調べる


#---‘’’と’’がある理由---
print(“I don’t know”)
#バックスラッシュを使えば使える
print(’I don\’t know’)
#\nで改行ができる
print(’hello. \n How are you?’)
#改行したくない時
print(r ‘c:\name\name’)

#まとめて改行して表示したい時※”の変換がおかしい
print(“””
line1
line2
line3
“””)
# 上記の書き方だとline1の上とline3の下に空白行が1つ入る。
#いれたくない場合は下記のように記載する。
print(“””\
line1
line2
line3\
“””)
#x回表示する
print(‘Hi’ * x)

#長い文字を出力する時
s = (aaaaaaaaaaaaaaaa
	bbbbbbbbbbbbbbbb)

s = aaaaaaaaaaaaaaaaaa \
      bbbbbbbbbbbbbbbbbb

#—インデックスとスライスの使い方—
# [-1]
# [0:2]
# [2:]3から最後まで

#先頭１文字を変える場合
word[0] = ‘j’ #※この記法は使えないので下記の方法を使う
word = ‘j’ + word[1:]

#—文字列のライブラリ—
s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize()) #最初だけ大文字で他小文字
print(s.title()) #全てのワードの頭文字が大文字
print(s.upper()) #全て大文字
print(s.lower()) #全て小文字
print(s.replace('Mike','Nancy')) #文字の置き換え


#---文字列の代入---
#.format()
print('a is {}'.format('a'))
print('a is {}'.format('test'))
print('a is {} {} {}'.format(1,2,3))
print('a is {0} {1} {2}'.format(1,2,3)) #数字から文字列に変換される
print('a is {2} {1} {0}'.format(1,2,3))
print('My name is {0} {1}'.format('Yamada','Tarou'))
print('My name is {name} {family}'.format(name = 'Yamada',family = 'Tarou'))

#f-strings
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x},{y},{z}')

name = 'Tarou'
family = 'Yamada'
print(f'My name is {name} {family}')
print(f'私の名前は{family}{name}です')

②リストの操作
#リスト操作
l = [1,2,3,4,5,6,7,8]
print(l[0])
print(l[:2]) #前から２文字
print(l[-1]) #一番最後を出力
print(l[-2]) #最後から２文字目を出力
print(len(l)) #リストの長さを出力
print(type(l)) #型をチェックする
l2 = list('abcdefg') #1つづつリストに入れる
print(l2)
print(l[::2]) #2つ飛ばしで出力

a = ['a','b','c']
n = [1,2,3]
z = [a,n]

print(z)
print(z[0][-1]) #c

s = ['a','b','c','d','e','f','g']
s[0] = 'x'

print(s)
print(s[2:5])
s[2:5] = [] #2から5番目の要素を空にする
print(s)
s[:] = []
print(s) #リストの中身を空にする

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.append(100) #末尾に100を追加
print(n)
n.insert(0,200) #0番目に200を追加
print(n)
print(n.pop()) #末尾を削除
print(n.pop(0)) #0番目を削除
#del n nを全て消す

n.remove(2) #リスト内にある2を消す
print(n)

#リストの結合
#新しい変数を作って結合
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
#aにbを結合
a += b
print(a)

#extendメソッドを使って結合
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)

#リストのメソッド
r = [1, 2, 3, 4, 5, 1, 2, 3 ]
print(r.index(3)) #3のある位置を返す
print(r.index(3,3)) #4番目以降に3のある位置を返す

print(r.count(3)) #3の数を数える

r.sort() #昇順にソート
print(r)
r.sort(reverse=True) #降順にソート
print(r)
r.reverse() #降順にソート
print(r)

s = 'My name is Mike'
to_split = s.split(' ') #空白で区切ってリストに入れる
print(to_split)

x = ' '.join(to_split) # ' 'で区切って結合
print(x)

print(help(list)) #リストのヘルプを見る

#リストのコピー
#参照渡しになる例
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100

print(j)
print(i)

#参照渡しせずコピーする方法
x = [1, 2, 3, 4, 5]
y = x.copy() # y = x[:]でも可能
y[0] = 100
print(x)
print(y)
