class Solver(BaseClass):
    slurm_parameters = {
      'slurm_time': '02:00:00',
    }
    parameters = {
      "slurm_gres": ["gpu:1", "gpu:2"],
      ...
    }