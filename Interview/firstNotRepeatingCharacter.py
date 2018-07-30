'''Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.

Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.'''


def firstNotRepeatingCharacter(s):
    aset=list(set(s))
    cmd=list(s)
    check=list(s)

    for i in aset:
        cmd.remove(i)
    for j in check:
        if j not in cmd:
            return j
    return '_'
