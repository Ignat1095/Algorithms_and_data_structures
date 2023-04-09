# Структура данных для хранения узла бинарного дерева
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Обход заданного бинарного дерева с использованием обхода предварительного порядка
def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


# Распечатать заданный двусвязный список слева направо
def getChildrenCount(head):
    while head:
        print(head.data, end=' ')
        head = head.right


# Возвращает true, если данный узел дерева является листом; ложь в противном случае
def isLeaf(root):
    return root is not None and root.left is None and root.right is None


# Функция для извлечения листьев бинарного дерева в двусвязный список.
# `head` и `tail` отслеживают начало и конец двусвязного списка.
def construct(root, head=None, tail=None):
    # Базовый вариант
    if root is None:
        return None, head, tail

    is_leaf = isLeaf(root)

    # повторяется для левого поддерева
    (root.left, head, tail) = construct(root.left, head, tail)

    # , если текущий узел является листом
    if is_leaf:
        # Это верно только для самого левого конечного узла.
        if head is None:
            # указывает голову двусвязного списка на текущий конечный узел и
            # инициализирует хвостовой указатель
            head = tail = root
        else:
            # устанавливает левый дочерний элемент текущего узла в конец двусвязного списка.
            root.left = tail
            # устанавливает правый дочерний элемент хвоста в текущий узел
            tail.right = root
            # обновить хвост
            tail = root

        # возвращает None, чтобы удалить текущий узел из двоичного дерева.
        return None, head, tail

    # повторяется для правого поддерева
    root.right, head, tail = construct(root.right, head, tail)

    # возвращает корневой узел
    return root, head, tail


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)

    root.right.left.left = Node(10)
    root.right.left.right = Node(11)

    root, head, tail = construct(root)

    print('Номера листьев = ', end='')
    getChildrenCount(head)
