from objects.territory.territory import Territory
from tools.traingulating import triangulate_polygon
from tools.clustering import kmeans_clustering
from tools.polygons_action import multiply_polygon_vertices
from tools.colors import colors_dict
from objects.territory.zone import Zone
from objects.buldings.sport.sport_race import SportRace
from objects.buldings.sport.football_field import FootBallField
from objects.buldings.sport.volleyball_court import VolleyballCourt
from objects.buldings.sport.basketball_court import BasketballCourt
from objects.buldings.main_zone.shool_main import ShoolMain
from objects.buldings.main_zone.shool_junior import ShoolJunior
from objects.buldings.main_zone.meet_square import MeetSquare
from tools.decorators import retry_on_exception

from tools.polygons_action import place_rectangles
from tools.polygons_action import align_rectangles
from tools.polygons_action import get_random_dimensions
class Shool(Territory):



    zone_color_dict = {
        'main_zone': colors_dict['blue'],
        'sport_zone': colors_dict['green'],
        'meet_zone': colors_dict['navy'],
        'relax_zone': colors_dict['silver'],
        'ground_zone': colors_dict['chocolate']
    }
    @retry_on_exception(4)
    def total_rebuild(self):
        self.objects = []

        self.create_ground_polygon()
        self.devide_territory()
        self.build_zone()
        self.build_main_zone()
        self.build_sport_zone()

        print('End of total rebuild')

    def build_main_zone(self):
        current_zone = None
        for zone in self.zone_list:
            if zone.name == 'main_zone':
                current_zone = zone
                break
        if current_zone == None:
            return
        recktangles_to_place = []

        # self.bulding_main_zone = Building(self.levels_num, self.levels_hight, self.square_size)
        # self.bulding_main_zone.build(self.zone_list[0].center_coords)
        # self.objects.extend(self.bulding_main_zone.objects)
        meet_square_size = get_random_dimensions( self.configuration['human_capacity']*0.3*0.001)
        recktangles_to_place.append(meet_square_size)

        if self.configuration['has_junior'] and not(self.configuration['has_junior_hight_connection']):
            shool_size = get_random_dimensions(
                0.001 * self.configuration['square_size'] / self.configuration['levels_num']/2)
            shool_size_jun = get_random_dimensions(
                0.001 * self.configuration['square_size'] / self.configuration['levels_num'] / 2)
            recktangles_to_place.append(shool_size_jun)
        else:
            shool_size = get_random_dimensions(0.001*self.configuration['square_size']/self.configuration['levels_num'])
        recktangles_to_place.append(shool_size)

        self.shool_main = ShoolMain(self.levels_num, self.levels_hight, self.square_size)
        if self.configuration['has_junior'] and not(self.configuration['has_junior_hight_connection']):
            self.shool_jun = ShoolJunior(self.levels_num, self.levels_hight, self.square_size)
        self.meet_zone = MeetSquare(1, 0.001, self.square_size)
        print(recktangles_to_place)
        coords = place_rectangles(current_zone.coords, recktangles_to_place)
        coords = align_rectangles(coords)

        if self.configuration['has_junior'] and not (self.configuration['has_junior_hight_connection']):
            self.shool_main.build(coords[2], self.configuration)
            self.shool_jun.build(coords[1])
            self.meet_zone.build(coords[0])
            self.objects.extend(self.shool_main.objects)
            self.objects.extend(self.meet_zone.objects)
            self.objects.extend(self.shool_jun.objects)
        else:
            self.shool_main.build(coords[1], self.configuration)
            self.meet_zone.build(coords[0])

            self.objects.extend(self.shool_main.objects)
            self.objects.extend(self.meet_zone.objects)

        ...
    def build_sport_zone(self):
        # 1 - 100 метров
        current_zone = None
        for zone in self.zone_list:
            if zone.name == 'sport_zone':
                current_zone = zone
                break
        if current_zone == None:
            return

        sport_race_size = (1, 0.2)
        football_field_size = (1, 0.5)
        volleyball_court_size = (0.2, 0.1)
        basketball_court_size = (0.3, 0.2)

        recktangles_to_place = [sport_race_size, football_field_size]

        self.sport_race = SportRace(1, 0.02, self.square_size)
        self.football_field = FootBallField(1, 0.1, self.square_size)
        if self.configuration['has_volleyball_court']:
            self.volleyball_court = VolleyballCourt(1, 0.1, self.square_size)
            recktangles_to_place.append(volleyball_court_size)
        if self.configuration['has_basketball_court']:
            self.basketball_court = BasketballCourt(1, 0.1, self.square_size)
            recktangles_to_place.append(basketball_court_size)




        coords = place_rectangles(current_zone.coords, recktangles_to_place)


        coords = align_rectangles(coords)
        # coords[2:3] = align_rectangles(coords[2:3])

        self.sport_race.build(coords[0])
        self.football_field.build(coords[1])

        self.objects.extend(self.sport_race.objects)
        self.objects.extend(self.football_field.objects)

        coords[2:] = align_rectangles(coords[2:])
        if self.configuration['has_volleyball_court']:
            self.volleyball_court.build(coords[2])
            self.objects.extend(self.volleyball_court.objects)
        if self.configuration['has_basketball_court']:
            if len(recktangles_to_place) == 3:
                self.basketball_court.build(coords[2])
            else:
                self.basketball_court.build(coords[3])
            self.objects.extend(self.basketball_court.objects)

        ...
    def build_trash_zone(self):
        ...
    def build_meet_zone(self):
        ...

    def build_zone(self):
        for zone in self.zone_list:
            zone.buld_model()
            self.objects.append(zone.object)
    def devide_territory(self, zone_number = 2):

        # print(triangles)

        # target_count = 3
        if self.configuration['has_relax_zone']:
            zone_number +=1
        if len(self.ground_polygon)%2 == 1:
            self.ground_polygon = multiply_polygon_vertices(self.ground_polygon, 2)
        if len(self.ground_polygon) < zone_number *3:
            self.ground_polygon = multiply_polygon_vertices(self.ground_polygon, zone_number)


        triangles = triangulate_polygon(self.ground_polygon)

        # mesh_count = 9999
        # while mesh_count > target_count:
        zone_coords_list = kmeans_clustering(triangles, zone_number)
        print('len(zone_list)', len(zone_coords_list))
        self.zone_list = []
        for zone_coords in zone_coords_list:
            self.zone_list.append(Zone(zone_coords))

        self.zone_list.sort(key = lambda zone: zone.area_size, reverse=True)
        self.zone_list[0].name = 'main_zone'
        self.zone_list[0].color = self.zone_color_dict[self.zone_list[0].name]
        self.zone_list[1].name = 'sport_zone'
        self.zone_list[1].color = self.zone_color_dict[self.zone_list[1].name]
        # self.zone_list[2].name = 'meet_zone'
        # self.zone_list[2].color = self.zone_color_dict[self.zone_list[2].name]

        if len(self.zone_list)>2:
            self.zone_list[2].name = 'relax_zone'
            self.zone_list[2].color = self.zone_color_dict[self.zone_list[2].name]

        if len(self.zone_list) > 3:

            for zone in self.zone_list[3:]:
                zone.name = 'ground_zone'
                zone.color = self.zone_color_dict[zone.name]




        ...