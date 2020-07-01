GEAR_LEAST_RADIUS = 1

def solution(pegs):
    drive_gear_max_radius = pegs[1] - pegs[0]
    pegs_length = len(pegs)

    for radius in range(GEAR_LEAST_RADIUS, drive_gear_max_radius):
        gears_radii = [radius]

        for index in range(1, pegs_length):
            peg_in_instance = pegs[index]
            prior_peg = 0 if index == 0 else pegs[index - 1]
            latter_peg = 0 if index == pegs_length - 1 else pegs[index + 1]

            prior_gear_radius = radius if index == 0 else gears_radii[index - 1]

            distance_to_prior_peg = peg_in_instance - prior_peg
            distance_to_latter_peg = abs(latter_peg - peg_in_instance)

            gear_radius = distance_to_prior_peg - prior_gear_radius

            gears_radii.append(gear_radius)

            if gear_radius > distance_to_latter_peg - GEAR_LEAST_RADIUS: 
                break
        else:
            if float(gears_radii[-1]) / float(gears_radii[0]) == 0.5:
                return [gears_radii[0], 1]
                
            if radius + 1 == 2 * gears_radii[-1]:
		print(gears_radii, '<-')
                return [(radius * 3) + 1, 3]
            if radius + 2 == 2 * gears_radii[-1]:
		print(gears_radii , '-')
                return [(radius * 3) + 2, 3]

    return [-1, -1]

print(solution([4,10, 16, 20, 30, 40])) #46, 56, 80, 90]))
print(solution([4, 10, 40, 50]))
print(solution([4, 10, 30, 50, 54]))
print(solution([4, 10, 30, 50]))
print(solution([4, 24, 30]))
print(solution([4, 30, 38]))
print(solution([4, 16]))
print(solution([4, 10]))
print(solution([4, 30, 50]))
print(solution([4, 17, 50]))
