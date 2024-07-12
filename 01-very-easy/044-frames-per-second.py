"""
Frames Per Second

Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.

Examples
frames(1, 1) ➞ 60

frames(10, 1) ➞ 600

frames(10, 25) ➞ 15000

Notes
FPS stands for "frames per second" and it's the number of frames a computer screen shows every second.
"""



from edatest import Edatest
Test = Edatest()

def frames(minutes, fps):
    return minutes*fps*60

if __name__ == '__main__':
    Test.assert_equals(frames(1, 1), 60)
    Test.assert_equals(frames(10, 1), 600)
    Test.assert_equals(frames(10, 25), 15000)
    Test.assert_equals(frames(500, 60), 1800000)
    Test.assert_equals(frames(0, 60), 0)
    Test.assert_equals(frames(99, 1), 5940)
    Test.assert_equals(frames(419, 70), 1759800)
    Test.assert_equals(frames(52, 33), 102960)