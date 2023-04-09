class Node:
    """Клас для создания вершины бинарного дерева"""

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    """Класс для работы с бинарным деревом"""

    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        """Метод поиска вершины дерева к которой необходимо добавить значение"""
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        """Метод для добавления к бинарному дереву новых елементов из списка"""

        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        """Метод для отображения бинарного дерева"""
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self, node):
        """Метод для отображения бинарного дерева в ширину"""
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf(self, s, p):
        """Метод для удаления листовой вершины"""
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        """Метод для удаления вершини с одним потомком"""
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left

        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        """Метод для поиска минимального значения для удаления"""
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def del_node(self, key):
        """Метод для удаления из бинарного дерева"""
        s, p, fl_find = self.__find(self.root, None, key)
        if not fl_find:
            return None
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def min_node(self):
        """Метод лля поиска минимального значения"""
        node = self.root
        data = node.data
        while node:
            data = node.data
            node = node.left
        return data

    def max_node(self):
        """Метод лля поиска максимального значения"""
        node = self.root
        data = node.data
        while node:
            data = node.data
            node = node.right
        return data

v = [10, 5, 7, 16, 13, 2, 20, 14, 54]

t = Tree()
for x in v:
    t.append(Node(x))

# t.del_node(14)
t.show_wide_tree(t.root)
print()
print('min =', t.min_node())
print('max =', t.max_node())
