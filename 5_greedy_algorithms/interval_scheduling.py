import heapq
import sys

# input = sys.stdin.readline
# print = sys.stdout.write

def greedy(n, all_list): # 최대한 많은 강의 수
    all_list.sort(key=lambda x: x[0]) # 시작하는 시간을 기준으로 정렬
    all_list.sort(key=lambda x: x[1]) # 끝나는 시간을 기준으로 정렬
    endtime = 0
    count = 0
    for i in range(n):
        if endtime <= all_list[i][0]:
            endtime = all_list[i][1]
            count += 1
    return count

def greedy2(n, all_list): # 최대한 적은 강의실 수
    all_list.sort(key=lambda x: x[0]) # 시작 시간 기준으로 정렬
    
    heap = []  # 최소 힙
    for start, end in all_list:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)
    

