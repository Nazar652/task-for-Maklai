import itertools
from pprint import pprint

from flask import Flask, request, jsonify
from nltk.tree import *


app = Flask(__name__)


@app.route('/paraphrase', methods=['GET'])
def resp():
    string_tree = request.args.get('tree')
    tree = Tree.fromstring(string_tree)
    tree.pretty_print()
    nodes = find_same_nodes(tree, 'NP')
    combos = generate_combos(nodes)
    generate_trees(tree, nodes, combos)
    return 'None'


def find_same_nodes(in_tree, node_name):
    nodes = []

    def in_depth(node, pos):
        check_node(node, pos)

        for i, n in enumerate(node):
            if len(n) > 1:
                in_depth(n, pos + (i, ))

    def check_node(node, pos):
        add_node = []
        for i, n in enumerate(node):
            if n.label() == node_name:
                add_node.append(pos + (i, ))
            elif n.label() in (',', 'CC'):
                pass
            else:
                return
        nodes.append(add_node)

    in_depth(in_tree, tuple())
    return nodes


def generate_combos(nodes):
    all_permutations = []
    for n in nodes:
        all_permutations.append(tuple(itertools.permutations(n)))
    combos = tuple(itertools.product(*all_permutations))
    return combos


def generate_trees(tree, nodes, combos):
    trees = {
        'paraphrases': []
    }
    default_nodes = []
    for n in nodes:
        default_nodes.append([tree[i] for i in n])

    for c in combos:
        replacing_nodes = []
        for n in c:
            replacing_nodes.append([tree[i] for i in n])


if __name__ == '__main__':
    app.run()

