from .clinic_base import ClinicBase
from app.core.singleton import Singleton


class Oncology(Singleton, ClinicBase):
    id_clinic = 8
    queue = []

    def __init__(self) -> None:
        super().__init__()
