# MIT License
#
# Copyright (c) 2020 Filippo Vitale
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from functools import reduce
from uuid import uuid4, UUID

BASE62_INDEX_TABLE = ("0123456789"
                      "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                      "abcdefghijklmnopqrstuvwxyz")
BASE62_SIZE = len(BASE62_INDEX_TABLE)
BASE62_INDEX_DICT = {c: i for i, c in enumerate(BASE62_INDEX_TABLE)}


def encode_base62_int(uuid_internal_state: int) -> str:
    """Encode the integer representation of the UUID as Base62."""
    if uuid_internal_state <= 0:
        raise ValueError("UUID integer representation must be > zero")

    i = uuid_internal_state
    base62_reversed = ""
    while i > 0:
        j = i % BASE62_SIZE
        base62_reversed += BASE62_INDEX_TABLE[j]
        i //= BASE62_SIZE

    return base62_reversed[::-1]  # reverse the string


def decode_base62_int(uuid_base62: str) -> int:
    """Decode a Base62 string to an integer."""
    return reduce(
        lambda a, c: a + (BASE62_SIZE ** c[0]) * BASE62_INDEX_DICT.get(c[1]),
        enumerate(uuid_base62[::-1]), 0)


def encode_base62(uuid: UUID) -> str:
    """Encode a UUID as a Base62 string."""
    return encode_base62_int(uuid.int)


def decode_base62(uuid_base62: str) -> UUID:
    """Decode the Base62 string representation to a UUID object."""
    return UUID(int=decode_base62_int(uuid_base62))


def uuid_base62() -> str:
    """Generate a UUID and return the Base62 string representation."""
    uuid_internal_state = uuid4().int
    return encode_base62_int(uuid_internal_state)
