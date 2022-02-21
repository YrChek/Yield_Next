def flat_generator(collection):
    for list_ in collection:
        for el in list_:
            yield el


def generator(my_list):
    full_list = []

    def recruitment(lists):
        for sps in lists:
            if not isinstance(sps, list):
                full_list.append(sps)
            else:
                recruitment(sps)

    recruitment(my_list)
    for i in full_list:
        yield i
