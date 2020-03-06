tag_dict = {}
search_tag = '台北景點'   # 手動更改
path_dir = 'E:\專題\Instagram'
path = path_dir+'\{0}\Tag.txt'.format(search_tag)
with open(path, 'r', encoding='utf8') as f:
    txt_line_list = f.readlines()

for each_line in txt_line_list:
    for each_tah in each_line.split('#')[1:-1] :
        if each_tah in tag_dict:
            tag_dict[each_tah] += 1
        else:
            tag_dict[each_tah] = 1

# print(tag_dict)
tag_dict_list = sorted(tag_dict.items(), key=lambda d: d[1], reverse=True)
# print (tag_dict_list)
print("共", len(tag_dict_list), '個 Tag')
print(search_tag)
for i in range(300, 600):

    print('第', i, '名 :', tag_dict_list[i][0], tag_dict_list[i][1])
