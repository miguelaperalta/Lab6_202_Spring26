from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Node:
    val: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def preorder(tree: Optional[Node]) -> list[int]:
    if tree is None:
        return []
    return [tree.val] + preorder(tree.left) + preorder(tree.right)


def inorder(tree: Optional[Node]) -> list[int]:
    if tree is None:
        return []
    return inorder(tree.left) + [tree.val] + inorder(tree.right)


def postorder(tree: Optional[Node]) -> list[int]:
    if tree is None:
        return []
    return postorder(tree.left) + postorder(tree.right) + [tree.val]


def bfs(tree: Optional[Node]) -> list[int]:
    if tree is None:
        return []
    result = []
    q = [tree]

    while q:
        current = q.pop(0)
        result.append(current.val)

        if current.left is not None:
            q.append(current.left)

        if current.right is not None:
            q.append(current.right)
    
    return result
