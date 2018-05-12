import xml.etree.ElementTree as ET
import sys

def get_relations(root):
    return [relation for relation in root.findall('.relation')]

def get_relation_ways(root, relation):
    way_ids = [member.get('ref') for member in relation.findall('.member[@type=\'way\']')]
    return [root.find('.way[@id=\'' + id +  '\']') for id in way_ids]

def remove_relation_ways(root, relation):
    ways = get_relation_ways(root, relation)
    for way in ways:
        root.remove(way)

def get_simple_ways(root):
    return [way for way in root.findall('.way')]

def get_nodes(root, way):
    node_ids = [node_ref.get('ref') for node_ref in way.findall('.nd')]
    return [root.find('.node[@id=\'' + id + '\']') for id in node_ids]

def get_node_coords(node): # returns a coordinate list
    return [float(node.get('lat')), float(node.get('lon'))]

def get_node_list(root, way): # returns a list of coordinate lists
    return [get_node_coords(node) for node in get_nodes(root, way)]

def parse(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    borders = []

    relations = get_relations(root)

    for relation in relations:
        relation_borders = []

        relation_ways = get_relation_ways(root, relation)
        for way in relation_ways:
            relation_borders.append(get_node_list(root, way))
        remove_relation_ways(root, relation)

        borders.append(relation_borders)

    simple_ways = get_simple_ways(root)
    for way in simple_ways:
        borders.append(get_node_list(root, way))

    return borders

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(-1)

    print(parse(sys.argv[1]))