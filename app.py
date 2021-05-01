
from src.models.summoner import Summoner
import json


print("Starting")
dd = Summoner.init_by_name("DreamDog")
dd.get_match_history()
