class PointAnalyzer:
    def __init__(self, window_height):
        self.window_height = window_height

    def is_point_above_center(self, point_y):
        center = self.window_height / 2
        return point_y < center
