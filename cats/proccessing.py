def get_cats_info(path):
    cat_list = []
    try:
        with open(path, 'r', encoding='UTF-8') as fl:
            lines = fl.readlines()
            for line in lines:
                info = line.strip().split(',')
                cat_dict = { 'id': info[0], 'name': info[1], 'age': info[2]}
                cat_list.append(cat_dict)
    except FileNotFoundError:
        print('File is not found')
    return cat_list

cats_info = get_cats_info("./cats/cats_file.txt")
print(cats_info)