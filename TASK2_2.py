import sqlite3

class ServiceRecord:
    # init will take in all attributes since none of them are fixed at point of creation
    # no need to privatise attributes to facilitate access of attributes and inheritance later on
    def __init__(self, Sender, AccessDate, Status, AppType):
        self.Sender = Sender
        self.AccessDate = AccessDate
        self.Status = Status
        self.AppType = AppType
    
    def isSuccess(self):
        return self.Status == 200
    
    def getAppType(self):
        return self.AppType


# connect to the db file
db = sqlite3.connect('ServiceLog.db')

### optional but recommended: to clear the table
# (in case of errors halfway through execution, we ensure we start on clean slate on the next run)
# because of AUTOINCREMENT field, we need to DROP And re-create the table
db.execute('''DROP TABLE Log''')
db.execute('''CREATE TABLE "Log" (
                "LogID"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "Sender"	TEXT,
                "AccessDate"	TEXT,
                "Status"	INTEGER,
                "AppType"	TEXT
            );''')
db.commit()

# open and process the file
file = open('LOG.txt', 'r')

for line in file:
    line = line.strip()

    # we don't assign to variable names on the left
    # because we're not sure how many parts it will split into
    # (can be 3 or 4 parts)
    line = line.split(' ') # split by space

    # line is now a list (either 3 or 4 items)

    # decide what type of log it is based on the length of the line

    if len(line) == 4: # must be IP address line

        # create instance of ServiceRecord with the information
        # remember to cast Status (line[2]) to integer
        record = ServiceRecord(line[0], line[1], int(line[2]), line[3])

    else: # must be length 3, so it's a phone number line

        # create instance of ServiceRecord with the information
        # remember to cast Status (line[2]) to integer
        # AppType is going to be an empty string since it's not provided
        record = ServiceRecord(line[0], line[1], int(line[2]), '')

    # insert the record, regardless of what it is, into the db
    # LogID does not need to be inserted as it is auto-incremented
    db.execute('''INSERT INTO Log(Sender, AccessDate, Status, AppType)
                  VALUES (?, ?, ?, ?)''', (record.Sender, record.AccessDate, record.Status, record.AppType))

    db.commit() # remember to commit in order to save the changes to the db
 
file.close() # remember to close the file

db.close() # remember to close the db