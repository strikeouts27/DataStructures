# FUNCTION recursive_function(input_data):
#     // ------------------------------------------------------------------
#     // STEP 1: BASE CASE (Stopping Condition)
#     // Identify the absolute smallest input where the answer is known instantly.
#     // ------------------------------------------------------------------
#     IF condition_is_met(input_data) THEN:
#         RETURN default_or_known_value
#     END IF

def main():
    numbers_list = [1, 2, 4, 5, 7, 11, 16, 23, 34, 50, 73, 100]
    insertion_point = 10
    n = int(input("Hello user, please input a number to call this function."))
    skip_fib(numbers_list, n)
    print(f"The term at position {n} is: {numbers_list[n]}")

"""
The 4-Step Process for Finding a Base Case
Identify the State Variables: Look at the parameters changing on each call. In your function signature recursive_function(numbers, insertion_point), those are numbers (the list) and insertion_point (an index or target value).
Find the Smallest Valid Input: Ask, "What is the most reduced form of this data?" For a list, it’s an empty list len(numbers) == 0 or a single-item list len(numbers) == 1. For an index, it’s reaching 0 or len(numbers) - 1.
Identify the Out-of-Bounds Condition: Ask, "When has the algorithm gone too far?" For searching or insertion problems, this happens when an index moves beyond list boundaries (e.g., insertion_point >= len(numbers) or insertion_point < 0).
Determine the Immediate Return Value: Ask, "What answer requires zero computation at this stopping point?" (e.g., returning 0, True/False, or the modified list itself).
"""
def skip_fib(numbers, n):
    if numbers is None or len(numbers) == 0:
        numbers = [1, 2, 4, 5, 7, 11, 16, 23, 34, 50, 73, 100]

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    else:
        return skip_fib(numbers, n - 1,)

    numbers[n] = skip_fib(n - 1, numbers) + skip_fib(n - 3, numbers)
    return numbers[n]


if __name__ == "__main__":
    main()
        # ------------------------------------------------------------------
        # STEP 1: BASE CASE (Stopping Condition)
        # Identify the absolute smallest input where the answer is known instantly.
        # ------------------------------------------------------------------

#     // STEP 2: PREPARATION & RECURSIVE STEP
#     // Modify input_data so it strictly moves closer to the base case,
#     // then call the function again with the smaller input.
#     // ------------------------------------------------------------------
#     smaller_input = modify_or_shrink(input_data)
#     result_from_subproblem = recursive_function(smaller_input)

#     // ------------------------------------------------------------------
#     // STEP 3: COMBINE & RETURN
#     // Combine work done at the current level with the recursive result.
#     // ------------------------------------------------------------------
#     final_result = combine(current_work, result_from_subproblem)
#     RETURN final_result

# END FUNCTION


# // ----------------------------------------------------------------------
# // MAIN EXECUTION / ENTRY POINT
# // ----------------------------------------------------------------------
# FUNCTION main():
#     initial_data = get_user_input_or_test_data()
#     output = recursive_function(initial_data)
#     PRINT(output)
# END FUNCTION