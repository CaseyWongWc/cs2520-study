import random
def unique_random_ints(how_many, max_num):
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""

    # Type your code here. #
    result = []
    global retries
    retries = 0
    while len(result) < how_many:
        num = random.randint(0, max_num)
        if num not in result:
            result.append(num)
        else:
            retries += 1
    return result



if __name__ == "__main__":
    seed = int(input())
    how_many = int(input())
    max_num = int(input())

    # Type your code here. #
    random.seed(seed)
    random_ints = unique_random_ints(how_many, max_num)
    print(*random_ints, f"retries={retries}")

