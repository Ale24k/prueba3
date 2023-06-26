T = int(input())

for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    fastest_return_award_count = 0

    for i in range(1, N+1):
        faster_count = sum(1 for p in P if p < P[i-1])
        return_count = sum(1 for p in P if p < 2*P[i-1])

        if faster_count == return_count:
            fastest_return_award_count += 1

    print(fastest_return_award_count)