from uber.automated_emails import AutomatedEmailFixture
from uber.config import c
from uber.models import Attendee, Room
from uber.models import email
from uber.utils import days_before


# Janky monkeypatch AutomatedEmail.reconcile to fix hardcoded subjects.
_original_AutomatedEmail_reconcile = email.AutomatedEmail.reconcile

def _AutomatedEmail_reconcile(self, fixture):
    _original_AutomatedEmail_reconcile(self, fixture)
    if self.ident == 'band_charity_reminder':
        self.subject = '{} charity raffle reminder'.format(c.EVENT_NAME)
    return self

email.AutomatedEmail.reconcile = _AutomatedEmail_reconcile


AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} Check-in Barcode',
    'checkin_barcode.html',
    lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, c.FINAL_EMAIL_DEADLINE),
    ident='maglabs_checkin_barcode')

AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} FAQ',
    'prefest_faq.html',
    lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, c.FINAL_EMAIL_DEADLINE),
    ident='maglabs_prefest_faq')

AutomatedEmailFixture(
    Room,
    '{EVENT_NAME} Hotel Room Assignment Update',
    'hotel/room_assignment_update.txt',
    lambda r: r.locked_in,
    sender=c.ROOM_EMAIL_SENDER,
    ident='hotel_room_assignment_update')
