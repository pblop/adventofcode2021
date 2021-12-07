#!/usr/bin/env bash

echo "Part 1:"
cc part1.c -o part1 && (cat input.txt | ./part1)

echo "Part 2:"
cc part2.c -o part2 && (cat input.txt | ./part2)
