from durak import текущая_ситуация
from pip._internal.utils.misc import capturedoutput

from durak import  текущаяситуация, основнаяигра


def testвыводситуации(игроки):
    текущаяситуация(игроки)

    ожидаемый_вывод = "Игрок 1: 6 карт\nИгрок 2: 6 карт"

    assert capturedoutput() == ожидаемыйвывод


def testосновнаяигра():
    основная_игра(2)

    assert "Игра завершена" in captured_output()