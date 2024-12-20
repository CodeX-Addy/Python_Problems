#itertools.product()
from itertools import product 
print(*product(list(map(int,input().split())),list(map(int,input().split()))))

#itertools.permutations()
from itertools import permutations
S, k = input().split()
print('\n'.join(sorted(map(''.join,permutations(S,int(k))))))
