class Vec:
    """A simple vector/point in 2D. Also used as a point (position from origin)."""
    point_num = 0
    box_calls = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Auto-generate a label for plotting/debugging
        self.label = 'P' + str(Vec.point_num)
        Vec.point_num += 1

    def __add__(self, other):
        """Vector addition."""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction."""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Scalar multiplication."""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product."""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """Squared length (avoids sqrt when only comparisons are needed)."""
        return self.dot(self)

    def in_box(self, bottom_left, top_right):
        """
        True iff this point lies within or on the boundary of the axis-aligned
        rectangle defined by bottom_left and top_right.
        """
        Vec.box_calls += 1
        return (bottom_left.x <= self.x <= top_right.x and
                bottom_left.y <= self.y <= top_right.y)

    def __getitem__(self, axis):
        """Indexing by axis: 0 -> x, 1 -> y (used by k-d splitting)."""
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"
        
    def __lt__(self, other):
        """Total order for stable sorting (x, then y)."""
        return (self.x, self.y) < (other.x, other.y)


class KdTree:
    """A 2D k-d tree for range queries (axis-aligned rectangles)."""
    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25

    def __init__(self, points, depth=0, max_depth=10):
        """
        Build a k-d tree from a list of Vec points.

        """
        if len(points) < 2 or depth >= max_depth:
            # Leaf: store the remaining points (at least one).
            self.is_leaf = True
            self.points = points
        else:
            # Internal node: choose axis and split on median coordinate.
            self.is_leaf = False
            self.axis = depth % 2                  # 0 = vertical split (x), 1 = horizontal (y)
            points = sorted(points, key=lambda p: p[self.axis])
            halfway = len(points) // 2
            # Split coordinate is taken from the left median (stable, deterministic)
            self.coord = points[halfway - 1][self.axis]
            # Recursively build children
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop   = KdTree(points[halfway:], depth + 1, max_depth)
            
    def points_in_range(self, query_rectangle):
        """
        Return all points within/on the axis-aligned query rectangle.

        """
        bottom_left, top_right = query_rectangle

        if self.is_leaf:
            # Check each stored point against the rectangle
            return [p for p in self.points if p.in_box(bottom_left, top_right)]
        else:
            matches = []
            if self.axis == 0:
                # Vertical split line at x = self.coord
                # If the rectangle extends to the right of the split, search right subtree
                if top_right.x >= self.coord:
                    matches += self.rightortop.points_in_range(query_rectangle)
                # If the rectangle extends to the left of the split, search left subtree
                if bottom_left.x <= self.coord:
                    matches += self.leftorbottom.points_in_range(query_rectangle)
            else:
                # Horizontal split line at y = self.coord
                if top_right.y >= self.coord:
                    matches += self.rightortop.points_in_range(query_rectangle)
                if bottom_left.y <= self.coord:
                    matches += self.leftorbottom.points_in_range(query_rectangle)
            return matches

    def plot(self, axes, top, right, bottom, left, depth=0):
        """
        Plot the kd-tree decomposition on a provided matplotlib Axes.

        Draws split lines at internal nodes and points at leaves.
        """
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(
                        p.label, (p.x, p.y),
                        xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y)
                    )
        else:
            if self.axis == 0:
                # Vertical split at x = self.coord
                axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                # Horizontal split at y = self.coord
                axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth + 1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)
       
    def __repr__(self, depth=0):
        """Readable tree dump: Node(axis, coord, left, right) or Leaf([...])."""
        if self.is_leaf:
            return depth * 2 * ' ' + f"Leaf({self.points})"
        else:
            s = depth * 2 * ' ' + f"Node({self.axis}, {self.coord}, \n"
            s += self.leftorbottom.__repr__(depth + 1) + '\n'
            s += self.rightortop.__repr__(depth + 1) + '\n'
            s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            return s


# --- Small test ---
if __name__ == "__main__":
    point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
    points = [Vec(*tup) for tup in point_tuples]
    tree = KdTree(points)

    # Query rectangle: bottom_left=(0, 3), top_right=(5, 19)
    in_range = tree.points_in_range((Vec(0, 3), Vec(5, 19)))
    print(sorted(in_range))  # Deterministic via Vec.__lt__
