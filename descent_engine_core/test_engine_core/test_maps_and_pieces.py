from unittest import TestCase
from descent_engine_core.map.map_core import MapPiece, Mapp
import json
import os


class MapsTestCase(TestCase):
    def setUp(self) -> None:
        self.big_map = Mapp()
        self.big_map.map_matrix[0][1] = "Z"
        self.small_map = Mapp()
        self.small_map.map_matrix = [["S" for _ in range(10)] for _ in range(10)]

    test_map_piece = MapPiece(
        [
            ["S", "S", "S", "S", "S", "S", "S"],
            ["S", "S", "B", "F", "F", "B", "S"],
            ["S", "B", "B", "W", "W", "F", "B"],
            ["F", "F", "W", "W", "W", "F", "B"],
            ["F", "F", "W", "W", "W", "F", "B"],
            ["S", "B", "F", "F", "F", "F", "B"],
            ["S", "B", "B", "B", "B", "B", "B"],
        ]
    )

    def test_piece_rotates(self):

        rotated_test_piece = MapPiece(
            [
                ["S", "S", "F", "F", "S", "S", "S"],
                ["B", "B", "F", "F", "B", "S", "S"],
                ["B", "F", "W", "W", "B", "B", "S"],
                ["B", "F", "W", "W", "W", "F", "S"],
                ["B", "F", "W", "W", "W", "F", "S"],
                ["B", "F", "F", "F", "F", "B", "S"],
                ["B", "B", "B", "B", "B", "S", "S"],
            ]
        )
        self.test_map_piece.rotate()
        self.assertEqual(self.test_map_piece.map_piece, rotated_test_piece.map_piece)

    def test_piece_rotates_twice(self):

        twice_rotated_piece = MapPiece(
            [
                ["S", "S", "B", "B", "B", "B", "B"],
                ["S", "B", "F", "F", "F", "F", "B"],
                ["S", "F", "W", "W", "W", "F", "B"],
                ["S", "F", "W", "W", "W", "F", "B"],
                ["S", "B", "B", "W", "W", "F", "B"],
                ["S", "S", "B", "F", "F", "B", "B"],
                ["S", "S", "S", "F", "F", "S", "S"],
            ]
        )

        self.test_map_piece.rotate(2)

        self.assertEqual(self.test_map_piece.map_piece, twice_rotated_piece.map_piece)

    def test_add_map_piece_to_map(self):
        small_map = [
            ["B", "B", "B", "B", "B", "B", "S", "S", "S", "S"],
            ["B", "F", "F", "F", "F", "B", "S", "S", "S", "S"],
            ["S", "F", "F", "F", "F", "B", "S", "S", "S", "S"],
            ["S", "F", "F", "F", "F", "B", "S", "S", "S", "S"],
            ["B", "F", "F", "F", "F", "B", "S", "S", "S", "S"],
            ["b", "B", "S", "S", "B", "B", "S", "S", "S", "S"],
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
        ]
        self.small_map.add_map_piece_to_map(
            [
                ["B", "B", "B", "B", "B", "B"],
                ["B", "F", "F", "F", "F", "B"],
                ["S", "F", "F", "F", "F", "B"],
                ["S", "F", "F", "F", "F", "B"],
                ["B", "F", "F", "F", "F", "B"],
                ["b", "B", "S", "S", "B", "B"],
            ],
            0,
            0,
        )

        self.assertEqual(self.small_map.map_matrix, small_map)

    def test_map_export(self):
        self.big_map.export_map("test_map.json")
        new_map = json.load(open("test_map.json"))

        self.assertEqual(self.big_map.map_matrix[0][1], new_map[0][1])
        os.remove("test_map.json")

    def test_map_import(self):
        small_map_piece = self.big_map.map_matrix[0][1]
        json_dump = json.dumps(self.big_map.map_matrix)

        with open("second_test_map.json", "w") as file:
            file.write(json_dump)
            file.close()

        self.assertEqual(self.big_map.map_matrix[0][1], small_map_piece)
        os.remove("second_test_map.json")
