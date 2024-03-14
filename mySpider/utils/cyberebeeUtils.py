others_el = {'Package included:', 'Details pictures:', 'Package Included:',
             'Specification:', 'Description:', 'Features:', 'More Details:', 'Package Include:'}


def handle_feature(str):
    # print(str)
    bullet_points = {}
    lines = str.splitlines(True)
    for index, line in enumerate(lines):
        if len(line.strip()) == 0:
            continue
        if line.strip() in others_el:
            # print(line)
            bullet_point = __handle_bullet_point(lines, index + 1)
            bullet_points[line.strip()] = bullet_point
            continue
    return bullet_points


def __handle_bullet_point(lines, start_index):
    bullet_point = []
    for i in range(start_index, len(lines)):
        if len(lines[i].strip()) == 0:
            continue
        if lines[i].strip() in others_el:
            break
        bullet_point.append(lines[i])
    return bullet_point


def handle_bullet_points(bullet_points):
    points = []
    cnt = 0
    for index, vale in enumerate(bullet_points):
        num = vale[0]
        # print("num=", num, "vale=", vale)
        if num.isdigit():
            # print("append")
            points.append(vale)
        else:
            # print("insert")
            cnt += 1
            points[index - cnt] = points[index - cnt] + vale
    return points
