"""
Problema: Kth Largest Element in an Array
Entrada: nums = [3,2,1,5,6,4], k = 2
Salida: 5
"""

import heapq
nums = [3,2,1,5,6,4]
k = 2
def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap[0]

comprobation = findKthLargest(nums, k)
print(comprobation)
