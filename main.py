# List

# append(), add an element to the end of a list
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)

# copy()
# 在Python中，copy() 方法用于创建一个列表的浅拷贝（shallow copy）。浅拷贝意味着新列表包含原始列表中元素的副本，但不会递归地复制嵌套的对象。换句话说，如果原始列表包含其他可变对象（如列表或字典），它们的引用将被复制到新列表中，而不是创建它们的新副本。
original_list = [1, 2, 3, [4, 5]]
print("未做任何修改的原始列表", original_list)
# 使用 copy() 创建原始列表的浅拷贝
copied_list = original_list.copy()
# 修改原始列表的一个元素
original_list[3][0] = 99
# 打印原始列表和浅拷贝后的列表
print("修改元素后的原始列表:", original_list)
print("浅拷贝后的列表:", copied_list)
# 在上面的例子中，由于是浅拷贝，修改原始列表中嵌套列表的元素也会影响到浅拷贝后的列表。这是因为嵌套列表的引用被共享，而不是被复制。

# count() 计算列表中特定元素出现的次数
my_list = [1, 2, 2, 3, 4, 2, 5, 2]
count = my_list.count(2)
print(count)

# del 删除list中的某个元素 at specified index, 或者一个区间的数
my_list = [10, 20, 30, 40, 50]
del my_list[2]
print(my_list)

# extend() 和 append（）
# append()：接受一个参数，将其作为单个元素添加到列表的末尾。
# extend()：接受一个可迭代对象（通常是另一个列表），并将其所有元素添加到列表的末尾。
# 使用 append()
list1 = [1, 2, 3]
list1.append(4)
print(list1)
# 现在，list1 是 [1, 2, 3, 4]
# 使用 extend()
list2 = [5, 6, 7]
list1.extend(list2)
# 现在，list1 是 [1, 2, 3, 4, 5, 6, 7]

# indexing 定位输出打印list中的某个元素
my_list = [10, 20, 30, 40, 50]
print(my_list[0])
print(my_list[-1])

# insert() 插入一个元素 insert（index，element）
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)
# 打印出来是[1,2,6,3,4,5]

# modifying a list 根据index位置修改list中的具体某个元素, lis_name[index] = 修改内容
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print(my_list)
# Output: [10, 25, 30, 40, 50]

# pop() 列表中用于移除并返回指定索引处的元素的方法，pop（【index】）如果只是（），默认移除并返回列表的最后一个元素
my_list = [10, 20, 30, 40, 50]
removed_element = my_list.pop(2)
# Removes and returns the element at index 2
print(removed_element)
# Output: 30
print(my_list)
# Output: [10, 20, 40, 50]

# remove() 用于移除列表中指定值的方法, 语法 list.remove(value)
# remove() 方法只会移除列表中第一个匹配到的元素。如果列表中有多个相同的值，只有第一个匹配的值会被移除。
my_list = [10, 20, 30, 40, 50]
my_list.remove(30) # Removes the element 30
print(my_list)
# Output: [10, 20, 40, 50]

# reverse（）反转列表，会修改原始列表
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
# Output: [5, 4, 3, 2, 1]

# slicing[] 基本语法 sequence[start:stop:step]
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])
# Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3])
# Output: [1, 2, 3] (elements from the beginning up to index 2)
print(my_list[2:])
# Output: [3, 4, 5] (elements from index 2 to the end)
print(my_list[::2])
# Output: [1, 3, 5] (every second element)

# sort() 默认升序排序
my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)
# Output: [1, 2, 5, 8, 9]
# 降序用法
my_list = [5, 2, 8, 1, 9]
my_list.sort(reverse=True)
print(my_list)
# Output: [9, 8, 5, 2, 1]




# 列表（List）、字典（Dictionary）和集合（Set）区别

# 列表（List）：
# 有序序列，可以包含任意类型的元素。
# 使用方括号 [] 定义列表，元素之间用逗号分隔。
# 元素可以通过索引访问，索引从0开始。
# 列表是可变的（Mutable），可以通过各种方法添加、删除、修改元素。
my_list = [1, 2, 'three', 4.0]

# 字典（Dictionary）：
# 无序的键值对集合，每个元素由一个键和一个值组成。
# 使用花括号 {} 定义字典，键和值之间用冒号 : 分隔，键值对之间用逗号分隔。
# 键必须是唯一的，而值可以重复。
# 字典是可变的，可以通过键访问、添加、删除、修改元素。
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# 集合（Set）：
# 无序的不重复元素的集合。
# 使用花括号 {} 定义集合，元素之间用逗号分隔。
# 集合中的元素是唯一的，不允许重复。
# 集合是可变的，可以通过各种方法添加、删除元素。
my_set = {1, 2, 3, 4, 5}



