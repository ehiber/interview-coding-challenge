def reduce_gifts(prices=[], k=3, threshold=14):
    prices.sort(reverse=True)
def reduce_gifts(prices=[], k=3, threshold=14):
    """
    Hidden solution: iteratively remove the largest element from the first
    k-window (in the current array) that exceeds the threshold until all
    k-windows have sum <= threshold. Returns the number of removed items.
    This is a straightforward (but not optimal for huge inputs) approach
    useful for testing and demonstration.
    """
    if prices is None:
        prices = []
    arr = list(prices)
    removed = 0

    # Edge cases
    if k <= 0:
        return 0

    # Keep removing until no window of size k exceeds threshold
    while True:
        n = len(arr)
        if n < k:
            break

        found = False
        for i in range(0, n - k + 1):
            window = arr[i:i+k]
            s = sum(window)
            if s > threshold:
                # remove the largest element in this window
                max_val = max(window)
                idx = i + window.index(max_val)
                arr.pop(idx)
                removed += 1
                found = True
                break

        if not found:
            break

    return removed


if __name__ == '__main__':
    prices = [3, 2, 1, 4, 6, 5]
    k = 3
    threshold = 14
    print(reduceGifts(prices, k, threshold))