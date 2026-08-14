class TreeNode:

    def __init__(self, value,
                 children=None):

        self.value = value
        self.children = children or []

def minimax(node, is_max):

    if not node.children:
        return node.value

    scores = [
        minimax(child, not is_max)
        for child in node.children
    ]

    if is_max:
        return max(scores)

    return min(scores)

root = TreeNode(0, [

    TreeNode(0, [
        TreeNode(3),
        TreeNode(5)
    ]),

    TreeNode(0, [
        TreeNode(2),
        TreeNode(9)
    ]),

    TreeNode(0, [
        TreeNode(12),
        TreeNode(5)
    ])
])

best = minimax(root, True)

print(
    "Best value for MAX player:",
    best
)
