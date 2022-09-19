def check_pnr(pnr):
    control_number = pnr[9]
    #print(control_number)
    result_pnr = round_pnr(sum_pnr(split_pnr(multiply_pnr(pnr[:9]))))
    return result_pnr == control_number

def multiply_pnr(pnr):
    for i in range(len(pnr)):
        if i % 2 == 0:
            pnr[i] = pnr[i] * 2
    return pnr

def split_pnr(multiply_pnr):
    for i in multiply_pnr:
        if i % 10 == i - 10:
            first_number = i - 10
            multiply_pnr.append(first_number)
            multiply_pnr.append(1)
            multiply_pnr.remove(i)
    return multiply_pnr

def sum_pnr(split_pnr):
    summed_pnr = 0
    for i in split_pnr: 
        summed_pnr += i        
    return summed_pnr

def round_pnr(sum_pnr):
    nearest_higher_ten = int((sum_pnr+9)/10)*10
    result_pnr = nearest_higher_ten - sum_pnr
    return result_pnr

print(check_pnr([7,0,0,7,0,8,6,6,6,8]))