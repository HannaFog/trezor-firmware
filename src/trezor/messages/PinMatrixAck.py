# Automatically generated by pb2py
import protobuf as p


class PinMatrixAck(p.MessageType):
    FIELDS = {
        1: ('pin', p.UnicodeType, 0),  # required
    }
    MESSAGE_WIRE_TYPE = 19

    def __init__(
        self,
        pin: str = None,
        **kwargs,
    ):
        self.pin = pin
        p.MessageType.__init__(self, **kwargs)