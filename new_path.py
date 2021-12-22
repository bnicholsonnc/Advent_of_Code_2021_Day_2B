def main():
    file = open('input.txt', 'r')
    path = []
    aim = 0
    y = 0
    z = 0

    for line in file:
        entry = line.rstrip().split(' ')
        path.append(entry)

    for motion in path:
        if motion[0] == 'up':
            aim -= int(motion[1])
        elif motion[0] == 'down':
            aim += int(motion[1])
        else:
            y += int(motion[1])
            z += aim * int(motion[1])

    answer = y * z
    print(answer)



main()
