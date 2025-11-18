"""
HW02 — Courier Handoffs (BFS Shortest Path)

Implement:
- bfs_path(graph, s, t)
"""

from collections import deque
from typing import Dict, List, Optional, Any

def bfs_path(graph: Dict[Any, List[Any]], s: Any, t: Any) -> Optional[List[Any]]:
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. If s or t not in graph, return None.
    """
    if s not in graph or t not in graph:
        return None
    if s == t:
        return [s]

    queue = deque([s])
    visited = {s}
    parent = {s: None}

    while queue:
        node = queue.popleft()
        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = node
                if nbr == t:
                    # Reconstruct path from t back to s.
                    path = []
                    cur = t
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    path.reverse()
                    return path
                queue.append(nbr)

    return None