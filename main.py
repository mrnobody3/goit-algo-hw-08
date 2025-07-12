import heapq
from typing import List


def min_cost_to_connect_ropes(ropes: List[int]) -> int:
    if len(ropes) == 0:
        return 0

    heapq.heapify(ropes)
    total_cost = 0

    while len(ropes) > 1:
        min_rope1 = heapq.heappop(ropes)
        min_rope2 = heapq.heappop(ropes)

        new_rope = min_rope1 + min_rope2
        total_cost += new_rope
        heapq.heappush(ropes, new_rope)

    return total_cost


# Example usage:
ropes = [2, 4, 3, 6]
print(min_cost_to_connect_ropes(ropes))
