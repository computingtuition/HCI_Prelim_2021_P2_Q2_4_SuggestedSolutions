### NOTE: you will need to import the object(s) you need
### from the previous tasks' files
from TASK2_3 import AppServiceRecord, SmsServiceRecord

import flask, sqlite3

app = flask.Flask(__name__)

# only one page needed for this question!
@app.route('/')
def home():

    # connect to the db to retrieve all data
    db = sqlite3.connect('ServiceLog.db')

    cursor = db.execute('''SELECT Sender, AccessDate, AppType, Status
                           FROM Log''') # no WHERE criteria needed

    data = cursor.fetchall() # a list of tuples will be fetched
    
    db.close()

    # we need to loop through the data list
    # and replace all tuples with their corresponding object representation
    for i in range(len(data)):
        
        # use AppType (index 2) to check which type of object
        
        if data[i][2] == '': # SmsServiceRecord
            # remember to cast Status to integer
            record = SmsServiceRecord(data[i][0], data[i][1], int(data[i][3]), data[i][2])

        else: # AppServiceRecord
            # remember to cast Status to integer
            record = AppServiceRecord(data[i][0], data[i][1], int(data[i][3]), data[i][2])

        # replace the existing tuple of data with the record object created
        data[i] = record
            

    return flask.render_template('table.html', data = data)

# this is only for deploying on Google Cloud (so that you can preview online)
app.run('0.0.0.0', port=8080)

# for running on own computer, use this
# app.run()
