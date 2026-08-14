class Node:

    def __init__(self,
                 value,
                 children=None):

        self.value = value
        self.children = children or []

def alpha_beta(node,
               depth,
               alpha,
               beta,
               is_max):

    if depth == 0 or not node.children:
        return node.value

    if is_max:

        value = float('-inf')

        for child in node.children:

            value = max(
                value,
                alpha_beta(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    False
                )
            )

            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return value

    else:

        value = float('inf')

        for child in node.children:

            value = min(
                value,
                alpha_beta(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    True
                )
            )

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value

root = Node(0, [

    Node(0, [
        Node(3),
        Node(5)
    ]),

    Node(0, [
        Node(2),
        Node(9)
    ]),

    Node(0, [
        Node(12),
        Node(5)
    ])
])

result = alpha_beta(
    root,
    2,
    float('-inf'),
    float('inf'),
    True
)

print(
    "Optimal Value:",
    result
)
