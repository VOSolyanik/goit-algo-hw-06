import networkx as nx
from collections import deque

# Реалізація алгоритмів DFS і BFS
def dfs(graph: nx.Graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            visited = dfs(graph, neighbor, visited)
    return visited

def bfs(graph: nx.Graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            neighbors = list(graph.neighbors(node))
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited

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
        ("Київ", "Харків"), ("Київ", "Одеса"), ("Київ", "Львів"), 
        ("Київ", "Дніпро"), ("Київ", "Запоріжжя"), ("Київ", "Вінниця"), 
        ("Київ", "Чернігів"), ("Київ", "Житомир"), ("Київ", "Полтава"), 
        ("Київ", "Черкаси"), ("Київ", "Суми"), ("Харків", "Дніпро"), 
        ("Харків", "Запоріжжя"), ("Харків", "Полтава"), ("Одеса", "Миколаїв"), 
        ("Одеса", "Херсон"), ("Львів", "Івано-Франківськ"), ("Львів", "Тернопіль"), 
        ("Львів", "Ужгород"), ("Львів", "Рівне"), ("Дніпро", "Запоріжжя"), 
        ("Дніпро", "Кривий Ріг"), ("Дніпро", "Полтава"), ("Донецьк", "Луганськ"), 
        ("Запоріжжя", "Миколаїв"), ("Луганськ", "Суми"), 
        ("Чернівці", "Івано-Франківськ"), ("Чернівці", "Тернопіль"), 
        ("Хмельницький", "Тернопіль"), ("Рівне", "Луцьк"), 
        ("Сімферополь", "Херсон")
    ]

    G.add_edges_from(connections)

    # Знаходження шляхів у графі
    start_node = "Київ"

    dfs_path = dfs(G, start_node)
    bfs_path = bfs(G, start_node)

    # Порівняння результатів
    print("Порівняння шляхів DFS та BFS:")
    print("DFS шлях: ", dfs_path)
    print("BFS шлях: ", bfs_path)

    # Пояснення різниці
    difference = set(dfs_path) ^ set(bfs_path)
    print(f"Різниця в шляхах: {difference}")

if __name__ == "__main__":
    main()