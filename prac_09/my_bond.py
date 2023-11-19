class MusicalGroup:
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def perform(self):
        """Simulate each member playing their musical instrument."""
        for member in self.members:
            if member.instruments:  # If the member has instruments
                for instrument in member.instruments:
                    print(f"{member.name} is performing with: {instrument}")
            else:
                print(f"{member.name} needs a musical instrument!")

    def __str__(self):
        """Return a string representation of the musical group and its members."""
        return f"{self.group_name} ({', '.join(str(member) for member in self.members)})"

class Musician:
    def __init__(self, name):
        self.name = name
        self.instruments = []

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def __str__(self):
        """Return a string representation of the musician."""
        instruments_str = ', '.join(str(instrument) for instrument in self.instruments)
        return f"{self.name} ([{instruments_str}])"

class MusicalInstrument:
    def __init__(self, instrument_name, creation_year, instrument_value):
        self.instrument_name = instrument_name
        self.creation_year = creation_year
        self.instrument_value = instrument_value

    def __str__(self):
        """Return a string representation of the musical instrument."""
        return f"{self.instrument_name} ({self.creation_year}) : ${self.instrument_value:.2f}"
