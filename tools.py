import itertools
from nltk.tree import *


def find_key_nodes(tree: Tree, key_nodes: list | tuple) -> list:
    """
    A function for searching for nodes consisting of nodes with
    tags that are specified at the beginning of the search.
    :param tree:
    :param key_nodes:
    :return:
    """
    replacing_nodes = []

    def in_depth(node, position):
        """
        A recursive function that implements the DFS.
        :param node:
        :param position:
        :return:
        """
        if node.label() in key_nodes:
            check_node(node, position, node.label())

        for i, n in enumerate(node):
            if len(n) > 1:
                in_depth(n, position + (i,))

    def check_node(node, position, label):
        """
        Function that checks if the node fits to searching nodes.
        :param node:
        :param position:
        :param label:
        :return:
        """
        new_replace_node = []
        for i, n in enumerate(node):
            if n.label() == label:
                new_replace_node.append(position + (i,))
            elif n.label() in (',', 'CC'):
                pass
            else:
                return
        replacing_nodes.append(new_replace_node)

    in_depth(tree, tuple())
    return replacing_nodes


def generate_combinations(nodes: list) -> tuple:
    """
    Function that generates all possible combinations of tree nodes.
    :param nodes:
    :return:
    """
    all_permutations = []
    for n in nodes:
        all_permutations.append(tuple(itertools.permutations(n)))
    combos = tuple(itertools.product(*all_permutations))
    return combos


def generate_trees(tree: Tree, nodes: list, combos: tuple, limit: int) -> dict:
    """
    A function that generates a dictionary with all
    the trees according to the generated combinations.
    :param tree:
    :param nodes:
    :param combos:
    :param limit:
    :return:
    """
    trees = {
        'paraphrases': []
    }
    default_nodes = []
    for n in nodes:
        default_nodes.append([tree[i] for i in n])

    for ea, c in enumerate(combos):
        rep_tree = tree
        replacing_nodes = []
        for n in c:
            replacing_nodes.append([tree[i] for i in n])
        if ea == 1:
            pass
        for i, tree_nodes in enumerate(replacing_nodes):
            for j, tree_node in enumerate(tree_nodes):
                rep_tree[nodes[i][j]] = tree_node
        trees['paraphrases'].append(
            {
                'tree': rep_tree.__str__()
            }
        )
        if ea == limit:
            break

    return trees
