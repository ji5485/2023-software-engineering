from packages.Check import DetectHazardSpot, DetectColorBlobSpot

class SIM:
  def detect_sensor(self, map, robot):
    hazard = self.detect_hazard_sensor(map, robot)
    color_blob = self.detect_color_blob_sensor(map, robot)
    positioning = self.detect_positioning_sensor(robot)

    return { 'hazard': hazard, 'color_blob': color_blob, 'positioning': positioning }

  def detect_hazard_sensor(self, map, robot):
    return DetectHazardSpot().check(map, robot.get_sight_position())

  def detect_color_blob_sensor(self, map, robot):
    return DetectColorBlobSpot().check(map, robot.get_position())

  def detect_positioning_sensor(self, robot):
    return robot.get_position()
