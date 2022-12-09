import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    #if MUST_JOIN.startswith("@"):
        #MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = "7756158007"
    API_HASH = "05c174b66cedccbb2e7756158007fa63"
    BOT_TOKEN = "5890248722:AAFhabP-LlF7-IKdMBWOdLE3__W4OVzAi1c"
    DATABASE_URL = "mongosh "mongodb+srv://cluster0.ohfjetd.mongodb.net/myFirstDatabase" --apiVersion 1 --username Elitesteffen"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "@Bring_out_your_feelings"
    #if MUST_JOIN.startswith("@"):
       # MUST_JOIN = MUST_JOIN[1:]
