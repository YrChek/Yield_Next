class FlatIterator:
    def __init__(self, collection, start=0):
        self.list = collection
        self.start = start
        self.full_list = []

    def __iter__(self):
        self.cursor = self.start
        for el in self.list:
            self.full_list += el
        return self

    def __next__(self):
        if self.cursor >= len(self.full_list):
            raise StopIteration
        else:
            current = self.full_list[self.cursor]
            self.cursor += 1
            return current


class CompoundIterator:
    def __init__(self, collection, start=0):
        self.list = collection
        self.start = start
        self.full_list = []

    def recruitment(self, list_iter):
        for item in list_iter:
            if isinstance(item, list):
                self.recruitment(item)
            else:
                self.full_list.append(item)

    def __iter__(self):
        self.cursor = self.start
        self.recruitment(self.list)
        return self

    def __next__(self):
        if self.cursor >= len(self.full_list):
            raise StopIteration
        else:
            current = self.full_list[self.cursor]
            self.cursor += 1
            return current
