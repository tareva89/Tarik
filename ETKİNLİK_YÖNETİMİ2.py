import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

    def __str__(self):
        return f"{self.name} ({self.date}, {self.location})"


class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class Ticket:
    def __init__(self, event, participant, price):
        self.event = event
        self.participant = participant
        self.price = price

    def __str__(self):
        return f"Ticket for {self.event} - {self.participant} ({self.price}$)"


class EventManagementSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Event Management System')
        self.setGeometry(100, 100, 400, 300)

        self.label_event_name = QLabel('Event Name:')
        self.input_event_name = QLineEdit()
        self.label_event_date = QLabel('Event Date:')
        self.input_event_date = QLineEdit()
        self.label_event_location = QLabel('Event Location:')
        self.input_event_location = QLineEdit()

        self.label_participant_name = QLabel('Participant Name:')
        self.input_participant_name = QLineEdit()
        self.label_participant_email = QLabel('Participant Email:')
        self.input_participant_email = QLineEdit()

        self.label_ticket_price = QLabel('Ticket Price:')
        self.input_ticket_price = QLineEdit()

        self.button_create_event = QPushButton('Create Event')
        self.button_create_event.clicked.connect(self.create_event)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_event_name)
        self.layout.addWidget(self.input_event_name)
        self.layout.addWidget(self.label_event_date)
        self.layout.addWidget(self.input_event_date)
        self.layout.addWidget(self.label_event_location)
        self.layout.addWidget(self.input_event_location)
        self.layout.addWidget(self.label_participant_name)
        self.layout.addWidget(self.input_participant_name)
        self.layout.addWidget(self.label_participant_email)
        self.layout.addWidget(self.input_participant_email)
        self.layout.addWidget(self.label_ticket_price)
        self.layout.addWidget(self.input_ticket_price)
        self.layout.addWidget(self.button_create_event)

        self.setLayout(self.layout)

        self.events = []
        self.participants = []
        self.tickets = []

    def create_event(self):
        event_name = self.input_event_name.text()
        event_date = self.input_event_date.text()
        event_location = self.input_event_location.text()

        participant_name = self.input_participant_name.text()
        participant_email = self.input_participant_email.text()

        ticket_price = self.input_ticket_price.text()

        if event_name and event_date and event_location and participant_name and participant_email and ticket_price:
            event = Event(event_name, event_date, event_location)
            participant = Participant(participant_name, participant_email)
            ticket = Ticket(event, participant, ticket_price)

            self.events.append(event)
            self.participants.append(participant)
            self.tickets.append(ticket)

            QMessageBox.information(self, 'Success', 'Event and ticket created successfully.')
            self.clear_inputs()
        else:
            QMessageBox.warning(self, 'Error', 'Please fill all fields.')

    def clear_inputs(self):
        self.input_event_name.clear()
        self.input_event_date.clear()
        self.input_event_location.clear()
        self.input_participant_name.clear()
        self.input_participant_email.clear()
        self.input_ticket_price.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EventManagementSystem()
    window.show()
    sys.exit(app.exec_())