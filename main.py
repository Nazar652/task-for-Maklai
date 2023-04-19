from flask import Flask, request, jsonify
from nltk.tree import *


app = Flask(__name__)


@app.route('/paraphrase', methods=['GET'])
def resp():
    string_tree = request.args.get('tree')
    tree = Tree.fromstring(string_tree)
    combos = find_same_nodes(tree, 'NP')
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


if __name__ == '__main__':
    app.run()
