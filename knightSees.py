def knightSees(pos,size):
    """Return a list of all squares "In view" of a knight in the position pos on a board of size"""
    inView = []
    appendIfInBounds(inView, pointShift(pos, 2, 1), size)
    appendIfInBounds(inView, pointShift(pos, 2, -1), size)
    appendIfInBounds(inView, pointShift(pos, 1, 2), size)
    appendIfInBounds(inView, pointShift(pos, 1, -2), size)
    appendIfInBounds(inView, pointShift(pos, -1, 2), size)
    appendIfInBounds(inView, pointShift(pos, -1, -2), size)
    appendIfInBounds(inView, pointShift(pos, -2, 1), size)
    appendIfInBounds(inView, pointShift(pos, -2, - 1), size)
    return inView
