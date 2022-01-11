class User:

    def __init__(self, email, name, password, title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = title

    def change_password(self, password):
        self.password = password

    def change_job_title(self, title):
        self.title = title

    def get_user_info(self):
        print(f"{self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}.")