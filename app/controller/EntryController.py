from app.models.model.Model import Entry
from app.models import db

class EntryController:
    """Manage Entry Controller"""
    def __init__(self):
        self.entries = [];
        self.count = 1


    def add_entry(self, ent):
        """Store Entry to Database"""
        self.entries = [];
        if not db.session.query(Entry).filter(Entry.title == ent['title']).count():
            c = Entry(ent['email'],ent['title'],ent['notes'],ent['date'])
            db.session.add(c)
            db.session.commit()
        for ent in Entry.query.filter(Entry.email == ent['email']):
            self.entries.append(ent.serialize())
        return self.entries

    def get_entry_id(self, id):
        li = [];
        id = int(id)
        for entry in Entry.query:
            if id == enrty.id:
                li.append(entry.serialize())
        return li

    def get_user_entry(self,email):
        gue = []
        for ent in Entry.query.filter(Entry.email == email):
            gue.append(ent.serialize())
        return gue

    def get_all_entry(self):
        gae = []
        for ent in Entry.query:
            gae.append(ent.serialize())
        return gae

    def update_entry(self, ent):
        id = int(ent['id'])
        for entry in Entry.query.filter(Entry.id == id):
            entry.title = ent['title']
            entry.notes = ent['notes']
            entry.date = ent['date']
            db.session.commit();
            return True
        return False;
        
    def delete_entry(self, id):
        id = int(id)
        if(Entry.query.filter(Entry.id == id).count()>0):
            for ent in Entry.query.filter(Entry.id == id):
                db.session.delete(ent)
                db.session.commit()
            return True
        return False;

    def return_entry(self, id):
        id = int(id)
        ae = [];
        for entry in Entry.query.filter(Entry.id == id):
            ae.append(entry.serialize())
        return ae