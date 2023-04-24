from flask import Flask, request

from tools import *


# initializing Flask app and setting config
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/paraphrase', methods=['GET'])                      # a decorator who implements API endpoint
def resp():
    # getting the tree in the string form, limit, and nodes for which the search is performed
    string_tree = request.args.get('tree')
    limit = int(request.args.get('limit')) if request.args.get('limit') else 20
    key_nodes = request.args.get('nodes').split(', ') if request.args.get('nodes') else ['NP']

    tree = Tree.fromstring(string_tree)                         # initializing tree from a string form
    nodes = find_key_nodes(tree, key_nodes)                     # finding key nodes
    combinations = generate_combinations(nodes)                 # generating combinations
    trees = generate_trees(tree, nodes, combinations, limit)    # generating trees

    return trees


if __name__ == '__main__':
    app.run(port=8000)
