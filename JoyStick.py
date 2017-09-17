import collections

# implements a joystick of sorts by converting booleans to 0 or 1 and then adding their decimal values to get the combinations below...
# e.g. 1000 = up = 16,  0001 = right = 1
JoyStick = collections.namedtuple(
    'JoyStick', 'up down left right upright upleft downright downleft')

joystick = JoyStick(16, 8, 4, 1, 17, 20, 9, 12)
