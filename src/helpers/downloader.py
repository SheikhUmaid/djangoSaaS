import requests
from pathlib import Path




def download_to_local(url: str, outpath:Path, parent_mkdir:bool=True) -> bool:
    if not isinstance(outpath, Path):
        raise ValueError(f"valid path is required")
    if parent_mkdir:
        outpath.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        outpath.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print("failed to download{}: {}".format(url, e))
        return false