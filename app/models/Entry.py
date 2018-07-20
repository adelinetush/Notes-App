class Entry:
    def __init__(self, ID, username, title, notes, date):
        self.id  = ID
        self.username = username
        self.title = title
        self.notes = notes
        self.date = date

    def get_title(self):
        return self.title

    def get_notes(self):
        return self.notes

    def set_title(self, title):
        self.title = title
        return title

    def set_notes(self, notes):
        self.notes = notes
        return self.notes

    def set_date(self, date):
        self.date = date
        return date

    def set_date(self, date):
        self.date = date
        return self.date

    def serialize(self):
            return {
            'id':self.id,
            'username':self.username,
            'title':self.title,
            'notes':self.notes
            'date':self.date
    }