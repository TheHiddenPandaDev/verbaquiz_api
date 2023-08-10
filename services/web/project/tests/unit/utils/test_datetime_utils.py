from datetime import datetime, timedelta
import unittest

from project.utils.datetime_utils import get_current_datetime, get_local_datetime, readable_datetime


class DateTimeTest(unittest.TestCase):

    def test_get_current_datetime(
        self,
    ):
        current_datetime = get_current_datetime(datetime.now())
        two_hours_from_now = datetime.now()

        self.assertEqual(
            current_datetime.strftime("%d-%m-%Y %H:%M:%S"),
            two_hours_from_now.strftime("%d-%m-%Y %H:%M:%S")
        )

    def test_get_local_datetime(
        self,
    ):
        current_datetime = get_local_datetime(datetime.now())
        two_hours_from_now = datetime.now() + timedelta(hours=2)

        self.assertEqual(
            current_datetime.strftime("%d-%m-%Y %H:%M:%S"),
            two_hours_from_now.strftime("%d-%m-%Y %H:%M:%S")
        )

    def test_readable_datetime(
        self,
    ):
        current_datetime: datetime = datetime.now()
        readable_current_datetime = readable_datetime(current_datetime)

        self.assertEqual(
            datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            readable_current_datetime
        )


if __name__ == '__main__':
    unittest.main()
