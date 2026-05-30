import math

def minimax(depth, node_index, maximizing_player, values):

    if depth == 3:
        return values[node_index]

    if maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, values),
            minimax(depth + 1, node_index * 2 + 1, False, values)
        )

    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values),
            minimax(depth + 1, node_index * 2 + 1, True, values)
        )

values = [3, 5, 6, 9, 1, 2, 0, -1]

result = minimax(0, 0, True, values)

print("Optimal Value:", result)
