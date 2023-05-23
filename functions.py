import random as rd

def rand_left(size):
    return (-5,rd.randint(0,size[1]))

def rand_right(size):
    return (size[0],rd.randint(0,size[1]))

def rand_top(size):
    return (rd.randint(0,size[0]),-5)

def rand_bottom(size):
    return (rd.randint(0,size[0]),size[1])

def choice(*args):
    return rd.choice(args)

def gen_text(time: list):
    return f'{0 if time[0] <= 9 else ""}{time[0]}:{0 if time[1] <= 9 else ""}{time[1]}:{0 if time[2] <= 9 else ""}{time[2]}'    
