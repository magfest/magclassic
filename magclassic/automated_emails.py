from magclassic import *
from hotel import *

AutomatedEmail(Attendee, '{EVENT_NAME} Check-in Barcode', 'checkin_barcode.html',
               lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, c.FINAL_EMAIL_DEADLINE),
               ident='maglabs_checkin_barcode')

AutomatedEmail(Attendee, '{EVENT_NAME} FAQ', 'prefest_faq.html',
               lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, c.FINAL_EMAIL_DEADLINE),
               ident='maglabs_prefest_faq')

AutomatedEmail(Room, '{EVENT_NAME} Hotel Room Assignment Update', 'room_assignment_update.txt', lambda r: r.locked_in,
               sender=c.ROOM_EMAIL_SENDER,
               ident='hotel_room_assignment_update')
