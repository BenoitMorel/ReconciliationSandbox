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


class DP_Table:
  def __init__(self, 
          species_tree, 
          gene_polytomy_node,
          species_count):
    self.postorder_species_nodes = []
    node.get_nodes_postorder(species_tree, self.postorder_species_nodes)
    self.species_datas = {}
    self.maxk = len(self.postorder_species_nodes) #todo how to define this number??
    self.species_count = species_count

  def get_species_entry(self, species_node):
    if (not (species_node.get_name() in self.species_data)):
      compute_species_entry(self, species_node)
    return self.species_data[species_node.get_name()]

  def _get_species_count(self, species_node):
      name = species_node.get_name()
      if (name in self.species_count):
          return self.species_count[name]
      else:
          return 0

  def compute_species_entry(self, species_node):
    species_data = SpeciesData(self.maxk)
    self.species_datas[species_node.get_name()] = species_data
    if (species_node.is_leaf()):
        nb = self._get_species_count(species_node)
        M = species_data.M
        for k in range(0, self.maxk):
            M[k] = abs(k + 1 - nb)
        print("M("+species_node.get_name()+") = " + str(M))
    else:
        for child in species_node.get_children():
            self.compute_species_entry(child)


def compute_species_count(leaves_mapping_str):
    species_count = {}
    for gene_str in leaves_mapping_str:
        species_str = leaves_mapping_str[gene_str]
        if (not species_str in species_count):
            species_count[species_str] = 1
        else:
            species_count[species_str] += 1
    return species_count

species_newick = sys.argv[1]
gene_polytomy_newick = sys.argv[2]
mapping_file = sys.argv[3]

species_tree = node.Node.read(species_newick)
species_tree.name_unnamed_nodes("S")
print("Species tree: \n" + species_tree.get_ascii("name"))
gene_polytomy_tree = node.Node.read(gene_polytomy_newick)
gene_polytomy_tree.name_unnamed_nodes("g")
print("Gene polytomy: \n" + gene_polytomy_tree.get_ascii("name"))


leaves_mapping_str = mapping.load_leaves_mapping_str(mapping_file)
print("Mapping: " + str(leaves_mapping_str))
species_count = compute_species_count(leaves_mapping_str)
print("Species count: " + str(species_count))
dp_table = DP_Table(species_tree, gene_polytomy_tree, species_count)
dp_table.compute_species_entry(species_tree)






