import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
newick_path = os.path.join(script_dir, "../deps/python-newick/src/")
sys.path.insert(0, newick_path)
import newick

class Node(object):
    def __init__(self, name=""):
        self.dico = {}
        if (name == None):
            self.dico["name"] = ""
        else:
            self.dico["name"] = name
        self.children = []
        self.parent = None

    @staticmethod
    def read(newick_filename):
        return Node.build_from_newick_object(
                newick.read(newick_filename)[0])
    
    @staticmethod
    def build_from_newick_object(newick_node):
        node = Node(newick_node.name)
        for newick_child in newick_node.descendants:
            child = Node.build_from_newick_object(newick_child)
            child.set_parent(node)
            node.add_child(child)
        return node
  
    def get_newick_node(self, label_name):
        label = "-"
        if label_name in self.dico:
            label = str(self.dico[label_name])
        result = newick.Node(label)
        for child in self.children:
            result.descendants.append(child.get_newick_node(label_name))
        return result

    def get_ascii(self, label):
        newick_node = self.get_newick_node(label)
        return newick_node.ascii_art()

    def set_name(self, name):
        self.dico["name"] = name

    def get_name(self):
        return self.dico["name"]
    
    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def set_parent(self, node):
        self.parent = node

    def get_parent(self):
        return self.parent

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not self.children

    def set_label(self, label_name, label):
        self.dico[label_name] = label

    def get_label(self, label_name):
        return self.dico[label_name]

    def has_label(self, label_name):
        return label_name in self.dico

    def __str__(self):
        return self.get_name()

    def name_unnamed_nodes(self, base_name, index=[0]):
        """
        Traverse the tree in pre-order fashion and uniquely
        name the nodes that don't have a name yet
        """
        if (not self.get_name()):
            self.set_name(base_name + str(index[0]))
            index[0] = index[0] + 1
        for child in self.get_children():
            child.name_unnamed_nodes(base_name, index)

    def label_with_height(self, height = 0):
        self.set_label("height", height)
        for child in self.get_children():
            child.label_with_height(height + 1)

def lca(node1, node2):
    """
    node1 and node2 must have a common ancestor AND the tree
    must be labelled with label_with_height
    """
    while (node1 != node2 and node1 and node2):
        if (node1.get_label("height") > node2.get_label("height")):
            node1 = node1.get_parent()
        else:
            node2 = node2.get_parent()
    return node1

