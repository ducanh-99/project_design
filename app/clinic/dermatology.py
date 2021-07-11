from .clinic_base import ClinicBase
from app.core.singleton import Singleton


class Dermatology(Singleton, ClinicBase):
    id_clinic = 3
    queue = []

    def __init__(self) -> None:
        super().__init__()
