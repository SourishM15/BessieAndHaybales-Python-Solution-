def total_haybales(N, T, deliveries):

    total = 0
    current_day = 1
    index = 0
    eaten = 0

    while current_day <= T:
        if index < N and current_day == deliveries[index][0]:
            total += deliveries[index][1]
            index += 1

        if total > 0:
            eaten += 1
            total -= 1

        current_day += 1
    return eaten
  
# Read input
N, T = map(int, input().split())
deliveries = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
result = total_haybales(N, T, deliveries)
print(result)
