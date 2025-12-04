import os
import requests
from datetime import datetime, date
from typing import List, Tuple, Optional

class BanxicoClient:
    BASE_URL = "https://www.banxico.org.mx/SieAPIRest/service/v1"
    SERIES_TIPO_CAMBIO = "SF60653"

    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv("BANXICO_TOKEN") or \
                     "20c0d154ab39c1a0d8d31bbc6411a6649acf12b7585a3a2d8bbbd100ff7a81b6"

        if not self.token:
            raise RuntimeError("No Banxico token provided.")

    def _get(self, path: str) -> dict:
        url = f"{self.BASE_URL}/{path}"
        headers = {"Bmx-Token": self.token}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def get_series_range(self, series_id: str, start: date, end: date) -> List[Tuple[date, float]]:
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
        path = f"series/{series_id}/datos/{start_str}/{end_str}"
        data = self._get(path)

        series = data["bmx"]["series"][0]["datos"]
        result = []
        for item in series:
            raw = item["dato"]
            if raw == "N/E":
                continue
            d = datetime.strptime(item["fecha"], "%d/%m/%Y").date()
            v = float(raw)
            result.append((d, v))

        result.sort(key=lambda x: x[0])
        return result

    def get_usd_mxn_range(self, start: date, end: date):
        return self.get_series_range(self.SERIES_TIPO_CAMBIO, start, end)
