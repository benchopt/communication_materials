from benchopt import BaseObjective


class Objective(BaseObjective):
    name = "Accuracy"
    sampling_strategy = "run_once"
