nums = []
count = 0
cluster = 0

while len(nums) < 10:
        try:
            nums.append(int(input("Enter a number: ")))
        except ValueError:
            print("Must be a numeric value")

for i in range(0,10):
    if nums[i] % 2 == 0:
        count = count+1
    elif count > 1:
        cluster = cluster+1
        count = 0
    else:
        count = 0
if count > 1:
    cluster = cluster+1

print(cluster)
print(len(nums))