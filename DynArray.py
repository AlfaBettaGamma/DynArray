import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        if i == self.count:
            self.array[self.count] = itm
            self.count += 1
        else:
            new_array = self.make_array(self.capacity)
            if i is not 0:
                for number in range(0,i):
                    new_array[number] = self.array[number]
                new_array[i] = itm
                for number in range(i+1,self.count+1):
                    new_array[number] = self.array[number-1]
                self.array = new_array
                self.count += 1
        # добавляем объект itm в позицию i, начиная с 0

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        new_array = self.make_array(self.capacity)
        if i is not 0:
            for number in range(i+1,self.count):
                new_array[number-1] = self.array[number]
            self.array = new_array
            self.count -= 1
            if self.count/self.capacity * 100 < 50:
                self.resize(int(self.capacity/1.5))
        # удаляем объект в позиции i