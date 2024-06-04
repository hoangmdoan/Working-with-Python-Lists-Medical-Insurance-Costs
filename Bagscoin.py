QUARTER_DIAMETER = 24
DIME_DIAMETER = 18
NICKEL_DIAMETER = 21
PENNY_DIAMETER = 19

def tally_coins(bag_of_coins):
    """Sorts and counts coins by denomination."""
    counts = [0, 0, 0, 0, 0]  # quarter, dime, nickel, penny, foreign
    for coin in bag_of_coins:
        if coin == QUARTER_DIAMETER:
            counts[0] += 1
        elif coin == DIME_DIAMETER:
            counts[1] += 1
        elif coin == NICKEL_DIAMETER:
            counts[2] += 1
        elif coin == PENNY_DIAMETER:
            counts[3] += 1
        else:
            counts[4] += 1
    return counts

def calculate_bag_value(coin_counts):
    """Calculates the total value of the bag in dollars."""
    return (
        coin_counts[0] * 0.25
        + coin_counts[1] * 0.10
        + coin_counts[2] * 0.05
        + coin_counts[3] * 0.01
    )

def display_results(coin_counts):
    """Displays the coin tally and total value."""
    print("The bag contains the following coins:")
    print(f"Quarter: {coin_counts[0]}")
    print(f"Dime: {coin_counts[1]}")
    print(f"Nickel: {coin_counts[2]}")
    print(f"Penny: {coin_counts[3]}")
    print(f"Foreign: {coin_counts[4]}")
    total_value = calculate_bag_value(coin_counts)
    print(f"Total value in the bag: ${total_value:.2f}")

def main():
    """Creates a bag of coins and processes it."""
    bag_of_coins = [
        19, 21, 20, 19, 18, 20, 19, 24, 25, 19, 24, 18, 23, 21, 19, 24, 18, 21,
        19, 24, 18, 21, 30, 32, 24,
    ]
    coin_counts = tally_coins(bag_of_coins)
    display_results(coin_counts)

if __name__ == "__main__":
    main()
