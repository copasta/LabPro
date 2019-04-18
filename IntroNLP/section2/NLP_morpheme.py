
##  形態素解析
## 『入門 自然言語処理』

## N 名詞
## V 動詞(-Z 未然形 -Y 連用系 -S 終止形 -T 連体形 -R 命令形)
## J 助詞(-K 格助詞 -F 副助詞)
## T 連体詞
## SF 接尾辞
## A 助動詞

import nltk

_BOS_ENTRY = {'length':1, 'pos':'BOS', 'lemma': u'BOS', 'cost': 0}
_EOS_ENTRY = {'length':1, 'pos':'EOS', 'lemma': u'EOS', 'cost': 0}

## 隣接行列では無理なグラフをこの関数で作る事が出来る．
def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        if not 'value' in trie:
            trie['value'] = []
        trie['value'].append(value)

## 共通接頭辞の探索
def common_prefix_search(trie, key):
    ret = []
    if 'value' in trie:
        ret += trie['value']
    if key:
        first, rest = key[0], key[1:]
        if first in trie:
            ret += common_prefix_search(trie[first], rest)
    return ret

## 連接可能か?
def is_connectaqble(bnode, cnode):
    ctable = set([
        ('BOS', 'N'), ('BOS', 'V'),
        ('N', 'N'), ('N', 'V'), ('N', 'J'),
        ('J', 'V'),
        ('V', 'N'),('V', 'EOS')
    ])
    bpos = bnode['entry']['pos']
    cpos = cnode['entry']['pos']
    return (((bpos, cpos) in ctable) or ((bpos, cpos) in ctable))

def enum_solutions(node):
    results = []
    if node['entry']['lemma'] == u'EOS':
        return [[u'EOS']]
    for nnode in node['next']:
        for solution in enum_solutions(nnode):
            results.append([node['entry']['lemma']]+solution)
    return results

## 形態素解析
def simple_morphogical(trie, sent, connect_func=lambda x,y: True):
    bos_node = {'next':[], 'entry':_BOS_ENTRY}
    end_node_list = nltk.defaultdict(list)
    end_node_list[0].append(bos_node)
    for i in range(0, len(sent)+1):
        if i < len(sent):
            cps_results = common_prefix_search(trie, sent[i:].encode('utf-8'))
        else:
            cps_results = [_EOS_ENTRY]
        
        for centry in cps_results:
            cnode = {'next':[], 'entry':centry}

            for bnode in end_node_list[i]:
                if connect_func(bnode, cnode):
                    bnode['next'].append(cnode)

                    end_nodes = end_node_list[i+centry['length']]

                    if not cnode in end_nodes:
                        end_nodes.append(cnode)

    return enum_solutions(bos_node)

if __name__ == "__main__":
    
    dict_entries = [
        [u"ね", {'pos':'N', 'lemma':u"根"}],
        [u"たら", {'pos':'N', 'lemma':u"鱈"}],
        [u"ねた", {'pos':'V', 'lemma':u"寝た"}],
        [u"ら", {'pos':'SF', 'lemma':u"ら"}],
        [u"ねたら", {'pos':'V', 'lemma':u"寝たら"}],
        [u"げんき", {'pos':'N', 'lemma':u"元気"}],
        [u"に",  {'pos':'J', 'lemma':u"に"}],
        [u"なった", {'pos':'V', 'lemma':u"なった"}],
        [u"になった", {'pos':'V', 'lemma':u"担った"}]
    ]

    matrie = nltk.defaultdict(dict)

    for entry in dict_entries:
        entry[1]['length'] = len(entry[0])
        insert(matrie, entry[0].encode('utf-8'), entry[1])
    
    res = simple_morphogical(matrie, u'ねたらげんきになった', is_connectaqble)
    print('\n'.join('/'.join(sent) for sent in res))