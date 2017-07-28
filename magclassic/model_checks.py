from magclassic import *


@validation.Attendee
def extra_donation_valid(attendee):
    try:
        extra_donation = int(float(attendee.extra_donation if attendee.extra_donation else 0))
        if extra_donation < 0:
            return 'Extra Donation must be a number that is 0 or higher.'
    except:
        return "What you entered for Extra Donation ({}) isn't even a number".format(attendee.extra_donation)