from converter_trillion import converter_main


def test_result_should_be_123024203():
    assert converter_main("一亿两千三百零二万四千二百零三") == str(123024203)


def test_result_should_be_40000010():
    assert converter_main("四千万零一十") == str(40000010)


def test_result_should_be_345500():
    assert converter_main("三十四万五千五") == str(345500)


def test_result_should_be_400200901a():
    assert converter_main("四亿二十万零九百零一") == str(400200901)


def test_result_should_be_400200901b():
    assert converter_main("四亿零二十万零九百零一") == str(400200901)


def test_result_should_be_20009010():
    assert converter_main("两千万九千零一十") == str(20009010)


def test_result_should_be_240222():
    assert converter_main("二十四万零二百二十二") == str(240222)


def test_result_should_be_2012():
    assert converter_main("两千零十二") == str(2012)


def test_result_should_be_4086000():
    assert converter_main("四百零八万六千") == str(4086000)


def test_result_should_be_5094600():
    assert converter_main("五百零九万四千六百") == str(5094600)


def test_result_should_be_21600900():
    assert converter_main("二千一百六十万零九百") == str(21600900)


def test_result_should_be_119000000():
    assert converter_main("一亿一千九百万") == str(119000000)


def test_result_should_be_675432():
    assert converter_main("六十七万五千四百三十二") == str(675432)


def test_result_should_be_450594001():
    assert converter_main("四亿五千零五十九万四千零一") == str(450594001)


def test_result_should_be_450703():
    assert converter_main("四十五万零七百零三") == str(450703)


def test_result_should_be_4326798():
    assert converter_main("四百三十二万六千七百九十八") == str(4326798)


def test_result_should_be_754375():
    assert converter_main("七十五万四千三百七十五") == str(754375)


def test_result_should_be_254325000():
    assert converter_main("二亿五千四百三十二万五千") == str(254325000)


def test_result_should_be_254315000():
    assert converter_main("二亿五千四百三十一万五千") == str(254315000)


def test_result_should_be_4036005():
    assert converter_main("四百零三万六千零五") == str(4036005)


def test_result_should_be_3605007():
    assert converter_main("三百六十万五千零七") == str(3605007)


def test_result_should_be_700200000():
    assert converter_main("七亿零二十万") == str(700200000)


def test_result_should_be_30569():
    assert converter_main("三万零五百六十九") == str(30569)


def test_result_should_be_10000000000():
    assert converter_main("一百亿") == str(10000000000)


def test_result_should_be_1000000000():
    assert converter_main("一十亿") == str(1000000000)


def test_result_should_be_100000000():
    assert converter_main("一亿") == str(100000000)


def test_result_should_be_140056000():
    assert converter_main("一亿四千五万六千") == str(140056000)


def test_result_should_be_150():
    assert converter_main("百五") == str(150)


def test_result_should_be_15000():
    assert converter_main("万五") == str(15000)


def test_result_should_be_12():
    assert converter_main("十二") == str(12)


def test_result_should_be_0():
    assert converter_main("零") == str(0)


def test_result_should_be_305():
    assert converter_main("三百零五") == str(305)


def test_result_should_be_123456789000():
    assert converter_main("一千二百三十四亿五千六百七十八万九千") == str(123456789000)


def test_result_should_be_111111111111():
    assert converter_main("一千一百一十一亿一千一百一十一万一千一百一十一") == str(111111111111)


def test_result_should_be_100111111111():
    assert converter_main("一千零一亿一千一百一十一万一千一百一十一") == str(100111111111)


def test_result_should_be_error_number_too_big_a():
    assert converter_main(
        "一萬千一百零十一亿一") == "一萬千一百零十一亿一 is too high, only numbers lower than 10^12 are allowed."


def test_result_should_be_error_number_too_big_b():
    assert converter_main(
        "一萬千一百零十一亿一千一百零十一万四千七百五十二") == "一萬千一百零十一亿一千一百零十一万四千七百五十二 is too high, only numbers lower than 10^12 are allowed."


def test_result_should_be_error_not_a_chinese_numeral():
    assert converter_main(
        "a") == "You need to input Chinese numerals, a is not a proper Chinese number!\nThe characters are not all numbers."


def test_result_should_be_error_same_chars_a():
    assert converter_main(
        "十十") == "You need to input Chinese numerals, 十十 is not a proper Chinese number!\nSame characters cannot be next to each other."


def test_result_should_be_error_same_chars_b():
    assert converter_main(
        "億億") == "You need to input Chinese numerals, 億億 is not a proper Chinese number!\nSame characters cannot be next to each other."
