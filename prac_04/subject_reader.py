

def main():
    data = get_data()
    display_subject_details(data)

def get_data():
    input_file = open(subject_data.txt)
    subject_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data

def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        subject_code, lecturer, num_students = subject
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")

main()
