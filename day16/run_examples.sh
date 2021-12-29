#!/usr/bin/env bash

function teststring () {
  echo "  Input: $1"
  echo "$1" | python3 "$2"
  # echo "$1" | python3 $3
  read
}

echo "Part 1:"
teststring "D2FE28" part1.py
teststring "38006F45291200" part1.py
teststring "EE00D40C823060" part1.py
teststring "8A004A801A8002F478" part1.py
teststring "620080001611562C8802118E34" part1.py
teststring "C0015000016115A2E0802F182340" part1.py
teststring "A0016C880162017C3686B18A3D4780" part1.py

echo "Part 2:"
teststring "C200B40A82" part2.py
teststring "04005AC33890" part2.py
teststring "880086C3E88112" part2.py
teststring "CE00C43D881120" part2.py
teststring "D8005AC2A8F0" part2.py
teststring "F600BC2D8F" part2.py
teststring "9C005AC2F8F0" part2.py
teststring "9C0141080250320F1802104A08" part2.py
