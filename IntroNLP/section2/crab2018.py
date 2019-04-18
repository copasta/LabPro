
## 学習済みベクトル
## https://github.com/singletongue/WikiEntVec

import gensim
from gensim.models import word2vec
from gensim.models import KeyedVectors

f_path = './data/jawiki.entity_vectors.300d.txt'

model = KeyedVectors.load_word2vec_format(f_path, binary=False)

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
('練り物', 0.7908490896224976)
('アンダンスー', 0.7904255986213684)
('切り込み', 0.7898656129837036)
('青のり', 0.7877135872840881)
('揚げ玉', 0.78424471616745)
蟹
('タコ', 0.675778865814209)
('ウニ丼', 0.6331205368041992)
('キタムラサキウニ', 0.6330656409263611)
('カニ', 0.6328063011169434)
('鯵', 0.6273504495620728)
カニ
('タコ', 0.7989360094070435)
('イカ', 0.7620768547058105)
('ウニ', 0.7538758516311646)
('エビ', 0.7534494400024414)
('ヒトデ', 0.7150376439094543)
'''