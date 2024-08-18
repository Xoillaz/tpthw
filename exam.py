print()

tags = ["A", "B", "C"]
groups = [[f"{tags[i]}{j}" for j in range(1, 6)] for i in range(3)]

line = "A, B, C 组的人员组成如下：\n"
for i in range(3):
    line += "{} | {}\n".format(tags[i], groups[i])
print(line)

date = int(input("现开始排期，请输入开始日期：\n> "))

print("\n生成日程表如下：")
for i in range(5):
    line = f"{date+i} |"
    for j in range(3):
        line += f" {groups[j][i]}"

    print(line)

print()

# Additional Practice
# - - -
# [Your answer]
