# nums = [1, 1, 1, 2, 2, 3, 4, 5, 5]
# # output = [1, 1, 2, 2, 3, 4, 5, 5]
# k = len(nums)
#
# for i in range(k - 1):
#     for j in range(0, i):
#         if nums[i] == nums[j] and nums[i] == nums[j+1]:
#             nums.pop(nums[j])
#             k -= 1
# print(nums)

"""
licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
output = "steps"

filter_data = ''
map = {}

licensePlate = licensePlate.replace(' ', '').lower()
for word in licensePlate:
    if word.isalpha():
        filter_data += word

# print(filter_data)
for word in words:
    map[word] = 0
"""

words = ["flower", "flow", "flying"]
# Output = "fl"

words = sorted(words)
new_words = []
w = ''
for i in words[0]:
    new_words.append(i)
print(new_words)
for i in range(len(words)-2):
    for j in range(len(new_words)):
        if new_words[j] == words[i+1][j] and new_words[j] == words[i+1][j] and new_words[j] == words[i+2][j]:
            if new_words[j] is not w:
                w += new_words[j]

print(w)