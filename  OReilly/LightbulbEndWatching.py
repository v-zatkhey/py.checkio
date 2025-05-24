# Taken from mission Lightbulb Start Watching

from datetime import datetime, timedelta
from typing import List, Optional

def _sum_light(els: List[datetime]) -> int:
    result = timedelta()
    for i in range(len(els)//2):
        result = result + els[2 * i + 1] - els[2 * i]
    return int(result.total_seconds())


def sum_light(
    els: List[datetime],
    start_watching: Optional[datetime] = None,
    end_watching: Optional[datetime] = None,
) -> int:
    """
    how long the light bulb has been turned on
    """
    if (start_watching == None or end_watching == None) and len(els) % 2 == 1:
        raise "Missing parameter"

    if start_watching == None:
        start_watching = datetime(1970,1,1,0,0,0)
    if end_watching == None:
        end_watching = datetime(9999,12,31,23,59,59)

    before_els = list(filter(lambda x: x < start_watching, els))
    rest_els = els[len(before_els):]
    if len(before_els) % 2 == 1:
        rest_els = [start_watching] + rest_els

    rest_els = list(filter(lambda x: x < end_watching, rest_els))
    if len(rest_els) % 2 == 1:
        rest_els = rest_els + [end_watching]

    return _sum_light(rest_els)


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
    )

    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 0),
            end_watching=datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 7),
        )
        == 7
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 3),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 7
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 30, 0),
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 20
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 9, 50, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 9, 0, 0),
            datetime(2015, 1, 12, 10, 5, 0),
        )
        == 300
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 12, 0, 0),
        )
        == 310
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 11, 10, 0),
        )
        == 300
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 20
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 10, 0),
            datetime(2015, 1, 12, 10, 20, 20),
        )
        == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 10, 0),
            datetime(2015, 1, 12, 10, 20, 20),
        )
        == 1220
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 9, 0),
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 9, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )

    print(
        "The third mission in series is completed? Click 'Check' to earn cool rewards!"
    )
