from dataclasses import dataclass
from .nodetype import NodeType
from __future__ import annotations

@dataclass
class Node:
    type: NodeType = NodeType.PATH
    isVisited: bool = False
    row: int = -1
    col: int = -1
    g: int = 0
    h: int = 0
    previousNode: Node = None
