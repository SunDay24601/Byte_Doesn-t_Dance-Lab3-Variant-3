from typing import Dict, Any, List, Optional, Tuple


class Node:
    def __init__(
        self,
        name: str,
        transition_rules: Dict[int, str],
        output_mapping: Dict[int, str],
    ) -> None:
        self.name: str = name
        self.transition_rules: Dict[int, str] = transition_rules
        self.output_mapping: Dict[int, str] = output_mapping

    def activate(self, input_value: int) -> Tuple[str, Optional[str]]:
        if input_value in self.transition_rules:
            next_state = self.transition_rules[input_value]
            output = self.output_mapping.get(input_value)
            return next_state, output
        else:
            return self.name, None


class MealyFSM:
    def __init__(self, initial_state: str) -> None:
        self.current_state: str = initial_state
        self.nodes: Dict[str, Node] = {}
        self.state_seq: List[str] = []
        self.output_seq: List[Any] = []

    def add_node(
        self,
        node_name: str,
        transition_rules: Dict[int, str],
        output_mapping: Dict[int, str],
    ) -> None:
        node: Node = Node(node_name, transition_rules, output_mapping)
        self.nodes[node_name] = node

    def execute(self, input_seq: List[int]) -> None:
        for input_value in input_seq:
            node: Node = self.nodes[self.current_state]
            next_state, output = node.activate(input_value)
            self.state_seq.append(self.current_state)
            if output is not None:
                self.output_seq.append(output)
            self.current_state = next_state
        self.state_seq.append(self.current_state)
