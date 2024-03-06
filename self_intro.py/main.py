import random
import pyperclip

def generate_about(name, degree, position, company, skills):
    intros = [
        f"👋 Hello! I'm {name}, an {position} at {company} with a {degree}. I specialize in {skills}. Passionate about leveraging technology to drive innovation and solve real-world problems. Let's connect!",
        f"🌟 Hi there! I'm {name}, currently working as an {position} at {company}. I hold a {degree} and have expertise in {skills}. Excited to collaborate and contribute to impactful projects!",
        f"🚀 Welcome! I'm {name}, a {position} at {company} with a background in {degree}. My skills include {skills}. Dedicated to continuous learning and growth. Let's build something amazing together!"
    ]
    return random.choice(intros)

# Function to copy the about section to the clipboard
def copy_to_clipboard(content):
    pyperclip.copy(content)
    print("The generated about section has been copied to the clipboard.")

# Function to save the about section to a file
def save_to_file(content):
    filename = "about_section.txt"
    with open(filename, "a", encoding="utf-8") as file:  # Append mode
        file.write(content + "\n")  # Add a newline after each section
    print(f"The generated about section has been saved to {filename}.")

# Sample information
name = input("Name:\n")
degree = input("Qualification:\n")
position = input("Role:\n")
company = input("Company:\n")
skills = input("Skills(use comma while writing skills):\n")

# Generate About section
about = generate_about(name, degree, position, company, skills)
print("Generated About Section:\n", about)

# Prompt the user for action
while True:
    action = input("\nPress c --- To copy about to the clipboard.\nPress s --- To save about to the about_section.txt file.\nPress b --- To work the above both functionalities.\n").lower()
    if action == 'c':
        copy_to_clipboard(about)
        break
    elif action == 's':
        save_to_file(about)
        break
    elif action == 'b':
        copy_to_clipboard(about)
        save_to_file(about)
        break
    else:
        print("Invalid input. Please enter 'c', 's', or 'b'.")
