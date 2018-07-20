import sys
sys.path.insert(0, '../../deps/python-newick/src/')
import newick

class PhyloNode(object):
    def __init__(self, name=""):
        self.dico = {}
        if (name == None):
            self.dico["name"] = ""
        else:
            self.dico["name"] = name
        self.children = []

    @staticmethod
    def read(newick_filename):
        return PhyloNode.build_from_newick_object(
                newick.read(newick_filename)[0])
    
    @staticmethod
    def build_from_newick_object(newick_node):
        node = PhyloNode(newick_node.name)
        for child in newick_node.descendants:
            node.add_child(PhyloNode.build_from_newick_object(child))
        return node
  
    def get_newick_node(self, label):
        result = newick.Node(self.dico[label])
        for child in self.children:
            result.descendants.append(child.get_newick_node(label))
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

    


def load_mapping(mapping_file):
    mapping = {}
    lines = open(mapping_file).readlines()
    for line in lines:
        split = line.split(" ")
        if (split[1].endswith("\n")):
            mapping[split[0]] = split[1][:-1]
        else:
            mapping[split[0]] = split[1]
    return mapping

def map_gene_to_species(gene_tree, species_tree, mapping):
    """
    Recursively map the gene nodes to species tree nodes
    """

if (len(sys.argv) != 4):
    print("Syntax: python dl_parsi_rec.py genes species map")
    sys.exit(1)

species_newick = sys.argv[1]
genes_newick = sys.argv[2]
mapping_file = sys.argv[3]

species_tree = PhyloNode.read(species_newick)
print("Species tree: \n" + species_tree.get_ascii("name"))
gene_tree = PhyloNode.read(genes_newick)
print("Gene tree: \n" + gene_tree.get_ascii("name"))
mapping = load_mapping(mapping_file)
print("Mapping: " + str(mapping))

