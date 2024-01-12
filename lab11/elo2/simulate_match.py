def simulate(a,b):
    import random
    p1=a
    draw=b
    #p2=1-draw-p1
    result = random.uniform(0,1)
    if result<p1:
        return 1
    elif result>p1+draw:
        return 2
    else:
        return 0
