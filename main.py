from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    data_ingestion = DataIngestionTrainingPipeline()
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 