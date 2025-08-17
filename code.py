import math

def PRV():
    """
    Calculates the minimum Product-Requirement Variance (PRV) for a
    set of products using dynamic programming.
    """
    print("Input No. of types of different products: ", end="")
    n = int(input())  # No. of different products

    arr = [0] * (n + 1)  # Array to store product requirements for each type
    tstages = 0  # Total number of stages
    base = 2  # Base system to encode intermediate stages
    fstage = 0  # Encoded value of our final state

    print("Input requirements:")
    requirements_str = input()
    requirements = list(map(int, requirements_str.split()))

    for i in range(1, n + 1):
        arr[i] = requirements[i - 1]
        tstages += arr[i]
        base = max(base, arr[i] + 1)

    # Calculates the encoded value of final state
    for i in range(1, n + 1):
        fstage += arr[i] * (base**(i - 1))

    # Debug info
    print(f"Total stages: {tstages}")
    print(f"Encoding Base: {base}")
    print(f"Encoded value of the final stage: {fstage}")

    # DP array
    dp = [[float('inf')] * (fstage + 5) for _ in range(tstages + 5)]

    # Base case
    dp[0][0] = 0.0

    # Iterate through each stage
    for i in range(1, tstages + 1):
        # Iterate through every encoded intermediate state
        for j in range(1, fstage + 1):
            total_variance = 0.0
            cur = j
            flag = True

            # Decode the value and compute variances
            for exp in range(1, n + 1):
                val = cur % base
                cur //= base

                if val > arr[exp]:
                    flag = False
                    break

                dev = val - ((i * arr[exp]) / tstages)
                variance = dev * dev
                total_variance += variance

            if not flag:
                continue

            # Transition state
            k = 1
            for exp in range(1, n + 1):
                if ((j // k) % base) >= 1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + total_variance)
                k *= base

    print(f"Min PRV: {dp[tstages][fstage]}")

if __name__ == "__main__":
    PRV()
