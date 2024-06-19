# номер посылки: 115378127
def decode_string(encoded_string: str) -> str:
    stack: list[tuple[list[str], int]] = []
    current_number: int = 0
    current_segment: list[str] = []

    for character in encoded_string:
        if '0' <= character <= '9':
            current_number = current_number * 10 + int(character)
        elif character == '[':
            stack.append((current_segment, current_number))
            current_segment = []
            current_number = 0
        elif character == ']':
            previous_segment, repeat_count = stack.pop()
            current_segment = previous_segment + current_segment * repeat_count
        else:
            current_segment.append(character)

    return ''.join(current_segment)


if __name__ == '__main__':
    compressed_instructions: str = input().strip()  # Ввод сокращенной формы команды
    print(decode_string(compressed_instructions))
