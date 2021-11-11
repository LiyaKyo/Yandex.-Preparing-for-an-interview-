def gen_par(pars: str, p_count: int, left: int, right: int):
    if left == p_count and right == p_count:
        print(pars)
    else:
        if left < p_count:
            gen_par(pars + '(', p_count, left + 1, right)
        if right < left:
            gen_par(pars + ')', p_count, left, right + 1)


gen_par('', int(input()), 0, 0)
