from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from src.database import engine, URLS


class Database:

    @staticmethod
    def create_session():
        return sessionmaker(bind=engine)()

    def insert(self, long_url, short_url):
        session = self.create_session()
        row = URLS(original_url=long_url, short_url=short_url)
        session.add(row)
        session.commit()
        session.close()

    def delete(self, url):
        session = self.create_session()
        query = select(URLS).where(URLS.short_url == url)
        result = session.execute(query)
        record = result.fetchone()
        if record:
            session.delete(record[0])
            session.commit()
        session.close()

    def get_long_url(self, url):
        session = self.create_session()
        query = select(URLS).where(URLS.short_url == url)
        result = session.execute(query)
        record = result.fetchone()
        session.close()
        return record[0].original_url if record else None

    def get_short_url(self, url):
        session = self.create_session()
        query = select(URLS).where(URLS.original_url == url)
        result = session.execute(query)
        session.close()
        return result.fetchone()
