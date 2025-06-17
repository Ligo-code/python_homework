import pandas as pd

class DFPlus(pd.DataFrame):

    # Ensures operations return DFPlus, not plain DataFrame
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    # --- new helper method ---
    def print_with_headers(self, block_size: int = 10):
        total_rows = len(self)
        for start in range(0, total_rows, block_size):
            end = start + block_size
            print("\n" + "-" * 60)
            print(self.columns.to_list())      # headers once per block
            print(self.iloc[start:end])


if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()