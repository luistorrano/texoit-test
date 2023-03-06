from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Repository(object):
    def __init__(self, db_connection_string=None):
        if not db_connection_string:
            db_connection_string = "sqlite:///movieslist.db"
        
        self.engine = create_engine(db_connection_string)
        self.session = self.create_session()


    def create_session(self):
        return sessionmaker(bind=self.engine)()

    def get(self, model, my_id):
        try:
            return self.session.query(model).get(my_id)
        except Exception as e:
            print(f'Exception on get {str(e)}')
            session.rollback()
        finally:
            self.close()

    def add(self, entity):
        try:
            self.session.add(entity)
            self.session.commit()
        except Exception as e:
            print(f'Exception on add {str(e)}')
            self.session.rollback()
        finally:
            self.close()

    def create_table(self, entity):
        try:
            entity.__table__.create(self.engine, checkfirst=True)
        except Exception as e:
            print(f'Exception on create table {str(e)}')
        finally:
            self.close()

    def query(self, model):
        try:
            return self.session.query(model)
        except Exception as e:
            print(f'Exception on query {str(e)}')
            self.session.rollback()

    def get_by_field(self, model, field, value):
        try:
            query = self.query(model)
            return query.filter(field == value)
        except Exception as e:
            print(f'Exception on get_by_field {str(e)}')
        finally:
            self.close()

    def close(self):
        try:
            if self.session:
                self.session.close()
        except Exception as e:
            print(f'Exception on close {str(e)}')