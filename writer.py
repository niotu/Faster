for i in range(1, 21):
    with open(f'texts/text{i}.txt', 'r', encoding='utf-8') as f:
        line = f.read()
        my_tuple = (i, line)
        res = 'INSERT INTO texts ( id, text ) VALUES ' + str(my_tuple) + ';'
        print(res)
