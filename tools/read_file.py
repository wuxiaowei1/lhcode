import yaml
from pathlib import Path
from tools import extractor
class ReadFile:
    config_dict = None
    config_path = f"{str(Path(__file__).parent.parent)}/config/config.yaml"

    @classmethod
    def get_config_dict(cls):
        if cls.config_dict is None:
            with open(cls.config_path, "r", encoding="utf-8") as file:
                cls.config_dict = yaml.load(file.read(), Loader=yaml.FullLoader)
        return cls.config_dict
    @classmethod
    def read_config(cls, expr:str = "."):
        return extractor(cls.get_config_dict(), expr)