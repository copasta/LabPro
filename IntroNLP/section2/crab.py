
## 学習済みベクトル
## https://github.com/Kyubyong/wordvectors
## http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/

import gensim
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('./data/entity_vector.model.bin', binary=True)

print('かに')
for result in model.most_similar(u'かに', topn=5):
    print(result)

print('蟹')
for result in model.most_similar(u'蟹', topn=5):
    print(result)

print('カニ')
for result in model.most_similar(u'カニ', topn=5):
    print(result)

'''
かに
('きつね', 0.7576180696487427)
('さば', 0.7575410604476929)
('みそ', 0.752464234828949)
('どん', 0.7488217353820801)
('もなか', 0.735567033290863)
蟹
('鼠', 0.7857352495193481)
('蛙', 0.7853800058364868)
('鮒', 0.7824612259864807)
('芋', 0.7820870876312256)
('海老', 0.7772840857505798)
カニ
('イカ', 0.776286244392395)
('[イカ]', 0.7702370285987854)
('[カニ]', 0.7595261335372925)
('シカ', 0.7583878636360168)
('[タコ]', 0.7548997402191162)
'''