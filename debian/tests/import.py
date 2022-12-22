import uuid
import systemd.id128

u = systemd.id128.randomize()

assert isinstance(u, uuid.UUID)
print('UUID:', u)
