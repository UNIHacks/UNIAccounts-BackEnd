from typing import Dict

import config.base as CONFIG
from config.database import get_session
from models import ServicesModel


class ServicesService:
    def get_services(self) -> Dict[str, "ServicesModel"]:
        if not CONFIG.API_KEYS:
            session = get_session()
            services = session.query(ServicesModel).all()
            session.close()
            CONFIG.API_KEYS = {service.name: service for service in services}
        return CONFIG.API_KEYS
