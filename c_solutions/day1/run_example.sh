#!/usr/bin/env bash

echo "Part 1:"
cc part1.c -o part1 && (cat example_input.txt | ./part1)

echo "Part 2:"
cc part2.c -o part2 && (cat example_input.txt | ./part2)
