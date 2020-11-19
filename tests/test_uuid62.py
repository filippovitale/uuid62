from uuid import UUID

from hypothesis import assume, given
from hypothesis.strategies import binary, builds
from pytest import raises

from uuid62 import decode_base62, encode_base62, uuid_base62


@given(builds(uuid_base62))
def test_uuid_base62(uuid):
    base62_str = decode_base62(uuid)
    assert uuid == encode_base62(base62_str)


@given(binary(min_size=16, max_size=16))
def test_encode_decode_base62(b):
    assume(b != b"\x00" * 16)
    uuid = UUID(bytes=b)
    assert uuid == decode_base62(encode_base62(uuid))


def test_encode_uuid_zero():
    with raises(ValueError):
        b = b"\x00" * 16
        uuid = UUID(bytes=b)
        decode_base62(encode_base62(uuid))
