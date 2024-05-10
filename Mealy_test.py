import unittest
from Mealy import MealyFSM


class TestMealyFSM(unittest.TestCase):
    def test_execution(self) -> None:
        fsm = MealyFSM(initial_state="S0")
        fsm.add_node("S0", {1: "S1", 0: "S0"}, {1: "Output_A", 0: "Output_B"})
        fsm.add_node("S1", {1: "S1", 0: "S0"}, {1: "Output_C", 0: "Output_D"})

        input_sequence = [(0, None), (2, 1), (4, 0), (7, 1), (9, 0)]
        expected_state_sequence = [
            (0, "S0"),
            (2, "S1"),
            (4, "S0"),
            (7, "S1"),
            (9, "S0"),
        ]
        expected_output_sequence = [
            (2, "Output_A"),
            (4, "Output_D"),
            (7, "Output_A"),
            (9, "Output_D"),
        ]

        fsm.execute(input_sequence)

        self.assertEqual(fsm.state_seq, expected_state_sequence)
        self.assertEqual(fsm.output_seq, expected_output_sequence)


if __name__ == "__main__":
    unittest.main()
