from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity import config_entity 

if __name__ =="__main__":
     try:
          traing_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = config_entity.DataIngestionConfig(traing_pipeline_config=traing_pipeline_config)
          print(data_ingestion_config.to_dict())
     except Exception as e:
          print(e)
