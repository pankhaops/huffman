import heapq

class Node:
    def __init__(self, char, freq):
        self.char, self.freq = char, freq
        self.left = self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def print_codes(r, code=""):
    if r:
        if r.char:
            print(r.char, ":", code)
        print_codes(r.left, code+"0")
        print_codes(r.right, code+"1")

def huffman(chars, freqs):
    q = [Node(c,f) for c,f in zip(chars,freqs)]
    heapq.heapify(q)

    while len(q) > 1:
        a, b = heapq.heappop(q), heapq.heappop(q)
        n = Node(None, a.freq+b.freq)
        n.left, n.right = a, b
        heapq.heappush(q,n)

    print("--- Huffman Codes ---")
    print_codes(q[0])

chars = ['A','B','C','D','E','F']
freqs = [5,9,12,13,16,45]
huffman(chars,freqs)

#activities
def activity_selection(a):
    a.sort(key=lambda x:x[1])
    selected = [a[0]]
    finish = a[0][1]

    for s,e in a[1:]:
        if s >= finish:
            selected.append((s,e))
            finish = e
    return selected

a = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),
     (6,10),(8,11),(8,12),(2,14),(12,16)]

r = activity_selection(a)
print("Maximum number of activities:",len(r))
print("Selected Activities:",r)
