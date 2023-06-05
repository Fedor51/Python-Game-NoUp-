import random as rd
# for bullets
def rand_left(size):
    return (-5,rd.randint(0,size[1]))

def rand_right(size):
    return (size[0],rd.randint(0,size[1]))

def rand_top(size):
    return (rd.randint(0,size[0]),-5)

def rand_bottom(size):
    return (rd.randint(0,size[0]),size[1])

# for mini_boss
def b_rl(size):
    return (-20,rd.randint(0,size[1]))

def b_rt(size):
    return (rd.randint(0,size[0]),-20)

# for boss
def bb_rl(size):
    return (-50,rd.randint(0,size[1]))

def bb_rt(size):
    return (rd.randint(0,size[0]),-50)

# random choice and other
def choice(*args):
    return rd.choice(args)

def gen_text(time: list):
    return f'{0 if time[0] <= 9 else ""}{time[0]}:{0 if time[1] <= 9 else ""}{time[1]}:{0 if time[2] <= 9 else ""}{time[2]}'    

