from peewee import PostgresqlDatabase, Model, TextField

db = PostgresqlDatabase('hello_world', user='postgres', password='password', host='postgres', port=5432)

class HelloWorld(Model):
    class Meta:
        database = db
        table_name = "hello_world"
    welcome_message = TextField(null=True, column_name="welcome_message")
    welcome_user = TextField(null=True, column_name="welcome_user")

    def storeWelcomeMessageForUser(self, message, user):
        self.welcome_message = message
        self.welcome_user = user
        self.save()



