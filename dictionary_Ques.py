##Ques1.
s ="Python is easy and python is very easy"
words = s.split()
count ={}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
##Ques2.
student = {
    "Isha":56,
    "Yamini":89,
    "Pallvi":90,
    "Ruhi":98,
    }
total =sum(student.values())
average = total / len(student)
print("average marks: ",average)
print(total)
##Ques3.
dict1 = {'a': 50, 'b': 30, 'c': 70}
dict2 = {'b': 60, 'c': 65, 'd': 40}

result = dict1.copy()

for key, value in dict2.items():
    if key in result:
        result[key] = max(result[key], value)
    else:
        result[key] = value

print(result)
##Ques4.
data = {
    'name': 'Alice',
    'city': 'Bangalore',
    'course': 'Data Science'
}

max_key = ""
max_length = 0

for key, value in data.items():
    if len(value) > max_length:
        max_length = len(value)
        max_key = key

print(max_key)
##Ques5.
votes = {
    "Alice": 450,
    "Bob": 120,
    "Charlie": 600,
    "David": 300,
    "Eva": 80
}

# New dictionary for filtered votes
filtered_votes = {}

# Filter values between 100 and 500
for name, count in votes.items():
    if 100 <= count <= 500:
        filtered_votes[name] = count

print(filtered_votes)
##Ques6.
data = {'a': 10, 'b': 20, 'c': 30}
update = {'b': 200, 'c': 300}

for key in update:
    if key in data:
        data[key] = update[key]

print(data)