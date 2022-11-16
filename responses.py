from datetime import datetime

def responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hi','hello','hi!','Hello?'):
        return "Hello There!"
    
    if user_message in ('about','about?'):
        return "This is a telegram bot for a workshop"

    if user_message in ('time','time?', 'date','date?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H: %M, %S")
        return str(date_time)

    return "Sorry wrong input! Try to press /option for more information"