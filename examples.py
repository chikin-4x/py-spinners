"""Examples demonstrating various spinners.

Attributes
----------
CLEAR_LINE : str
    To clear the current line
"""
import sys
import time
import cursor

from patterns import Patterns

CLEAR_LINE = '\033[K'


def animate(frames, interval, name, iterations=2):
    """Animate given frame for set number of iterations.

    Parameters
    ----------
    frames : list
        Frames for animating
    interval : float
        Interval between two frames
    name : str
        Name of animation
    iterations : int, optional
        Number of loops for animations
    """
    for i in xrange(iterations):
        for frame in frames:
            output = "\r{0} {1}".format(frame.encode('utf-8'), name)
            sys.stdout.write(output)
            sys.stdout.write(CLEAR_LINE)
            sys.stdout.flush()
            time.sleep(0.001 * interval)

try:
    cursor.hide()
    for pattern in Patterns:
        frames = pattern.value['frames']
        interval = pattern.value['interval']
        name = pattern.name
        animate(frames, interval, name)

    print '\n'
finally:
    cursor.show()