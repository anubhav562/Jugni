"""
This file is responsible for training and saving the SnipsNLU Engine
"""

import json

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

engine = SnipsNLUEngine(config=CONFIG_EN)

with open("dataset.json") as f:
    dataset = json.load(f)

engine.fit(dataset)
engine.persist("persisted_engine")
