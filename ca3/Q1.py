import sys
import functools

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if attr == 'Node':
                setattr(cls, attr, getattr(cls, attr))
            elif callable(getattr(cls, attr)) :
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
        for i in range(1,len(args)):
            if isinstance(newArgsList[i], str):
                newArgsList[i] = newArgsList[i].replace('\'', '')
        return tuple(newArgsList)

def fix_str_arg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(len(args) > 1):
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
class MinHeap:
    def __init__(self):
        self.heap = []
        
    class Node:
        def __init__(self, val):
            self.val = val
        
    def bubble_up(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if not len(self.heap):
            raise Exception('empty')
        if index < 0 or index >= len(self.heap):
            raise Exception('out of range index')
        while index > 0:
            if ((index-1)//2 >= 0) and (self.heap[(index-1)//2].val > self.heap[index].val):
                self.heap[(index-1)//2].val, self.heap[index].val = self.heap[index].val, self.heap[(index-1)//2].val
            else: 
                break
            index = (index-1)//2
            
    def bubble_down(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if not len(self.heap):
            raise Exception('empty')
        if index < 0 or index >= len(self.heap):
            raise Exception('out of range index')
        min = index
        while 2*index < len(self.heap):
            if ((2*index + 1) < len(self.heap)) and (self.heap[min].val > self.heap[2*index + 1].val):
                min = 2*index + 1
            if ((2*index + 2) < len(self.heap)) and (self.heap[min].val > self.heap[2*index + 2].val):
                min = 2*index + 2
            if min != index:
                self.heap[min].val,self.heap[index].val=self.heap[index].val,self.heap[min].val
                index = min
            else: 
                break
    
    def heap_push(self, value):
        new = self.Node(value)
        self.heap.append(new)
        
        self.bubble_up(len(self.heap)-1)
        
    def heap_pop(self):
        if not len(self.heap):
            raise Exception('empty')
        node_pop = self.heap[0].val
        self.heap[0].val = self.heap[len(self.heap)-1].val
        self.heap.pop()
        if len(self.heap):
            self.bubble_down(0)
        return node_pop
    
    def find_min_child(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if index < 0 or index >= len(self.heap):
            raise Exception('out of range index')
        if not len(self.heap):
            raise Exception('empty')
        if 2*index < len(self.heap) and self.heap[2*index+1].val > self.heap[2*index+2].val:
            return 2*index+2
        return 2*index+1
            
    def heapify(self, *args):
        for val in args:
            self.heap_push(val)

class HuffmanTree:
    def __init__(self):
        self.letters = []
        self.repetitions = []
        self.head = None
        self.count = None
        
    @fix_str_arg    
    def set_letters(self,*args):
        self.letters = args
        self.count = {i: None for i in self.letters }

    @fix_str_arg    
    def set_repetitions(self,*args):
        self.repetitions = args

    class Node:
        def __init__(self, lett, freq, left=None, right=None):
            self.letter = lett
            self.freq = freq
            self.left = left
            self.right = right
            self.dir = ""
            
    def build_huffman_tree(self):
        nodes = list(zip(self.repetitions,self.letters))
        nodes = [self.Node(i,j) for j,i in nodes]
        nodes.sort(key = lambda x : (x.freq,x.letter), reverse=True)
        while len(nodes) > 1:
           nodes.sort(key = lambda x : (x.freq), reverse=True)
           r = nodes[-1]
           l = nodes[-2]
           nodes = nodes[:-2]
           r.dir = "0"
           l.dir = "1"
           new_head= self.Node("", r.freq+l.freq, l, r)
           nodes = [new_head] + nodes
           self.head = new_head
        self.get_nodes_cost(node = self.head)

    def get_nodes_cost(self, node, nodes_list = ""):
        n = nodes_list + node.dir
        if node.right:
            self.get_nodes_cost(node.right,n)
        if node.left:
            self.get_nodes_cost(node.left,n)
        if not node.right and not node.left:
            self.count[node.letter] = n

    def get_huffman_code_cost(self):
        cost = 0
        i = 0
        for letter in self.count:
            cost += self.repetitions[i]*len(self.count[letter])
            i += 1
        return cost

    @fix_str_arg
    def text_encoding(self, text):
        split_letters = {}
        for letter in text:
            split_letters[letter] = split_letters[letter]+1 if letter in split_letters else 1
        self.letters= list(split_letters.keys())
        self.repetitions = list(split_letters.values())
        self.count = {i:None for i in self.letters }
        self.build_huffman_tree()

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class Bst(): 
    def __init__(self):
        self.root = self.Node(None)
        self.print = 0
    
    class Node:
        def __init__(self, parent = None, val = None, left = None, right = None):
            self.value = val
            self.parent = parent 
            self.left = left
            self.right = right
                        
    def insert(self, key):
        current = self.root
        if current.value == None:
            current.value = key
            return
        new_node = self.Node(val = key)
        while current != None:
            parent = current
            if current.value > new_node.value:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if new_node.value < new_node.parent.value:
            new_node.parent.left = new_node
        else:
            new_node.parent.right = new_node
                
    def inorder(self):
        inorder_list = []
        def node_read_value(node):
            if node != None:
                node_read_value(node.left)
                inorder_list.append(node.value)
                # print(node.value)
                node_read_value(node.right)
            return
        node_read_value(self.root)
        print(*inorder_list)
        

classDict = { "min_heap": MinHeap, "bst": Bst, "huffman_tree": HuffmanTree}
    
if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.start_program()

