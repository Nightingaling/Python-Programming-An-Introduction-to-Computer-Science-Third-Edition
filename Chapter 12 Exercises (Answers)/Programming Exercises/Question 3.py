class Attendance():

    def __init__(self):
        infile = open('attendees.txt', 'r')
        self.attendees = {}
        for i in infile.readlines():
            name = i.split(",")[0]
            info = i.rstrip().split(",")[1:]
            self.attendees[name] = info
        infile.close()

    def add(self):
        name = input('Name of attendee: ')
        company = input('Attendee Company: ')
        state = input('Which state does the attendee live in: ')
        email = input('Attendee Email: ')
        self.attendees[name] = [company,state,email]
        print('The new attendee has been added')
        self.update()

    def delete(self, name):
        if name in self.attendees:
            del self.attendees[name]
            print(name, "has been deleted from the attendance list")
            self.update()
        else:
            print('Invalid name. Please try again.')

    def DisplayInformationOn(self, name):
        if name in self.attendees:
            company = self.attendees[name][0]
            state = self.attendees[name][1]
            email = self.attendees[name][2]
            return "{0}:\nCompany: {1}\nState: {2}\nEmail: {3}".format(name,company,state,email)
        else:
            return 'Attendee not found'

    def allAttendeesEmail(self):
        for name in self.attendees:
            email = self.attendees[name][2]
            print("{0}: {1}".format(name, email))

    def allAttendeesEmailfrom(self, state):
        for name in self.attendees:
            if self.attendees[name][1] == state:
                email = self.attendees[name][2]
                print("{0}: {1}".format(name, email))

    def update(self):
        outfile = open("attendees.txt", 'w')
        for name in self.attendees:
            company = self.attendees[name][0]
            state = self.attendees[name][1]
            email = self.attendees[name][2]
            print("{0},{1},{2},{3}".format(name,company,state,email), file=outfile)
        outfile.close()
        print('The attendees list has been updated.')


def main():
    conference = Attendance()
    while True:
        print("\n1.Add 2.View 3.Delete 4.List All 5.List by State 6.Exit")
        choice = int(input("Select: "))
        if choice == 1:
            conference.add()
        elif choice == 2:
            name = input('Name of attendee: ')
            print(conference.DisplayInformationOn(name))
        elif choice == 3:
            name = input('Name of attendee: ')
            conference.delete(name)
        elif choice == 4:
            conference.allAttendeesEmail()
        elif choice == 5:
            state = input('Which state: ')
            conference.allAttendeesEmailfrom(state)
        elif choice == 6:
            conference.update()
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
