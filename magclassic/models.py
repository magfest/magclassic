from magclassic import *


@Session.model_mixin
class Attendee:
    extra_donation = Column(Integer, default=0)

    @cost_property
    def donation_cost(self):
        return self.extra_donation or 0

    @presave_adjustment
    def set_empty_donation(self):
        if not self.extra_donation:
            self.extra_donation = 0

    @property
    def addons(self):
        return ['Extra donation of ${}'.format(self.extra_donation)] if self.extra_donation else []