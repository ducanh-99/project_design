from .clinic_base import ClinicBase
from app.core.singleton import Singleton


class Ophthalmology(Singleton, ClinicBase):
    id_clinic = 1

    def __init__(self) -> None:
        super().__init__()
