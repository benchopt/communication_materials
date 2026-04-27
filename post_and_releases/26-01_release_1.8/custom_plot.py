from benchopt import BasePlot

class Plot(BasePlot):
    name = "My Custom Plot"
    type = "scatter"
    options = {
        "dataset": ...,
        "p": [1, 2],
    }
    def plot(self, df, dataset, p):
        # ... process df ...
        return plot_data

    def get_metadata(self, df, dataset, objective, p):
        return {
            "title": f"Plot for {dataset}",
            "xlabel": "X Label",
            "ylabel": "Y Label",
        }
