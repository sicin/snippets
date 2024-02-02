from typing import Any, Literal


numbers_dict: dict[str, int] = {
    "十": 10,
    "拾": 10,
    "百": 100,
    "佰": 100,
    "千": 1000,
    "仟": 1000,
    "万": 10000,
    "萬": 10000,
    "亿": 100000000,
    "億": 100000000,
    "一": 1,
    "壹": 1,
    "二": 2,
    "两": 2,
    "兩": 2,
    "贰": 2,
    "貳": 2,
    "三": 3,
    "叁": 3,
    "參": 3,
    "四": 4,
    "肆": 4,
    "五": 5,
    "伍": 5,
    "六": 6,
    "陆": 6,
    "陸": 6,
    "七": 7,
    "柒": 7,
    "八": 8,
    "捌": 8,
    "九": 9,
    "玖": 9,
    "零": 0,
    "〇": 0,
}


def multiply_value(pre_value: int, value: int) -> int:
    multiplier: int = pre_value if 0 < pre_value < value else 1
    return value * multiplier


def process_num_list_value(value: int, value_pos: int, list_of_numbers: list[int]) -> int:
    if value_pos == 0:
        return value
    else:
        pre_value: int = list_of_numbers[value_pos - 1]
    return multiply_value(pre_value, value)


def converter_main(user_input: str) -> str:
    wan_counter = 0
    final_append = 0
    qian_pre_wan = 0
    bai_pre_wan = 0
    shi_pre_wan = 0
    add_wan = 0
    add_digit = 0
    add_digit_higher = 0
    process_mapping: dict[int, list[int]] = {10: [0, 0, 0, 0],
                                             100: [0, 0, 0, 0],
                                             1000: [0, 0, 0, 0]}
    unverified_num_list: list[Any] = [
        numbers_dict.get(l, l) for l in user_input]

    if not unverified_num_list:
        return "Your input is empty!"

    if all(isinstance(x, int) for x in unverified_num_list):
        num_list: list[int] = unverified_num_list
        reversed_num_list: list[int] = num_list[::-1]
    else:
        return f"You need to input Chinese numerals, {user_input} is not a proper Chinese number!\nThe characters are not all numbers."

    if any(x == y for x, y in zip(num_list, num_list[1:])):
        return f"You need to input Chinese numerals, {user_input} is not a proper Chinese number!\nSame characters cannot be next to each other."

    def handle_number_higher(value: int) -> None:
        process_mapping[value][3] = process_num_list_value(
            value, num_list_higher.index(value), num_list_higher)

    def higher_numbers(list_of_numbers: list[int]) -> int | Literal[False]:
        for e in list_of_numbers:
            if e in [1000, 100, 10]:
                handle_number_higher(e)
            if e > 1000:
                return False
        return list_of_numbers[-1] if 0 < list_of_numbers[-1] < 10 else 0

    def process_one_counter(value: int, value_pos_plus_one: int) -> int:
        if value_pos_plus_one >= len(reversed_num_list) - 1:
            return value
        pre_value: int = reversed_num_list[value_pos_plus_one]
        return multiply_value(pre_value, value)

    def handle_number(value: int) -> None:
        if process_mapping[value][1] == 0:
            process_mapping[value][0] = process_num_list_value(
                value, num_list.index(value), num_list)
        else:
            process_mapping[value][2] = process_one_counter(
                value, reversed_num_list.index(value) + 1)
        process_mapping[value][1] += 1

    def process_sum(process_position: int) -> int:
        return sum(value[process_position] for _, value in process_mapping.items())

    if num_list[0] > 10:
        num_list.insert(0, 1)

    if len(num_list) >= 3 and num_list[-1] < 10 and num_list[-2] >= 100:
        final_append: int = num_list[-1]
        num_list.pop(-1)

    if num_list[-1] < 10:
        add_digit: int = num_list[-1]

    if 100000000 in num_list:
        num_list_higher: list[int] = num_list[:num_list.index(100000000)]
        num_list = num_list[num_list.index(100000000) + 1:]
        add_digit_higher: int | Literal[False] = higher_numbers(
            num_list_higher)
        if add_digit_higher is False:
            return f"{user_input} is too high, only numbers lower than 10^12 are allowed."

    for s in num_list:
        if s == 10000:
            wan_pos: int = num_list.index(s)
            wan_counter += 1
            pre_wan_value: int = num_list[wan_pos - 1]
            qian_pre_wan: int = process_mapping[1000][1]
            bai_pre_wan: int = process_mapping[100][1]
            shi_pre_wan: int = process_mapping[10][1]
            if wan_pos == 0 or not 0 < pre_wan_value < 10:
                wan_multiplier = 0
            else:
                wan_multiplier: int = pre_wan_value
            add_wan: int = s * wan_multiplier
        elif s in [1000, 100, 10]:
            handle_number(s)

    counters: int = process_sum(1)

    if wan_counter == 1 and counters != 0:
        if qian_pre_wan != 0:
            process_mapping[1000][0] *= 10000
        if bai_pre_wan != 0:
            process_mapping[100][0] *= 10000
        if shi_pre_wan != 0:
            process_mapping[10][0] *= 10000

    add_higher: int = (process_sum(3) + add_digit_higher) * 100000000

    added_up: int = add_higher + \
        process_sum(0) + add_wan + process_sum(2) + add_digit

    if final_append == 0:
        return str(added_up)
    append_list = list(map(int, str(added_up)))
    non_zero_pos = 0
    for z in reversed(append_list):
        non_zero_pos -= 1
        if z != 0:
            append_list[non_zero_pos + 1] = final_append
            return "".join(str(e) for e in append_list)
    return "Unknown error"


if __name__ == "__main__":
    print(converter_main(input("Enter Chinese numeral:")))
