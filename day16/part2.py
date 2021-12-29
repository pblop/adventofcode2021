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

# Function that multiplies together its input
def mul(iterable):
  res = 1
  for n in iterable:
    res *= n
  return res


# Decodes a packet and returns the unread bits
# Returns:
#  - If the packet is a literal:
#       ("literal", literal, last_read_bit_pos)
#    where 'literal' is the integer value of the literal
#      and 'last_read_bit_pos' is the position of the last read bit 
#          in the binary string given as input
#  - If the packet is an operator:
#       ("operator", result, last_read_bit_pos)
#    where 'result' is the integer value of the operation result
#      and 'last_read_bit_pos' is the position of the last read bit 
#          in the binary string given as input
def decode_packet(binstr):
  # Packet header
  # Version: 0, len 3
  # Type id: 3, len 3
  version = int(binstr[:3], 2)
  typeid = int(binstr[3:6], 2)

  if typeid == 4:
    # This is a literal packet

    binary_literal, unread_bits_pos = decode_literal(binstr[6:])
    literal = int(binary_literal, 2)

    return ("literal", literal, 6 + unread_bits_pos)
  else:
    # This is an operator packet
    literal_list = []

    # Length type ID: 6, len 1
    lentypeid = int(binstr[6], 2)

    # We're now going to parse the subpackets that this packet contains,
    # based on the type of length we've been given.
    if lentypeid == 0:
      # Subpackets length: 7, len 15
      subpacketslen = int(binstr[7:7+15], 2)

      decoding_position = 7+15
      while isvalid(binstr[decoding_position:]) and decoding_position < 7+15+subpacketslen:
        # Decoded packet will always be a literal, so we don't care
        # about the packet type (first elem in return tuple).
        _, literal, unread_bit_pos = decode_packet(binstr[decoding_position:])
        
        literal_list.append(literal)
        decoding_position += unread_bit_pos
    else:
      # Subpackets number (amount of subpackets): 7, len 11
      subpacketsnum = int(binstr[7:7+11], 2)

      decoding_position = 7+11
      for _ in range(subpacketsnum):
        _, literal, unread_bit_pos = decode_packet(binstr[decoding_position:])
        
        literal_list.append(literal)
        decoding_position += unread_bit_pos
    
    result = None
    match typeid:
      case 0:
        # sum operator
        result = sum(literal_list)
      case 1:
        # product operator
        result = mul(literal_list)
      case 2:
        # minimum operator
        result = min(literal_list)
      case 3:
        # maximum operator
        result = max(literal_list)
      case 5:
        # greater than (>) operator
        result = int(literal_list[0] > literal_list[1])
      case 6:
        # less than (<) operator
        result = int(literal_list[0] < literal_list[1])
      case 7:
        # equal to (==) operator
        result = int(literal_list[0] == literal_list[1])
    
    return ("operator", result, decoding_position)

def main():
  hexstr = input()
  print(f"Hex in: {hexstr}")
  binstr = nbin(hexstr)
  print(f"Input: {binstr}")

  packet_type, result, last_read_bit = decode_packet(binstr)

  print(f"Result: {result}")
  

if __name__ == "__main__":
  main()