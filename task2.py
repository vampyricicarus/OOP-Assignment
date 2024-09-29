
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []  # List to store participant names

    def add_participant(self, new_part):
        self.participants.append(new_part)  # Add new participant to the list
        print(f"Added {new_part} to the list.")

    def get_participant_count(self):
        part_count = len(self.participants)  # Count participants in the list
        print(f"There are {part_count} participants.")
        return part_count

# Create an instance of Event
event = Event("Festival", "June 3")
event.add_participant("Robby")
event.add_participant("Joseph")
count = event.get_participant_count()  
