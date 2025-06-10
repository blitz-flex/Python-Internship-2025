from ..extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey

class ProgramRegistration(db.Model):
    __tablename__ = 'program_registrations'

    id = Column(Integer, primary_key=True)
    # ეს არის უცხო გასაღები, რომელიც user_accounts ცხრილს უკავშირდება
    user_id = Column(Integer, ForeignKey('user_accounts.id'), nullable=False)
    # ველების სახელები შევცვალეთ, რომ უფრო აღწერითი იყოს
    full_name = Column(String(100), nullable=False)
    program = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)

    # განვსაზღვრავთ ორმხრივ კავშირს UserAccount მოდელთან
    user = db.relationship('UserAccount', back_populates='registrations')