from pprint import pprint
from typing import List, Optional


# def remove(node, sub_paths):
#     for element in sub_paths.copy():
#         if node in element:
#             sub_paths.remove(element)
#     return sub_paths
#
#
# def find_ways(from_node, to_node, paths):
#     # if from_node not in paths:
#     #     return []
#
#     ways = {}
#     if from_node == to_node:
#         return to_node
#
#     for path in paths:
#         if from_node in path:
#             sub_paths = paths.copy()
#             if from_node == from_node.lower():
#                 sub_paths = remove(from_node, sub_paths)
#             rest_way = find_ways((path - {from_node}).pop(), to_node, sub_paths)
#             if rest_way:
#                 if from_node not in ways.keys():
#                     ways[from_node] = []
#                 ways[from_node].append(rest_way)
#
#     return ways

# def main_1():
#     with open("data.txt") as f:
#         paths = []
#         used_nodes = set()
#         for row in f.readlines():
#             node_1, node_2 = row.strip().split("-")
#             paths.append({node_1, node_2})
#
#         ways = find_ways("start", "end", paths)
#         pprint(ways)
#         # Solution is counting number of 'end' in output from print above
#


# global


def remove2(node, sub_paths, use_twice):

    for element in sub_paths.copy():
        if node in element:
            if node in ("start", "end"):
                sub_paths.remove(element)
            elif use_twice == node:
                use_twice = None
                break
            else:
                sub_paths.remove(element)

    return sub_paths, use_twice


def extract_lowercase_nodes(paths):
    result_set = set()
    for path in paths:
        for node in list(path):
            if node.lower() == node and node not in ("start", "end"):
                result_set.add(node)

    return result_set


def find_ways2(from_node, to_node, paths, use_twice):
    # if from_node not in paths:
    #     return []

    ways = {}
    if from_node == to_node:
        return to_node

    for path in paths:
        if from_node in path:
            sub_paths = paths.copy()
            if from_node == from_node.lower():
                sub_paths, use_twice = remove2(from_node, sub_paths, use_twice)
            rest_way = find_ways2(
                (path - {from_node}).pop(), to_node, sub_paths, use_twice
            )
            if rest_way:
                if from_node not in ways.keys():
                    ways[from_node] = []
                ways[from_node].append(rest_way)

    return ways


# def convert_to_list(ways):
#     return_list = []
#     if isinstance(ways, dict):
#         for key, value in ways.items():
#             return_list.append(key)
#             return_list += convert_to_list(value)
#
#     if isinstance(ways, list):
#         for way in ways:
#             return_list += convert_to_list(way)
#
#     if isinstance(ways, str):
#         return_list.append(ways)
#
#     return return_list
#
#
# def split_result_list(ways):
#     result_list = []
#     current_list = []
#     for node in ways:
#         if node == "start":
#             current_list = [node]
#         elif node == "end":
#             if current_list == []:
#                 current_list = result_list[-1][:-2]
#             current_list.append(node)
#             result_list.append(current_list)
#             current_list = []
#             # if result_list[-1][-1] == "end":
#             #     current_list = current_list[:-2]
#         else:
#             if current_list == []:
#                 current_list = ["start"]
#             current_list.append(node)
#
#     return result_list


def convert_to_list(ways):

    result_list = []
    current_list = []
    for way in ways:
        if way == "end":
            result_list.append(way)
            continue
        for node, value in way.items():
            value_list = convert_to_list(value)
            for v in value_list:
                current_list = [node] + [v]
                result_list += [current_list]

    return result_list


def split_result_list(ways):
    result_list = []
    current_list = []
    for node in ways:
        if node == "start":
            current_list = [node]
        elif node == "end":
            if current_list == []:
                current_list = result_list[-1][:-2]
            current_list.append(node)
            result_list.append(current_list)
            current_list = []
            # if result_list[-1][-1] == "end":
            #     current_list = current_list[:-2]
        else:
            if current_list == []:
                current_list = ["start"]
            current_list.append(node)

    return result_list


def main_2():
    with open("minitest_data.txt") as f:
        paths = []
        for row in f.readlines():
            node_1, node_2 = row.strip().split("-")
            paths.append({node_1, node_2})

        all_lowercase_nodes = extract_lowercase_nodes(paths)
        ways = []
        for use_twice in all_lowercase_nodes:
            ways.append(find_ways2("start", "end", paths, use_twice))
        pprint(ways)

        # Convert to list and remove duplicates
        ways = convert_to_list(ways)
        pprint(ways)
        # ways = split_result_list(ways)
        # pprint(ways)


if __name__ == "__main__":
    # main_1()
    main_2()
