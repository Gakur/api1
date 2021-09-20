class UserModels():
    """
    Create a class for the user operations
    """
    users = {}

    def __init__(self, username, email, password, confirm_password, work_time, break_time, break_task) -> None:
        """
        Function to initialize the user models
        """
        self.id = len(UserModels.users) + 1
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.work_time = work_time
        self.break_time = break_time
        self.break_task = break_task

    def save_user(self):
        """
        Method to register a user instance and update the data structure
        """
        user_record = dict(
            id = self.id,
            username = self.username,
            email = self.email,
            password = self.password,
            confirm_password = self.confirm_password,
            work_time = self.work_time,
            break_time = self.break_time,
            break_task = self.break_task
        )
        self.users.update({
            self.id: user_record
        })