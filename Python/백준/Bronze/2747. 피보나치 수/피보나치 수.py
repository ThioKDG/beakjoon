def fibo(num):
    if mem[num] == -1:
        mem[num] = fibo(num-1) + fibo(num-2)

    return mem[num]

N = int(input())
mem = [0, 1] + [-1] * (N-1)
print(fibo(N))