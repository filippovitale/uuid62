# uuid62

[Base62](https://en.wikipedia.org/wiki/Base62) [UUID](https://www.ietf.org/rfc/rfc4122.txt) generator


## Usage

```python
In [1]: import uuid62

In [2]: uuid62.uuid_base62()
Out[2]: '62NkbROZmSdqSsNnJTKBpj'

In [3]: uuid62.decode_base62(Out[2])
Out[3]: UUID('c6676fec-54de-46ff-865e-db3eaedb7743')

In [4]: uuid62.encode_base62(Out[3])
Out[4]: '62NkbROZmSdqSsNnJTKBpj'
```
