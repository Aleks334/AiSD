import random

def generate_sequences(k, lower_bound=1, upper_bound=100):
    sequences_dict = {
        'random': [],
        'ascending': []
    }

    for _ in range(random.randint(10, 15)):
        n = random.randint(10, k)

        random_sequence = [random.randint(lower_bound, upper_bound) for _ in range(n)]
        sequences_dict['random'].append(random_sequence)

        sorted_sequence = sorted(random_sequence)
        sequences_dict['ascending'].append(sorted_sequence)

    return sequences_dict


if __name__ == "__main__":
    k = 20
    sequences = generate_sequences(k)
    print(sequences)