from typing import Dict, Any, List, Optional, Tuple


class Node:
    def __init__(
        self,
        name: str,
        transition_rules: Dict[int, str],
        output_mapping: Dict[int, Optional[str]],
    ) -> None:
        self.name: str = name
        self.transition_rules: Dict[int, str] = transition_rules
        self.output_mapping: Dict[int, Optional[str]] = output_mapping

    def activate(self, input_tuple: Tuple[int, Any]) -> Tuple[str, Optional[str]]:
        time, input_value = input_tuple
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
        self.state_seq: List[Tuple[int, str]] = []
        self.output_seq: List[Tuple[int, str]] = []

    def add_node(
        self,
        node_name: str,
        transition_rules: Dict[int, str],
        output_mapping: Dict[int, Optional[str]],
    ) -> None:
        node: Node = Node(node_name, transition_rules, output_mapping)
        self.nodes[node_name] = node

    def execute(self, input_seq: List[Tuple[int, Any]]) -> None:
        for input_tuple in input_seq:
            node: Node = self.nodes[self.current_state]
            next_state, output = node.activate(input_tuple)
            self.state_seq.append((input_tuple[0], next_state))
            if output is not None:
                self.output_seq.append((input_tuple[0], output))
            self.current_state = next_state

    def generate_dot_graph(self) -> str:
        dot_graph = "digraph MealyFSM {\n"
        dot_graph += "    rankdir=LR;\n"
        for node_name, node in self.nodes.items():
            for input_value, next_state in node.transition_rules.items():
                output = node.output_mapping.get(input_value)
                dot_graph += f'    {node_name} -> {next_state} [label="{input_value} / {output}"];\n'
        dot_graph += "}"
        return dot_graph

    def generate_state_table(self) -> str:
        table = "| Current State | Input | Next State | Output |\n"
        table += "|---------------|-------|------------|--------|\n"
        for node_name, node in self.nodes.items():
            for input_value, next_state in node.transition_rules.items():
                output = node.output_mapping.get(input_value)
                table += f"| {node_name} | {input_value} | {next_state} | {output} |\n"
        return table
