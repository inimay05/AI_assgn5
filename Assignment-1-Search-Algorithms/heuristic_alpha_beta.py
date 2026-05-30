import math

def heuristic(node):
    return node

def alpha_beta(depth,
               node_index,
               maximizing,
               values,
               alpha,
               beta,
               max_depth):

    if depth == max_depth:
        return heuristic(values[node_index])

    if maximizing:

        value = -math.inf

        for i in range(2):

            value = max(
                value,
                alpha_beta(
                    depth+1,
                    node_index*2+i,
                    False,
                    values,
                    alpha,
                    beta,
                    max_depth
                )
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for i in range(2):

            value = min(
                value,
                alpha_beta(
                    depth+1,
                    node_index*2+i,
                    True,
                    values,
                    alpha,
                    beta,
                    max_depth
                )
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value

values = [8,7,6,5,4,3,2,1]

result = alpha_beta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf,
    3
)

print("Best Heuristic Value:", result)
