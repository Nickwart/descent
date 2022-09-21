from descent_engine_core.actions.actions_core import Action
from descent_engine_core.exeptions.exeption import NotEnoughMovePointsException
from descent_engine_core.items import random_treasure
from descent_engine_core.statuses import FALLEN, STUNNED


class MoveUnit(Action):

    name = 'move_unit'

    def activate(self, game_instance, unit, coords):
        if self.can_be_activated(game_instance, unit, coords):
            coords = tuple(coords)
            unit_speed = unit.current_speed
            move_way, move_list = self.get_move_list(unit, unit_speed, game_instance)
            if coords in move_list.keys():

                list_of_steps = []

                while coords != [unit.y_coord, unit.x_coord]:
                    list_of_steps.append(list(coords))
                    cell_info = move_way.get(tuple(coords))
                    coords = cell_info["previous_cell"]

                list_of_steps.reverse()

                for step in list_of_steps:
                    cell_info = move_way.get(tuple(step))
                    unit.y_coord = step[0]
                    unit.x_coord = step[1]
                    unit.current_speed -= cell_info["cost_of_move"]
                    print(unit.current_speed)

                    if len(game_instance.game_map.map_matrix[unit.y_coord][unit.x_coord]) < 2:
                        game_instance.pause_game_for_overlord()

            else:
                raise NotEnoughMovePointsException

    def can_be_activated(self, game_instance, unit, coords):
        if unit.moves > 1 and unit.name == 'Zombie':
            pass
        else:
            move_list, move_points = self.get_move_list(unit, unit.current_speed, game_instance)
            if unit.moves > 0 and tuple(coords) in move_points and [STUNNED, FALLEN] not in unit.statuses:
                return True
            else:
                return False

    def get_move_list(self, unit, move_points, game_instance):

        step_cost_massif = [[99 for _ in range(100)] for _ in range(100)]
        way_pointer_massif = [[[0, 0] for _ in range(100)] for _ in range(100)]
        true_false_massif = [[True for _ in range(100)] for _ in range(100)]

        step_cost_massif[unit.y_coord][unit.x_coord] = 0
        start_coords = [unit.y_coord, unit.x_coord]
        cost_of_move = self._get_step_cost(unit)

        points_of_way = {}
        min_move_point = 1
        while round(min_move_point) <= move_points:
            closest_to_min = 99
            closest_to_min_coords = [0, 0]

            points_of_way = self._get_point_to_move(
                start_coords,
                move_points,
                cost_of_move,
                true_false_massif,
                step_cost_massif,
                way_pointer_massif,
                points_of_way,
                game_instance
            )

            true_false_massif[start_coords[0]][start_coords[1]] = False

            closest_to_min, closest_to_min_coords = self._find_smallest_digit(
                closest_to_min,
                min_move_point,
                closest_to_min_coords,
                step_cost_massif,
                true_false_massif,
            )

            start_coords = closest_to_min_coords

            if closest_to_min > min_move_point:
                min_move_point = closest_to_min

        points_to_move_on = self._del_redundant_cells(points_of_way, game_instance)

        return points_of_way, points_to_move_on

    def _find_smallest_digit(
            self,
            closest_to_min,
            min_move_point,
            closest_to_min_coords,
            step_cost_massif,
            true_false_massif,
    ):
        row_counter = 0
        for row in step_cost_massif:

            cell_counter = 0
            for cell in row:
                if (
                        true_false_massif[row_counter][cell_counter]
                        and cell == min_move_point
                ):
                    closest_to_min = cell
                    closest_to_min_coords[0] = row_counter
                    closest_to_min_coords[1] = cell_counter
                    break

                elif (
                        true_false_massif[row_counter][cell_counter]
                        and cell <= closest_to_min
                ):

                    closest_to_min = cell
                    closest_to_min_coords[0] = row_counter
                    closest_to_min_coords[1] = cell_counter

                cell_counter += 1

            row_counter += 1

        return closest_to_min, closest_to_min_coords

    def _get_point_to_move(
            self,
            start,
            move_points,
            move_cost,
            true_false,
            cost_massif,
            pointer_massif,
            points_of_way,
            game_instance,
    ):
        for i in range(-1, 2):
            for j in range(-1, 2):
                current_coords = [start[0] + i, start[1] + j]
                cost_point = cost_massif[start[0] + i][start[1] + j]
                if true_false[current_coords[0]][current_coords[1]]:
                    map_point = game_instance.game_map.map_matrix[current_coords[0]][
                        current_coords[1]
                    ]
                    cost_of_step = (
                            move_cost[map_point] + cost_massif[start[0]][start[1]]
                    )

                    if (
                            round(cost_of_step) <= cost_point
                            and cost_of_step <= move_points
                    ):
                        cost_massif[current_coords[0]][current_coords[1]] = cost_of_step
                        pointer_massif[current_coords[0]][current_coords[1]] = start

                        if (
                                tuple([start[0] + i, start[1] + j])
                                not in points_of_way.keys()
                        ):
                            cell_items = {
                                "coords": [start[0] + i, start[1] + j],
                                "cost_of_step": cost_of_step,
                                "previous_cell": start,
                                "cost_of_move": move_cost[map_point],
                            }
                            points_of_way.update(
                                {tuple([start[0] + i, start[1] + j]): cell_items}
                            )

        return points_of_way

    def _get_step_cost(self, unit):

        cost_of_move = {
            "FT": 90,
            "FH": 90,
            "WH": 90,
            "LH": 90,
            "FB": 90,
            "WB": 90,
            "LB": 90,
            "B": 90,
            "S": 90,
            "F": 1,
            "W": 2,
            "L": 1.0001,
        }

        if unit.side == "Hero":
            cost_of_move["FH"] = 1
            cost_of_move["WH"] = 2
            cost_of_move["LH"] = 1.0001

        elif unit.side == "Bubuka":
            cost_of_move["FB"] = 1
            cost_of_move["WB"] = 2
            cost_of_move["LB"] = 1.0001

        return cost_of_move

    def _del_redundant_cells(self, points_list, game_instance):
        points_to_move_on = points_list.copy()
        cells_to_delete = []
        for cell_name in points_to_move_on.keys():
            if len(game_instance.game_map.map_matrix[cell_name[0]][cell_name[1]]) != 1:
                cells_to_delete.append(cell_name)

        for item in cells_to_delete:
            del points_to_move_on[item]

        return points_to_move_on


