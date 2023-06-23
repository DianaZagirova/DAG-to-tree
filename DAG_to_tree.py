
def dag2tree(graph_init, root_node):
    dict_att = {}
    graph = graph_init.copy()
    # create dict for the "visited" attribute
    for i in list(graph):
        if i == root_node:
            dict_att[i] = "true"
        else:
            dict_att[i] = "false"
    nx.set_node_attributes(graph, dict_att, name="visited")
    cnt_visited = 0

    cnt = 0
    key = 1

    # loop through the graph nodes while there are unvisited nodes
    while "false" in list(nx.get_node_attributes(graph, "visited").values()):
        print(cnt)

        descendants_at_distance = list(nx.descendants_at_distance(graph, root_node, distance=cnt))
        br_tree3 = list(graph.out_edges(descendants_at_distance))
        br_tree_ans = [i[0] for i in br_tree3]
        br_tree_des = [i[1] for i in br_tree3]
        ans_des_list = []
        for node_ans, node_des in zip(br_tree_ans, br_tree_des):
            key += 1
            if graph.nodes[node_des]["visited"] == "false":
                graph.nodes[node_des]["visited"] = "true"
            else:
                cnt_visited += 1

                ans_des_list.append(node_ans + '_' + str(key) + '_' + node_des)
                nodeset = nx.descendants(graph, node_des)
                nodeset.add(node_des)
                sub_graph = graph.subgraph(nodeset)
                dict_names = {}
                for i in list(sub_graph):
                    dict_names[i] = node_ans + '_' + str(key) + '_' + i
                sub_graph = nx.relabel_nodes(sub_graph, dict_names)
                graph.remove_edge(node_ans, node_des)
                edges2add = list(sub_graph.edges)
                edges2add = edges2add + [tuple([node_ans, node_ans + '_' + str(key) + '_' + node_des])]
                graph.add_edges_from(edges2add)
                list_added = list(set([item for t in edges2add for item in t]))
                list_added.remove(node_ans)
                dict_att_subgraph = {}
                for i in list_added:
                    if i != node_ans + '_' + str(key) + '_' + node_des:
                        dict_att_subgraph[i] = "false"
                    else:
                        dict_att_subgraph[i] = "true"
                nx.set_node_attributes(graph, dict_att_subgraph, name="visited")

        print(
            f"Round {cnt}, all - {len(list(graph))}, visited {cnt_visited}, true in graph - {list(nx.get_node_attributes(graph, 'visited').values()).count('true')}")
        cnt += 1

    return graph