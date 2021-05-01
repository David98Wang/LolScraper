import json
from src.helper import get_request, get_request_v5


class Summoner(object):
    def __init__(self, id: str, accountId: str, puuid: str, name: str, profileIconId: int, revisionDate: int, summonerLevel: int) -> None:
        super().__init__()
        self.id = id
        self.accountId = accountId
        self.puuid = puuid
        self.name = name
        self.profileIconId = profileIconId
        self.revisionDate = revisionDate
        self.summonerLevel = summonerLevel

    def get_match_history(self, start: int = 0, end: int = 20):
        puuid = self.puuid
        print(puuid)
        r = get_request_v5("/lol/match/v5/matches/by-puuid/{}/ids".format(puuid),
                           params={"start": start, "end": end})
        match_id_list = json.loads(r.content)
        return match_id_list

    def init_by_name(summoner_name: str):
        r = get_request(
            "/lol/summoner/v4/summoners/by-name/{}".format(summoner_name))
        content = r.content
        summoner_dict = json.loads(content)
        summoner = Summoner(**summoner_dict)
        return summoner
