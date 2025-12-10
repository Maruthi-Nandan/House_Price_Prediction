import pandas as pd

from src.handle_missing_values import (
    DropMissingValueStrategy,
    FillMissingValuesStrategy,
    MissingValueHandler,
)
from zenml import step

@step
def handle_missing_values_step(df: pd.DataFrame, strategy: str = "mean"):
    """Handles missing values using MissingValueHandler and the specified strategy."""
    
    if strategy == "drop":
        handler = MissingValueHandler(DropMissingValueStrategy(axis=0))
    elif strategy in ["mean", "median", "mode", "constant"]:
        handler = MissingValueHandler(FillMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling strategy: {strategy}")
    
    cleaned_df = handler.handle_missing_values(df)
    return cleaned_df
    