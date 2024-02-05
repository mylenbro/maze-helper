from json import load
from pathlib import Path
from typing import Dict, List, Optional
from collections import deque


class PathFinder:

    def __init__(self) -> None:
        self.graph: Dict[str, List[str]] = None

    def loadMap(self, filepath: Path) -> None:
        path = filepath.joinpath('graph.json')
        with open(path) as file:
            self.graph = load(file)

    # bfs algo
    def find(self, start: str, end: str, requiredNodes: List[str], maxOccurrences: Optional[int] = None) -> Optional[List[str]]:
        if self.graph is None:
            return None

        queue = deque([(start, [])])
        while queue:
            currentNode, path = queue.popleft()
            if currentNode == end and all(node in path for node in requiredNodes):
                # return path + [end]
                return self.__fixPath(path + [end])
            if maxOccurrences:
                occurrences = path.count(currentNode)
                if occurrences >= maxOccurrences:
                    continue
            neighbors = self.graph.get(currentNode, [])
            for neighbor in neighbors:
                queue.append((neighbor, path + [currentNode]))
        return None

    def __fixPath(self, path: List[str]) -> List[str]:
        modifiedPath = [s[:2] for s in path]
        fixedPath: List[str] = []
        for index, item in enumerate(modifiedPath):
            nextIndex = index + 1
            neighborExists = nextIndex < len(modifiedPath)
            if (neighborExists and modifiedPath[nextIndex] == item):
                continue
            fixedPath.append(item)
        return fixedPath
