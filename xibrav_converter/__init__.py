import requests

class XibravConverter:
    def __init__(self, base_url="http://xibrav.duckdns.org/convert"):
        self.base_url = base_url
        self.supported_formats = {"mp3", "mp4"}

    def convert(self, video_id: str, fmt: str = "mp4") -> dict:
        if fmt not in self.supported_formats:
            return {"error": f"Unsupported format: {fmt}. Supported formats: {', '.join(self.supported_formats)}"}
        params = {
            "id": video_id,
            "format": fmt
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
