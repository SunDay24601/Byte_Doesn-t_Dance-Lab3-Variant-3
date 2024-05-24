# Byte Doesn't Dance - lab 3 - variant 3

## Introduction

- Lab 3 involves designing and implementing a Mealy Finite State Machine (FSM)
  and a testing framework for it. The Mealy FSM interprets a specific model of
  computation using nodes and transition rules defined in an input language.
  The project aims to execute and trace computational processes, validate
  input data, and visualize models using GraphViz DOT.

## Features

- Define Mealy finite state machines using an embedded domain-specific language.
- Execute defined state machines with input sequences.
- Visualize state machines as GraphViz DOT graphs.
- Handle runtime errors and negative timestamps appropriately.

## Project Structure

- `Mealy.py` -- Implementation of the Mealy Finite State Machine and nodes.
- `Mealy_test.py` -- Unit and property-based tests for the Mealy Finite State Machine.

## Contribution

- **Hu Jinghao** (1206041060@qq.com) - All work

- **Meng Chenxu** (3183093110@qq.com) - All work

## Changelog

- **23.05.2024** - Visualize model.

- **20.05.2024** - Check code style.

- **18.05.2024** - Mealy_test.py.

- **16.05.2024** - Mealy.py.

## Design Notes

- The MealyFSM class maintains the current state of the machine, executes
  transition rules based on input sequences, and generates visual
  representations of the state machine.

- The Node class represents individual states and manages transition rules
  and output mappings. Input sequences are processed, and outputs are
  generated according to the rules defined in the state machine.
