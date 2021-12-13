class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        string = "(" + str(self.value) + "; "
        if self.left or self.right:
            string += str(self.left) + "; "
            if self.right:
                string += str(self.right) + "; "
        return string[:-2] + ")"
