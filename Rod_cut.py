import random
import time

# Function to solve the rod cutting problem using dynamic programming (bottom-up approach)
def extended_bottom_up_cut_rod(prices, rod_length):
    # Initialize arrays to store maximum revenue and optimal cuts
    r = [None] * (rod_length + 1)
    optimal_cut = [None] * (rod_length + 1)
    r[0] = 0
    
    # Loop through each rod length
    for j in range(1, rod_length + 1):
        max_revenue = float('-inf')
        # Find the optimal cut for the current rod length
        for i in range(j):
            if max_revenue < prices[i] + r[j - i - 1]:
                max_revenue = prices[i] + r[j - i - 1]
                optimal_cut[j] = i + 1
        # Store the maximum revenue for current rod length
        r[j] = max_revenue
    # Return the maximum revenue and optimal cuts
    return r[rod_length], optimal_cut[1:]

# Function to solve the rod cutting problem using memoization (top-down approach)
def memorized_cut_rod(prices, rod_length, memo):
    if rod_length in memo:
        return memo[rod_length]
    if rod_length <= 0:
        return 0, []
    else:
        max_revenue = float('-inf')
        optimal_cut = []
        # Find the optimal cut recursively and store results in memoization table
        for i in range(1, rod_length + 1):
            revenue, cuts = memorized_cut_rod(prices, rod_length - i, memo)
            total_revenue = prices[i - 1] + revenue
            if total_revenue > max_revenue:
                max_revenue = total_revenue
                optimal_cut = [i] + cuts
        memo[rod_length] = (max_revenue, optimal_cut)
        return memo[rod_length]

# Function to solve the rod cutting problem using recursive approach
def recursive_cut_rod(prices, rod_length):
    if rod_length == 0:
        return 0, []
    max_revenue = float('-inf')
    optimal_cut = -1
    # Find the optimal cut recursively
    for i in range(rod_length):
        revenue, cuts = recursive_cut_rod(prices, rod_length - i - 1)
        total_revenue = prices[i] + revenue
        if total_revenue > max_revenue:
            max_revenue = total_revenue
            optimal_cut = [i + 1] + cuts
    return max_revenue, optimal_cut

# Function to create a file with randomly generated prices
def create_prices(file_name, n, seed):
    random.seed(seed)
    with open(file_name, 'w') as f:
        f.write(f"{n}\n")
        prices = [random.randint(1, 30) for _ in range(n)]
        f.write(" ".join(map(str, prices)) + "\n")

# Function to read prices from a file
def read_prices(file_name):
    with open(file_name, 'r') as f:
        n = int(f.readline())
        prices = list(map(int, f.readline().split()))
    return n, sorted(prices)

if __name__ == "__main__":
    rod_lengths = [5, 10, 20, 30]
    algos = {
        "Recursive": recursive_cut_rod,
        "Dynamic programming bottom-up": extended_bottom_up_cut_rod,
        "Memorized": memorized_cut_rod
    }

    seed = 93  # Seed for random number generation
    for length in rod_lengths:
        # Generate prices file for each rod length
        create_prices(f"price{length}.txt", length, seed)
        print("-------------------------------------------")
        print(f"\nRod length: {length}")
        # Read prices from file
        n, prices = read_prices(f"price{length}.txt")
        print("Length:", n)
        print("Prices:", prices)

        for name, algo in algos.items():
            start_time = time.time()
            if name == "Memorized":
                memo = {}
                max_revenue, optimal_cut = algo(prices, n, memo)
            else:
                max_revenue, optimal_cut = algo(prices, n)
            finish_time = time.time()
            execution_time = finish_time - start_time

            # Print results
            print(f"{name}:")
            print("Max revenue:", max_revenue)
            print("Optimal cuts:", optimal_cut)
            print("Execution Time:", execution_time, "seconds\n")
