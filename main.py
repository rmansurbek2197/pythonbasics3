def manfiy_sonlar(N):
    if N < 0:
        return [i for i in range(1, N+1) if i < 0]
    else:
        return []

print(manfiy_sonlar(-10))