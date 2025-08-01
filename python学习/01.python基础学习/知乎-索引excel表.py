import pandas as pd
from pathlib import Path


def create_file_by_xlsx(suffix: str):
    df = pd.read_excel("002.xlsx", header=None)
    names = df[0].values

    pokes = Path(__file__).parent / "pokes"
    pokes.mkdir(exist_ok=True)

    for n in names:
        f = pokes / f"{n}.{suffix}"
        f.touch()


create_file_by_xlsx("mp4")