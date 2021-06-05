from collections import deque


def search(a_graph, name):
    search_queue = deque()
    search_queue += a_graph[name]
    visited = []
    while search_queue:
        person = search_queue.popleft()
        if person not in visited:
            if is_seller(person):
                print("we found a mongo seller: " + person)
                return True
            else:
                search_queue += a_graph[person]
                visited.append(person)
    return False


def is_seller(name):
    return name[-1] == 'm'


if __name__ == '__main__':
    graph = {}
    graph['you'] = ["ahmed", "said", "awd"]
    graph["said"] = ["ali", "medhat"]
    graph["ali"] = ["said", "mariam"]
    graph['ahmed'] = []
    graph['awd'] = []
    graph['medhat'] = []
    graph['mariam'] = []
    print(search(graph, 'you'))
