"""
Greedily selects subsets to cover the universe.

Parameters:
    universe (set): The set of elements to be covered.
    subsets (list of sets): The list of subsets available for covering.

Returns:
    list: A list of selected subsets that cover the universe.
"""

def set_cover(universe, subsets):
    covered = set()
    selected_subsets = []

    while covered != universe:
        # Select the subset that covers the most uncovered elements
        best_subset = max(subsets, key=lambda s: len(s - covered), default=None)
        if best_subset is None:
            break  # No more subsets can be added
        selected_subsets.append(best_subset)
        covered.update(best_subset)
        subsets.remove(best_subset)

    return selected_subsets

# Example usage
if __name__ == "__main__":
    universe = {1, 2, 3, 4, 5}
    subsets = [{1, 2}, {2, 3}, {3, 4}, {4, 5}, {1, 5}]
    
    result = set_cover(universe, subsets)
    print("Selected subsets:", result)
    print("Covered elements:", set().union(*result))
    
# k ln n
