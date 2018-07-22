import sys
import mapping
import node



if (len(sys.argv) != 4):
    print("Syntax: python dl_parsi_rec.py genes species map")
    sys.exit(1)

species_newick = sys.argv[1]
genes_newick = sys.argv[2]
mapping_file = sys.argv[3]

species_tree = node.Node.read(species_newick)
species_tree.name_unnamed_nodes("S")
print("Species tree: \n" + species_tree.get_ascii("name"))
gene_tree = node.Node.read(genes_newick)
gene_tree.name_unnamed_nodes("g")
print("Gene tree: \n" + gene_tree.get_ascii("name"))
leaves_mapping_str = mapping.load_leaves_mapping_str(mapping_file)
print("Mapping: " + str(leaves_mapping_str))
species_tree.label_with_height()
print("Species heights: \n" + species_tree.get_ascii("height"))
species_name_to_node = {}
mapping.get_name_to_node(species_tree, species_name_to_node)  
mapping.map_gene_to_species(gene_tree, leaves_mapping_str, species_name_to_node)
print("Gene mapped to species: \n" + gene_tree.get_ascii("species"))
