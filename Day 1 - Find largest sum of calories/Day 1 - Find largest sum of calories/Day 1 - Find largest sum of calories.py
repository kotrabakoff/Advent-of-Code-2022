list = []
current_list = []
current = input()

while True:
    if current.isdigit() and current != " ":
        current_list.append(int(current))
    else:
        current = input()
        list.append(int(sum(current_list)))
        current_list = []
        continue
    if current == "11517":
        break
    current = input()

print(max(list))

