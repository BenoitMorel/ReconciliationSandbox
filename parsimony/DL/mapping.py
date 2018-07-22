import sys
import os
import node

def load_leaves_mapping_str(mapping_file_path):
    """
    Load a dictionnary with gene names as keys and
    species names as value from the file at mapping_file_path
    """
    mapping = {}
    lines = open(mapping_file_path).readlines()
    for line in lines:
        split = line.split(" ")
        if (split[1].endswith("\n")):
            mapping[split[0]] = split[1][:-1]
        else:
            mapping[split[0]] = split[1]
    return mapping


def get_name_to_node(node, name_to_node):
    """
    Recursively fill name_to_node (dictionnary)
    with the node name as key and the node as
    value (if the node has a name)
    """
    if (node.get_name()):
        name_to_node[node.get_name()] = node
    for child in node.get_children():
        get_name_to_node(child, name_to_node)

def map_gene_to_species(gene_node, leaves_mapping, species_name_to_node):
    """
    Recursively map the gene nodes to species tree nodes
    Requires: the species tree is labelled with its height
    in label "height"
    leaves_mapping maps gene leaves names to species names
    """
    label = None
    if (gene_node.is_leaf()):
        label_str = leaves_mapping[gene_node.get_name()]
        label = species_name_to_node[label_str]
        gene_node.set_label("species", label)
        return label
    for child in gene_node.get_children():
        new_label = map_gene_to_species(child, leaves_mapping, species_name_to_node)
        if (label == None):
            label = new_label
        else:
            label = node.lca(label, new_label)
    gene_node.set_label("species", label)
    return label
