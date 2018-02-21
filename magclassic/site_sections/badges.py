from uber.config import c
from uber.decorators import ajax_gettable, all_renderable, unrestricted


@all_renderable(c.PEOPLE, c.REG_AT_CON)
class Root:
    @unrestricted
    def animation(self):
        return {'sold': c.BADGES_SOLD}

    @ajax_gettable
    def stats(self):
        return {'sold': c.BADGES_SOLD}
