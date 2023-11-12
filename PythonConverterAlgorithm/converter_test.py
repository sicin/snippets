from typing import Literal
from converter_trillion import converter_main

progress: str = ""


def x_test_conversion(input_value: str, expected_result: str) -> Literal['success', 'failure']:
    try:
        converter_main(input_value)
    except Exception as error:
        print(
            f"\nFAILURE!\nInput= {input_value}\nExpected result= {expected_result}\nReturned result= {error}")
        return "failure"
    else:
        if converter_main(input_value) == expected_result:
            return "success"
        print(
            f"\nFAILURE!\nInput= {input_value}\nExpected result= {expected_result}\nReturned result= {converter_main(input_value)}")
        return "failure"


# Conversion
progress += x_test_conversion("一亿两千三百零二万四千二百零三", str(123024203))
progress += x_test_conversion("四千万零一十", str(40000010))
progress += x_test_conversion("三十四万五千五", str(345500))
progress += x_test_conversion("四亿二十万零九百零一", str(400200901))
progress += x_test_conversion("四亿零二十万零九百零一", str(400200901))
progress += x_test_conversion("两千万九千零一十", str(20009010))
progress += x_test_conversion("二十四万零二百二十二", str(240222))
progress += x_test_conversion("两千零十二", str(2012))
progress += x_test_conversion("四百零八万六千", str(4086000))
progress += x_test_conversion("五百零九万四千六百", str(5094600))
progress += x_test_conversion("二千一百六十万零九百", str(21600900))
progress += x_test_conversion("一亿一千九百万", str(119000000))
progress += x_test_conversion("六十七万五千四百三十二", str(675432))
progress += x_test_conversion("四亿五千零五十九万四千零一", str(450594001))
progress += x_test_conversion("四十五万零七百零三", str(450703))
progress += x_test_conversion("四百三十二万六千七百九十八", str(4326798))
progress += x_test_conversion("七十五万四千三百七十五", str(754375))
progress += x_test_conversion("二亿五千四百三十二万五千", str(254325000))
progress += x_test_conversion("二亿五千四百三十一万五千", str(254315000))
progress += x_test_conversion("四百零三万六千零五", str(4036005))
progress += x_test_conversion("三百六十万五千零七", str(3605007))
progress += x_test_conversion("七亿零二十万", str(700200000))
progress += x_test_conversion("三万零五百六十九", str(30569))
progress += x_test_conversion("一百亿", str(10000000000))
progress += x_test_conversion("一十亿", str(1000000000))
progress += x_test_conversion("一亿", str(100000000))
progress += x_test_conversion("一亿四千五万六千", str(140056000))
progress += x_test_conversion("百五", str(150))
progress += x_test_conversion("万五", str(15000))
progress += x_test_conversion("十二", str(12))
progress += x_test_conversion("零", str(0))
progress += x_test_conversion("三百零五", str(305))
progress += x_test_conversion("一千二百三十四亿五千六百七十八万九千", str(123456789000))
progress += x_test_conversion("一千一百一十一亿一千一百一十一万一千一百一十一", str(111111111111))
progress += x_test_conversion("一千零一亿一千一百一十一万一千一百一十一", str(100111111111))

# Error messages
progress += x_test_conversion("", "Your input is empty!")
progress += x_test_conversion("一萬千一百零十一亿一",
                              "一萬千一百零十一亿一 is too high, only numbers lower than 10^12 are allowed.")
progress += x_test_conversion("一萬千一百零十一亿一千一百零十一万四千七百五十二",
                              "一萬千一百零十一亿一千一百零十一万四千七百五十二 is too high, only numbers lower than 10^12 are allowed.")
progress += x_test_conversion("a",
                              "You need to input Chinese numerals, a is not a proper Chinese number!\nThe characters are not all numbers.")
progress += x_test_conversion("十十",
                              "You need to input Chinese numerals, 十十 is not a proper Chinese number!\nSame characters cannot be next to each other.")
progress += x_test_conversion("億億",
                              "You need to input Chinese numerals, 億億 is not a proper Chinese number!\nSame characters cannot be next to each other.")

print("\nDone!")
print("Successful tests: " + str(progress.count("success")))
print("Failed tests: " + str(progress.count("failure")))
