import io
import json

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

engine = SnipsNLUEngine(config=CONFIG_EN)

with io.open("new_dataset.json") as f:
     dataset = json.load(f)

engine.fit(dataset)
