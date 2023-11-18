from .config import ALLOW_EXTERNAL_APPS
from typing import Optional
from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager


async def get_media_info() -> Optional[dict]:
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
        _app = current_session.source_app_user_model_id
        app = "Yandex.Music" if "Yandex.Music" in _app else _app

        if ("Yandex.Music" not in _app) and (not ALLOW_EXTERNAL_APPS):
            print("cont")
            return

        info = await current_session.try_get_media_properties_async()

        info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}

        info_dict['genres'] = list(info_dict['genres'])

        info_dict["app"] = app

        return info_dict
    
    return None