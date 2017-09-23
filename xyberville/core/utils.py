from datetime import datetime as _datetime
import random
import string
from contextlib import contextmanager
from xyberville.apps.profiles.models import Profile
from django.utils import timezone


def prepare_datetime_range(start, end, tzinfo=None):
    start = _datetime.combine(start, _datetime.min.time())
    start = timezone.localtime(timezone.make_aware(start))
    end = _datetime.combine(end, _datetime.max.time())
    end = timezone.localtime(timezone.make_aware(end))

    return start, end


def generate_random_string(
        length=8,
        chars=string.ascii_lowercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(length))


def generate_username(name, tanggal_lahir):
    name = str(name.split(" ")[0]).upper()
    date = str(tanggal_lahir).split("-")[2] + str(tanggal_lahir).split("-")[1]
    return name + date


@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
