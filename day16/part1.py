import sys

# Method that does the same as bin(int(hexstr, 16))
# but keeps the correspondence of 1 hex digit -> 4 bin digits
def nbin(hexstr):
  return ''.join(["{0:{fill}4b}".format(int(digit, 16), fill='0') for digit in hexstr])

# Decodes a literal and returns the decoded literal, as well as the last read bit position.
def decode_literal(binary):
  decoded = ""
  for i in range(0, len(binary) - len(binary)//5, 5):
    decoded += binary[i+1: i+5]
    if binary[i] == "0":
      return decoded, i+5

# Quick function for seeing if a binary string is (probably) a valid packet.
def isvalid(binary):
  return int(binary, 2) != 0

added_up_versions = 0
# Decodes a packet and returns the unread bits
def decode_packet(binstr):
  global added_up_versions
  # Packet header
  # Version: 0, len 3
  # Type id: 3, len 3
  version = int(binstr[:3], 2)
  added_up_versions += version
  typeid = int(binstr[3:6], 2)
  print(f"Version: {version}, type id: {typeid}")

  match typeid:
    case 4:
      # literal
      print("Type: literal.")

      binary_literal, unread_bits_pos = decode_literal(binstr[6:])
      literal = int(binary_literal, 2)
      print(f"Encoded literal: {binstr[6:]}")
      print(f"Decoded literal: {literal}")
      return 6 + unread_bits_pos
    case _:
      # operator
      print("Type: operator")

      # Length type ID: 6, len 1
      lentypeid = int(binstr[6], 2)
      print(f"Length type ID: {lentypeid}")
      if lentypeid == 0:
        # Subpackets length: 7, len 15
        subpacketslen = int(binstr[7:7+15], 2)
        print(f"Subpackets length: {subpacketslen}")

        decoding_position = 7+15
        while isvalid(binstr[decoding_position:]) and decoding_position < 7+15+subpacketslen:
          print("Decoding subpacket...")
          unread_bits = decode_packet(binstr[decoding_position:])
          decoding_position += unread_bits
      else:
        # Subpackets number (amount of subpackets): 7, len 11
        subpacketsnum = int(binstr[7:7+11], 2)
        print(f"Subpackets number: {subpacketsnum}")

        decoding_position = 7+11
        for _ in range(subpacketsnum):
          print("Decoding subpacket...")
          unread_bits = decode_packet(binstr[decoding_position:])
          decoding_position += unread_bits

      return decoding_position

def main():
  hexstr = input()
  print(f"Hex in: {hexstr}")
  binstr = nbin(hexstr)
  print(f"Input: {binstr}")

  decode_packet(binstr)

  print(f"Versions: {added_up_versions}")
  
  
  # print(binstr)
  # print(f"{version}{typeid}")

if __name__ == "__main__":
  main()