GEAR_LEAST_RADIUS = 1

def solution(pegs):
    total_radius_space = pegs[-1] - pegs[0]
    drive_gear_max_radius = pegs[1] - pegs[0] - GEAR_LEAST_RADIUS

    for radius in range(drive_gear_max_radius, 0, -1):
        gears_radius = [radius]
        drive_gear_radius = gears_radius[0] 
        remaining_radius_space = total_radius_space 
        remaining_radius_space = abs(remaining_radius_space - drive_gear_radius) 

        for index in range(1, len(pegs) - 1):
            driven_gear_max_radius = pegs[index + 1] - pegs[index] - GEAR_LEAST_RADIUS 
            driven_gear_radius = abs(remaining_radius_space - driven_gear_max_radius - 1)  

            if driven_gear_radius > driven_gear_max_radius:
                continue

            remaining_radius_space = abs(remaining_radius_space - (driven_gear_radius * 2))
            gears_radius.append(driven_gear_radius)

        output_gear_radius = remaining_radius_space
        gears_radius.append(output_gear_radius)

        if float(output_gear_radius) / float(drive_gear_radius) == 0.5:
            return [drive_gear_radius, 1]

    return [-1, -1]

print(solution([1, 16]))
print(solution([1, 18, 20]))
print(solution([4, 30, 50]))
print(solution([4, 17, 50]))
print(solution([6, 32, 52]))
print(solution([1, 30, 44, 55, 34]))
#assert solution([4, 30, 50]) == [12, 1]
#assert solution([4, 17, 50]) == [-1, -1]

