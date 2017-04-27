import random
from uber.common import *


@all_renderable(c.PEOPLE, c.REG_AT_CON)
class Root:
    @unrestricted
    def badges_animation(self):
        return {'sold': c.BADGES_SOLD}

    @ajax_gettable
    def badge_stats(self):
        return {'sold': c.BADGES_SOLD}
