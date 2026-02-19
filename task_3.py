class PointsForPlace:

    def __init__(self):
        self.points = 0

    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            return 101 - place

class PointsForMeters:
    def __init__(self):
        self.points = 0

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            return  meters * 0.5

class TotalPoints(PointsForPlace, PointsForMeters):
    
    def __init__(self):
        PointsForPlace.__init__(self) 
        PointsForMeters.__init__(self)

    def get_total_points(self, place, meters):
        place_point = self.get_points_for_place(place)
        meters_point = self.get_points_for_meters(meters)
        total = place_point + meters_point
        return total
    

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_place(200))
print(total_points.get_points_for_place(0.5))
print(total_points.get_points_for_meters(10))
print(total_points.get_points_for_meters(-1))
print(total_points.get_total_points(100, 10)) 