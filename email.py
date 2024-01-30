### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    
    # Create 3 sample emails and add it to the Inbox list. 
    email1 = Email("sender1@example.com", "Water", "Remember to stay hydrated")
    email2 = Email("sender2@example.com", "Congratulations!", "Well done for being our 100th visitor")
    email3 = Email("sender3@example.com", "Important Annoucement", "That show you love returns Tuesday at 9")
    inbox.extend([email1, email2, email3])


def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    print("\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[INBOX]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
    for index, email in enumerate(inbox):
        if email.has_been_read:
            print(f"\n════════════════ READ ✉ >> {index} : {email.subject_line}")
        else:
            print(f"\n════════════════ UNREAD ✉ >> {index} : {email.subject_line}")


def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email = inbox[index]
    print("\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[INBOX]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n")
    print(f"\n════════════════ ✉ From >> {email.email_address}\nSubject: {email.subject_line}\n\n{email.email_content}\n")
    email.mark_as_read()
    print(f"Email from {email.email_address} marked as read.\n")
    print("\n════════════════════════════════════════════════════════════════\n")



# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.
menu = True


while True:
    try:
        user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    

    
        if user_choice == 1:
        # Add logic here to read an email.
            list_emails()
            try:
                email_index = int(input("\nEnter the index of the email you want to read: \n"))
                print()
                read_email(email_index)
            except ValueError:
                print("\nInvalid input detected\n")
            except IndexError:
                print(f"\nEmail {email_index} does not exist.\n")
                
        
        elif user_choice == 2:
        # Add logic here to view unread emails.
            unread_emails = [email for email in inbox if not email.has_been_read]
            if unread_emails:
                print("Unread Emails:")
                for email in unread_emails:
                    print(email.subject_line)
                print()
            else:
                print("\nNo unread emails.\n")
            
        elif user_choice == 3:
            # Add logic here to quit appplication.
            print("\nGoodbye!")
            break

        else:
            print("\nOops - incorrect input.\n")
    except ValueError:
        print("\nInvalid input, please try again.\n")
    
