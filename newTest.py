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
        for k in range(i, self.count - 1):
        	self.array[k] = self.array[k + 1]
        self.count -= 1
        if self.count < self.capacity * 0.5:
            self.resize(int(self.capacity / 1.5))
            if self.capacity < 16:
            	self.capacity = 16
        # удаляем объект в позиции i


def test1():
	da = DynArray()
	for i in range(12):
	    da.append(i)
	    print (da[i]) 
	da.insert(10,999)
	print('len - ',da.__len__())
	print('cap - ', da.capacity)
	for i in range(da.__len__()):
	    print('test - ',da[i])

def test2():
	da = DynArray()
	for i in range(12):
	    da.append(i)
	    print (da[i]) 
	da.insert(10,999)
	print('len - ',da.__len__())
	print('cap - ', da.capacity)
	da.insert(10,888)
	da.insert(10,777)
	da.insert(10,666)
	da.insert(10,555)
	da.insert(10,444)
	for i in range(da.__len__()):
	    print('test - ',da[i])
	print('len - ',da.__len__())
	print('cap - ', da.capacity)

def test3():
	da = DynArray()
	for i in range(12):
	    da.append(i)
	    print (da[i]) 
	da.insert(15,999)
	print('len - ',da.__len__())
	print('cap - ', da.capacity)
	for i in range(da.__len__()):
	    print('test - ',da[i])

def test4():
	da = DynArray()
	for i in range(19):
	    da.append(i)
	    print (da[i]) 
	da.delete(10)
	print('len - ',da.__len__())
	print('cap - ', da.capacity)
	da.delete(4)
	for i in range(da.__len__()):
	    print('test - ',da[i])
	print('len - ',da.__len__())
	print('cap - ', da.capacity)

def test5():
	da = DynArray()
	for i in range(19):
	    da.append(i)
	    print (da[i]) 
	print('len - ',da.__len__())
	print('cap - ', da.capacity)
	da.delete(10)
	da.delete(9)
	da.delete(8)
	da.delete(7)
	da.delete(6)
	da.delete(5)
	da.delete(4)
	da.delete(3)
	da.delete(2)
	da.delete(1)
	for i in range(da.__len__()):
	    print('test - ',da[i])
	print('len - ',da.__len__())
	print('cap - ', da.capacity)	

def test6():
	da = DynArray()
	for i in range(19):
	    da.append(i)
	    print (da[i]) 
	print('len - ',da.__len__())
	print('cap - ', da.capacity)
	da.delete(28)


test = test5()
test