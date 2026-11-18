import threading

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

def sum_range(thread_id, start, end, result):
    result[thread_id] = sum(range(start, end + 1))

n = len(ranges)
result = [0] * n
threads = []

for i, (start, end) in enumerate(ranges):
    t = threading.Thread(target=sum_range, args=(i, start, end, result))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(result)
print(sum(result))