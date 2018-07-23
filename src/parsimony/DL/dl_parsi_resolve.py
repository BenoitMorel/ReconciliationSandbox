import sys
sys.path.insert(0, '../../common/')
import mapping
import node

if (len(sys.argv) != 4):
    print("Syntax: python dl_parsi_resolve.py species_newick gene_polytomy_newick species map")
    sys.exit(1)

species_newick = sys.argv[1]
gene_polytomy_newick = sys.argv[2]
mapping_file = sys.argv[3]

species_tree = node.Node.read(species_newick)
species_tree.name_unnamed_nodes("S")
print("Species tree: \n" + species_tree.get_ascii("name"))




