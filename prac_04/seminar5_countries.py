

def main()
    country_to_data = load_data(filename)
    display_details(country_to_data)


def load_data(filename):
    country_to_data ={}
    with open(filename) as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            record[2] = int(record[2].replace())