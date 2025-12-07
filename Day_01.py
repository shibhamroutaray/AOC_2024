arr1 = []
arr2 = []

with open("day_01.txt") as f:
    for line in f:
        a, b = map(int, line.split())
        arr1.append(a)
        arr2.append(b)
arr1.sort()
arr2.sort()
final_array = []

for i in range(len(arr1)):
    diff = abs(arr1[i] - arr2[i])
    final_array.append(diff)


print(f"Total distance is {sum(final_array)}")

#---------------------------PART-02--------------------------------
s_score = []

for i in range(len(arr1)):
    score = arr1[i] * arr2.count(arr1[i])
    s_score.append(score)
print(f"The similarity score is {sum(s_score)}")