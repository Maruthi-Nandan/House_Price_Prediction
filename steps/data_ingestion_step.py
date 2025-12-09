import pandas as pd
from src.ingest_data import DataIngestFactory
from zenml import step

@step
def data_ingestion_step(file_path:str) -> pd.DataFrame:
    """Ingest data from a ZIP file using the appropriate DataIngestor."""
    file_extension = ".zip" # Since we're dealing with ZIP files, this is hardcoded
    
    data_ingestor = DataIngestFactory.get_data_ingestor(file_extension)
    
    df = data_ingestor.ingest(file_path)
    return df


    