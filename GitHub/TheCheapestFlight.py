from math import inf, isinf

def get_cities(costs: list) -> set:
    result = set()
    for item in costs:
        result = result.union(set(item[:2]))
    return result


def cheapest_flight(costs: list, a: str, b: str) -> int:
    # your code here
    cities = get_cities(costs)
    rout_costs = {}
    checked_cities = set()
    rout_cost_result = {}

    for c in cities:
        rout_costs.update({c:("", inf)})
    rout_costs.update({a:(a,0)})

    def get_cheapest_neighbor():
        min_cost = min(list(map(lambda x: rout_costs[x][1], rout_costs)))
        for it in rout_costs.keys():
            if it not in checked_cities:
                if rout_costs[it][1] == min_cost:
                    return it
        return ''

    def get_linked(node):
        result = {}
        for item in costs:
            if node in set(item[:2]):
                point = set(item[:2]).difference(node).pop()
                cost = item[2]
                if point not in checked_cities:
                    result.update({point:cost})
        return result

    while checked_cities != cities:
        current_point = get_cheapest_neighbor()
        current_rout = rout_costs[current_point][0]
        current_cost = rout_costs[current_point][1]

        linked_points = get_linked(current_point)
        for p in linked_points.keys():
            new_cost = current_cost + linked_points[p]
            new_rout = current_rout + '-' + p
            old_cost = rout_costs[p][1]
            if old_cost > new_cost:
                rout_costs.update({p:(new_rout, new_cost)})

        checked_cities = checked_cities.union(current_point)
        rout_cost_result.update({current_point: rout_costs.pop(current_point)})
    return 0 if isinf(rout_cost_result[b][1]) else rout_cost_result[b][1]


print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
