from app.config import SETTINGS


class PlayerState:
    """
    SINGLETON

    Maintain player's nickname and player_id for turns and connection checks
    """

    def __init__(self):
        self.nickname = SETTINGS.player_nickname
        self.player_id = ""

    def set_player_id(self, player_id: str):
        self.player_id = player_id

    def get_player_id(self) -> str:
        return self.player_id

    def get_player_nickname(self) -> str:
        return self.nickname


PLAYER_STATE = PlayerState()
