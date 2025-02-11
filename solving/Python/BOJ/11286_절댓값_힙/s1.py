# BOJ_11286. 절댓값 힙
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    input_num = int(input())
    if input_num != 0:
        heappush(heap, -input_num)
    else:
        try:
            print(-heappop(heap))
        except:
            print(0)
