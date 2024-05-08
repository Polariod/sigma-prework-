def main(Num_list):
    max = Num_list[0]
    min = Num_list[0]
    for num in Num_list:
        if num > max:
            max = num
        if num < min:
            min = num
    return [min, max]