class PickUpTreasure(Action):

    name = 'pick_up_treasure'

    def activate(self, game_instance, unit, coords):
        if self.can_be_activated(game_instance, unit, coords):
            game_instance.game_map.map_matrix[coords[0]][coords[1]] = 'F'
            unit.items += [random_treasure]
            unit.moves -= 1

    def can_be_activated(self, game_instance, unit, coords):
        if unit.side == 'Hero' and game_instance.game_map.map_matrix[coords[0]][coords[1]] == 'FT':
            if [STUNNED, FALLEN] not in unit.statuses and unit.moves > 0:
                y_coord_diff = abs(unit.y_coord - coords[0])
                x_coord_diff = abs(unit.x_coord - coords[1])
                if y_coord_diff <= unit.search_range and x_coord_diff <= unit.search_range:
                    return True
        else:
            return False


class AddSpeedForStamina(Action):

    name = 'add_speed_for_stamina'

    def activate(self, game_instance, unit, coords):
        if self.can_be_activated(game_instance, unit, coords):
            if unit.current_durability == 0:
                unit.current_health -= 1
                unit.current_speed += 1

            else:
                unit.current_durability -= 1
                unit.current_speed += 1

    def can_be_activated(self, game_instance, unit, coords):
        return (
            unit.current_health > 1
            and unit.current_durability == 0
            and [STUNNED, FALLEN] not in unit.statuses
            and unit.side == "Hero"
        )
