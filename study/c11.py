flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']


def myEnumerate(collection):
    'Generates an indexed series:  (0,coll[0]), (1,coll[1]) ...'
    i = 0
    it = iter(collection)
    print("it type: ", type(it))
    while 1:
        yield (i, it.__next__())
        i += 1


if __name__ == '__main__':
    for i, flavor in myEnumerate(flavor_list):
        print("%d: %s" % (i + 1, flavor))

