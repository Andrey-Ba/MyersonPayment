import heapq


def payments(values: list[float], choice_rule) -> list[float]:
    topay = [0 for i in range(len(values))]
    # chosen_indexes = [i for i in range(len(chosen_values)) if chosen_values[i]]
    # not_chosen_indexes = [i for i in range(len(chosen_values)) if not chosen_values[i]]
    # for chosen_index in chosen_indexes:
    #     search_value = values.copy()
    #     while (choice_rule(search_value)[chosen_index]):
    #         search_value[chosen_index] = round(search_value[chosen_index] - 0.01, 2)
    #     topay[chosen_index] = round(search_value[chosen_index] + 0.01, 2)
    # for not_chosen_index in not_chosen_indexes:
    #     search_value = values.copy()
    #     while (not choice_rule(search_value)[not_chosen_index]):
    #         search_value[not_chosen_index] = round(search_value[not_chosen_index] + 0.01, 2)
    #     topay[not_chosen_index] = round(search_value[not_chosen_index], 2)
    for value_i in range(len(values)):
        topay[value_i] = FindHighestAcceptingBound(value_i, values.copy(), choice_rule, 0.01)
    return topay


# find the highest value that player i will be accepted and rejected if the value was lower by allowed difference
def FindHighestAcceptingBound(index: int, values: list[float], choice_rule, allowed_diff: float) -> float:
    chosen_values = choice_rule(values)
    low_bound = 0
    high_bound = 0
    # if he is already accepted the high bound is his value
    if chosen_values[index]:
        high_bound = values[index]
    # If he is not accepted find some higher bound
    else:
        high_bound, low_bound = FindSomeHighBound(choice_rule, index, values)
    return FindBoundWithDiff(allowed_diff, choice_rule, high_bound, index, low_bound, values)


# Find some bound that player i will be accepted
def FindSomeHighBound(choice_rule, index, values):
    while not choice_rule(values)[index]:
        values[index] = values[index] * 2
    return values[index], round(values[index] / 2)


# Find the bound with allowed difference.
def FindBoundWithDiff(allowed_diff, choice_rule, high_bound, index, low_bound, values):
    while low_bound != high_bound - allowed_diff:
        values[index] = round((high_bound + low_bound) / 2, 2)
        if choice_rule(values)[index]:
            high_bound = round((high_bound + low_bound) / 2, 2)
        else:
            low_bound = round((high_bound + low_bound) / 2, 2)
    return high_bound


vals = [1, 5, 11, 20]

print(payments(vals, lambda l: [i > 10 for i in l]))


def greatestthreevalues(values: list[float]) -> list[bool]:
    threelarget = heapq.nlargest(3, values)
    return [True if values[i] in threelarget else False for i in range(len(values))]


print(payments(vals, greatestthreevalues))
