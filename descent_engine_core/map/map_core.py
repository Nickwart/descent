import json


class Mapp:
    map_matrix = [["S" for _ in range(100)] for _ in range(100)]

    def add_map_piece_to_map(self, map_piece_template, coord_y, coord_x, rotate=0):
        new_map_piece = MapPiece(map_piece_template)
        new_map_piece.rotate(rotate)
        for i in range(len(map_piece_template)):
            for j in range(len(map_piece_template[0])):
                self.map_matrix[coord_y + i][coord_x + j] = new_map_piece.map_piece[i][j]

    def import_map(self, filename):
        new_map = json.load(open(filename))

        self.map_matrix = new_map

    def export_map(self, filename):

        full_map = self.map_matrix
        json_dump = json.dumps(full_map)

        with open(filename, "w") as file:
            file.write(json_dump)
            file.close()


class MapPiece:
    def __init__(self, map_piece):
        self.map_piece = map_piece

    def rotate(self, count_of_rotates=1):
        for i in range(count_of_rotates):
            new_list = []
            for j in range(len(self.map_piece[0])):
                new_list.append([])

            for one_list in self.map_piece:
                counter = 0
                for element in one_list:
                    new_list[counter].append(element)
                    counter += 1

            for lists in new_list:
                lists.reverse()
            self.map_piece = new_list

    def print_map_piece(self):
        for row in self.map_piece:
            print(row)
