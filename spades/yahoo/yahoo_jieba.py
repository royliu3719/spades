import jieba

txt = ''
path = 'e:/thematic/Yahoo/factory.txt'    # 爬蟲文檔路徑
stopword = 'e:/thematic/Yahoo/factory_stopword.txt'   # 停用詞庫路徑

with open(path, 'r', encoding='utf8') as f:
    txt = f.read()

with open(stopword, 'r', encoding='utf8') as f:
    stopword = f.read()

jieba_txt = jieba.cut(txt)
jieba_txt = list(filter(lambda a: a not in stopword and a != '\n', jieba_txt))
# print(jieba_txt)
word_cunt_dict = {}

for each_word in jieba_txt:
    if len(each_word) == 1 :
        continue

    if each_word in word_cunt_dict:
        word_cunt_dict[each_word] += 1
    else:
        word_cunt_dict[each_word] = 1

# print(word_cunt_dict)

sort_list = []
for each_dict_key in word_cunt_dict:
    if word_cunt_dict[each_dict_key] > 5:
        sort_list.append((each_dict_key,word_cunt_dict[each_dict_key]))


sort_list.sort(key=lambda x:x[1],reverse=True)

print("共", len(sort_list), '個 Tag')
print(sort_list)
for i in range(1, len(sort_list)):

    print('第', i, '名 :', sort_list[i-1][0], sort_list[i-1][1])