import heapq

class Node:
    def __init__(self, left=None, right=None, symbol = "_", freq=0):
        self.left = left
        self.right = right
        self.symbol = symbol
        self.freq = freq
        

def huffman_encoding(symbols, freqs):
    heap = []
    
    for i in range(len(symbols)):
        node = Node(symbol = symbols[i], freq = freqs[i])
        heapq.heappush(heap, [freqs[i], node])
        
    for i in range(len(symbols) - 1):
        _, i = heapq.heappop(heap)
        _, j = heapq.heappop(heap)
        
        node = Node(left = i, right = j, freq = i.freq + j.freq)
        
        heapq.heappush(heap, [node.freq, node])
        
    print("Huffman Tree:")
    print("Symbol\tFrequency")
    print("-------\t---------")
    for symbol in symbols:
        print(f"{symbol}\t{freqs[symbols.index(symbol)]}")
    
        
sybols = ["a", "b", "c", "d", "e", "f"]
freqs = [5, 9, 12, 13, 16, 45]

huffman_encoding(sybols, freqs)
