#!/usr/bin/python3

import uuid

random_uuid = uuid.uuid4()
print(random_uuid)

uuid_string = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
uuid_parsed = uuid.UUID(uuid_string)
print(uuid_parsed)
