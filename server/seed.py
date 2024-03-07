import random
from models import db, Event, User, EventNotification
from faker import Faker
from app import app

fake = Faker()

# Sample event data
event_data = [
    {
        'name': 'MMU Tech Meet Up',
        'description': "Let's gather together and make unforgettable memories at the CIT Meet-Up!",
        'image_url': 'https://i.pinimg.com/474x/8d/fb/67/8dfb67bb3522ac4360c6de1fa21205fe.jpg',
        'notification_message': "Let's gather together and make unforgettable memories at the CIT Annual Meet-Up!",
    },
    {
        'name': 'CU 23rd March',
        'description': 'Join us for an uplifting evening of fellowship, worship, and spiritual enrichment at our CU Christian Fellowship Night.',
        'image_url': 'https://i.pinimg.com/474x/b7/53/4d/b7534d438dea179990633217c8e8016c.jpg',
        'notification_message': "Don't miss this opportunity to deepen your faith and build meaningful relationships with God",
    },
    {
        'name': 'Movie Night at Two Rivers',
        'description': 'Experience the magic of cinema under the stars at our cozy movie night!.',
        'image_url': 'https://i.pinimg.com/474x/7d/92/46/7d92460503240934c7834a17601410e6.jpg',
        'notification_message': "Join us for a movie night under the stars with your friends and family.",
    },
    {
        'name': 'Charity Gala Dinner',
        'description': 'Support a good cause while enjoying a glamorous evening. Join us for the Charity Gala Dinner benefiting local charities.',
        'image_url': 'https://i.pinimg.com/564x/ff/2e/cf/ff2ecf5a3d7ccd9cae851ec27e463a62.jpg',
        'notification_message': "Join us for the annual charity gala dinner to make a difference.",
    },
    {
        'name': 'Art Exhibition',
        'description': 'Explore the world of art and creativity. Our art exhibition showcases breathtaking works that go "Beyond Colors."',
        'image_url': 'https://i.pinimg.com/474x/0c/41/10/0c411086902febd99c6b024229989f69.jpg',
        'notification_message': "Experience art like never before at our 'Beyond Colors' exhibition.",
    },
    {
        'name': 'Fitness Bootcamp Challenge',
        'description': 'Challenge yourself with a fitness bootcamp like no other. Get fit, have fun, and meet new fitness buddies.',
        'image_url': 'https://i.pinimg.com/564x/8c/53/fe/8c53feb9be638a6fe6a8a7ba7c101f2d.jpg',
        'notification_message': "Get ready to challenge yourself at our fitness bootcamp!",
    },
    {
        'name': 'Local Food Festival',
        'description': 'Indulge in the flavors of your local community. Sample delicious dishes and discover hidden culinary gems.',
        'image_url': 'https://i.pinimg.com/474x/bf/cf/f3/bfcff33b6f1b71da80011d727e2674dc.jpg',
        'notification_message': "Indulge in delicious local cuisines at our food festival.",
    }
]

with app.app_context():
    # Clear existing data
    EventNotification.query.delete()
    Event.query.delete()
    User.query.delete()

    
    # Function to create random events with organizers
    def create_events_with_organizers(num_events, num_organizers):
        events = []
        for i in range(num_events):
            organizer = random.choice(User.query.all())
            event_data_entry = event_data[i]  # Use the event_data in order
            fake_location = fake.city() + ', ' + fake.country()
            
            event = Event(
                organizer_id=organizer.user_id,
                poster=event_data_entry['image_url'],
                name=event_data_entry['name'],
                date=fake.date_time_this_decade(),
                location=fake_location,
                description=event_data_entry['description'],
                capacity=fake.random_int(min=10, max=200),
            )
            db.session.add(event)
            events.append(event)

        db.session.commit()
        return events

    # Function to create random event notifications
    def create_event_notifications(num_notifications, events):
        notifications = []
        for _ in range(num_notifications):
            event = random.choice(events)
            event_data_entry = event_data[events.index(event)]  # Match event data to events
            notification = EventNotification(
                event_id=event.event_id,
                message=event_data_entry['notification_message'],
            )
            db.session.add(notification)
            notifications.append(notification)

        db.session.commit()
        return notifications

    if __name__ == '__main__':
        num_users = 10
        num_events = 7
        num_organizers = 5
        num_notifications = 10

        # Create users
        create_users(num_users)

        # Create events with organizers
        events = create_events_with_organizers(num_events, num_organizers)

        # Create event notifications
        create_event_notifications(num_notifications, events)

        print("Seed data generated successfully.")

    