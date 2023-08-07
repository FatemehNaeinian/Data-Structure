import sys
import functools


def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if attr == 'Node':
                setattr(cls, attr, getattr(cls, attr))
            elif callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate


@for_all_methods(staticmethod)
class Utils():
    def parse_line(line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def delete_end_char(line):
        return line.rstrip(line[-1])

    def get_attribute_pointer(object, attribute):
        return getattr(object, attribute)

    def get_args(argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def run_function(attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)

    def covert_args_to_int(args):
        newArgsList = list(args[1:])
        for i in range(1, len(args)):
            if isinstance(args[i], str) and (args[i].isnumeric() or args[i][0] == '-'):
                newArgsList[i - 1] = int(args[i])
        return tuple([args[0]] + newArgsList)

    def delete_quotation(args):
        newArgsList = list(args)
        for i in range(1, len(args)):
            if isinstance(newArgsList[i], str):
                newArgsList[i] = newArgsList[i].replace('\'', '')
        return tuple(newArgsList)


def fix_str_arg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if (len(args) > 1):
            args = Utils.delete_quotation(args)
            args = Utils.covert_args_to_int(args)
        return func(*args, **kwargs)

    return wrapper


def print_raised_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if val != None:
                return val
        except Exception as e:
            print(str(e))

    return wrapper


class MainEmu():
    def __init__(self):
        self.items = dict()

    def start_program(self):
        for line in sys.stdin:
            line = Utils.delete_end_char(line)
            action, line = Utils.parse_line(line)
            actionPointer = Utils.get_attribute_pointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = Utils.parse_line(line)
        itemName, line = Utils.parse_line(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = Utils.parse_line(line, '.')
        funcName, line = Utils.parse_line(line, '(')
        argsLine, line = Utils.parse_line(line, ')')
        args = Utils.get_args(argsLine)
        attribute = Utils.get_attribute_pointer(self.items[itemName],
                                                funcName)

        Utils.run_function(attribute, args)


@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class Queue:
    def __init__(self):
        self.queue = []

    def getSize(self):
        size = len(self.queue)
        return size

    def enqueue(self, value):
        self.queue = [value] + self.queue

    def dequeue(self):
        size = len(self.queue)
        if size < 1:
            raise Exception('empty')
        return self.queue.pop()

    def isEmpty(self):
        size = len(self.queue)
        if size > 0:
            return False
        return True

    def getInOneLine(self): 
        return " ".join(map(str, list(reversed(self.queue))))


@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class Stack:
    def __init__(self, size=10):
        self.stack = []
        self.size = size

    def isEmpty(self):
        size = len(self.stack)
        if size > 0:
            return False
        return True

    def push(self, value):
        size = len(self.stack)
        # if size <= len(self.stack):
        #     self.expand()
        self.stack.append(value)

    def pop(self):
        size = len(self.stack)
        if size < 1:
            raise Exception('empty')
        return self.stack.pop()

    def put(self, value_):
        size = len(self.stack)
        if size < 1:
            raise Exception('empty')
        self.stack.pop()
        self.stack.append(value_)

    def peek(self):
        size = len(self.stack)
        if size < 1:
            raise Exception('empty')
        return self.stack[-1]

    def expand(self):
        self.size *= 2

    def getInOneLine(self):
        return " ".join(map(str, self.stack))

    def getSize(self):
        return len(self.stack)

    def getCapacity(self):
        return self.size


class Node():
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.Num = 0
        
    def getInOneLine(self):
        line = []
        temp = self.head
        while temp :
            line.append(temp.value)
            temp = temp.next
        return " ".join(map(str, line))
    
    def insertFront(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        if self.head == None:
            raise Exception('empty')
        previous = None
        current = self.head
        next = self.head.next
        while next != None:
            current.next = previous
            previous = current
            current = next
            if next != None:
                next = current.next
        current.next = previous
        self.head = current


classDict = {"stack": Stack, "queue": Queue, "linked_list": LinkedList}

if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.start_program()