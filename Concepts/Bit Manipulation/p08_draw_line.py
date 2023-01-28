"""
Draw line:

A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in 
one byte. The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows).
They height of the screen, of course, can be derived from the lenght of the array and the width.
Implement a function that draws a horizontal line from (x1, y) to (x2, y)

The method signature shoudl look something like:
drawLine(byte[] screen, int width, int x1, int x2, int y)
"""

def draw_line(screen: bytearray, width: int, x1: int, x2: int, y: int) -> bytearray:
    # Figure out if the first byte of the range needs to be partially filled or not
    start_offset =  x1 % 8
    first_full_byte = x1 // 8
    # x1 % 8 is never 0 unless x1 == 0
    if start_offset != 0:
        first_full_byte += 1

    # Figure out if the last byte of the range needs to be partially filled or not
    end_offset = x2 % 8
    last_full_byte = x2 // 8
    # if x2 is 7 then x2 mod 8 is 7 and means the last byte is full
    if end_offset != 7:
        last_full_byte -= 1

    # Set full bytes
    for full_byte in range(first_full_byte, last_full_byte + 1):
        screen[(width // 8) * y + full_byte] = 0xFF

    # Masks for start and end of line
    start_mask = 0xFF >> start_offset
    # unsigned complement to avoid negative numbers on mask
    end_mask = (0xFF >> (end_offset + 1)) ^ 0xFF

    ## if start and end on same byte
    start_byte = (x1 // 8)
    end_byte = (x2 // 8)

    if start_byte == end_byte:
        mask = start_mask & end_mask
        screen[(width // 8) * y + start_byte] |= mask
    else:
        if start_offset != 0:
            byte_number = (width // 8) * y + start_byte
            screen[byte_number] |= start_mask
        if end_offset != 7:
            byte_number = (width // 8) * y + end_byte
            screen[byte_number] |= end_mask
    return screen


def test():
    test_cases = [
        ([bytearray(2), 16, 0, 15, 0], bytearray([0b11111111, 0b11111111])),
        ([bytearray(1), 8 , 1, 5, 0], bytearray([0b01111100])),
        ([bytearray(1), 8 , 3, 7, 0], bytearray([0b00011111])),
        ([bytearray(3), 8, 1, 5, 1], bytearray([0b00000000, 0b01111100, 0b000000000])),
        ([bytearray(3), 24, 6, 17, 0], bytearray([0b00000011, 0b11111111, 0b11000000]))
    ]

    for test in test_cases:
        args = test[0]
        expected = test[1]
        result = draw_line(*args)
        assert expected == result

test()
