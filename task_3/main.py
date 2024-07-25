import networkx as nx

# Реалізація алгоритмe Дейкстри

def dijkstra(graph: nx.Graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    return distances, previous_nodes

def get_shortest_path(previous_nodes, start, target):
    path = []
    node = target
    
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    
    path = path[::-1]
    if path[0] == start:
        return path
    else:
        return None

def main():
    
    # Створення графа
    G = nx.Graph()

    # Додавання вершин (обласних центрів)
    cities = [
        "Київ", "Харків", "Одеса", "Дніпро", "Донецьк", 
        "Запоріжжя", "Львів", "Кривий Ріг", "Миколаїв", "Луганськ",
        "Вінниця", "Сімферополь", "Херсон", "Полтава", "Чернігів", 
        "Черкаси", "Суми", "Житомир", "Хмельницький", "Чернівці",
        "Рівне", "Івано-Франківськ", "Тернопіль", "Луцьк", "Ужгород"
    ]

    G.add_nodes_from(cities)

    # Додавання ребер (прямих сполучень між обласними центрами)
    connections = [
        ("Київ", "Харків", 477), ("Київ", "Одеса", 475), ("Київ", "Львів", 540), 
        ("Київ", "Дніпро", 480), ("Київ", "Запоріжжя", 520), ("Київ", "Вінниця", 270), 
        ("Київ", "Чернігів", 140), ("Київ", "Житомир", 140), ("Київ", "Полтава", 340), 
        ("Київ", "Черкаси", 190), ("Київ", "Суми", 330), ("Харків", "Дніпро", 215), 
        ("Харків", "Запоріжжя", 285), ("Харків", "Полтава", 145), ("Одеса", "Миколаїв", 130), 
        ("Одеса", "Херсон", 200), ("Львів", "Івано-Франківськ", 130), ("Львів", "Тернопіль", 130), 
        ("Львів", "Ужгород", 260), ("Львів", "Рівне", 210), ("Дніпро", "Запоріжжя", 85), 
        ("Дніпро", "Кривий Ріг", 150), ("Дніпро", "Полтава", 200), ("Донецьк", "Луганськ", 150), 
        ("Запоріжжя", "Миколаїв", 270), ("Луганськ", "Суми", 425), 
        ("Чернівці", "Івано-Франківськ", 135), ("Чернівці", "Тернопіль", 145), 
        ("Хмельницький", "Тернопіль", 110), ("Рівне", "Луцьк", 65), 
        ("Сімферополь", "Херсон", 280)
    ]
    
    for conn in connections:
        G.add_edge(conn[0], conn[1], weight=conn[2])

    # Знаходження шляхів у графі
    start_node = "Київ"

    # Знаходження найкоротших шляхів у графі
    start_node = "Київ"
    distances, previous_nodes = dijkstra(G, start_node)

    # Виведення найкоротших шляхів від стартової вершини до всіх інших
    for target_node in cities:
        if distances[target_node] == 0:
            continue
        path = get_shortest_path(previous_nodes, start_node, target_node)
        print(f"Найкоротший шлях від {start_node} до {target_node}: {path} з відстанню {distances[target_node]}")


if __name__ == "__main__":
    main()