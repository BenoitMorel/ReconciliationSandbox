import sys
sys.path.insert(0, '../../common/')
import mapping
import node

if (len(sys.argv) != 4):
    print("Syntax: python dl_parsi_resolve.py species_newick gene_polytomy_newick species map")
    sys.exit(1)

print("This script implements the algorithm presented in \"An optimal reconciliation algorithm for gene trees with polytomies\" (Lafond et. al)")
print("Variable (k, C, M...) are also named from this article notations")

class SpeciesData(object):
    def __init__(self, maxk):
      self.C = [0] * maxk
      self.M = [0] * maxk
      #self.m1 = 0
      #self.m2 = 0
      #self.gamma = 0


class DP_Table:
  def __init__(self, species_tree, gene_polytomy_node):
    self.postorder_species_nodes = []
    node.get_nodes_postorder(species_tree, self.postorder_species_nodes)
    self.species_data = {}
    self.maxk = len(self.postorder_species_nodes) #todo how to define this number??

  def get_species_entry(self, species_node):
    if (not (species_node.get_name() in self.species_data)):
      compute_species_entry(self, species_node)
    return self.species_data[species_node.get_name()]

  def compute_species_entry(self, species_node):
    self.species_data[species.get_name()] = SpeciesData(maxk)

  def compute_species_k_entry(self, species_node, k):
    pass


species_newick = sys.argv[1]
gene_polytomy_newick = sys.argv[2]
mapping_file = sys.argv[3]

species_tree = node.Node.read(species_newick)
species_tree.name_unnamed_nodes("S")
print("Species tree: \n" + species_tree.get_ascii("name"))
gene_polytomy_tree = node.Node.read(gene_polytomy_newick)
gene_polytomy_tree.name_unnamed_nodes("g")
print("Gene polytomy: \n" + gene_polytomy_tree.get_ascii("name"))

dp_table = DP_Table(species_tree, gene_polytomy_tree)
dp_table.compute_species_k_entry(species_tree, 0)






