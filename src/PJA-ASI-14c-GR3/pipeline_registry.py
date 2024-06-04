from typing import Dict

from kedro.pipeline import Pipeline
from .pipelines.data_processing import create_pipeline as create_data_processing_pipeline
from .pipelines.machine_learning import create_pipeline as create_machine_learning_pipeline
from .pipelines.auto_ml import create_pipeline as create_auto_ml_pipeline

def register_pipelines() -> Dict[str, Pipeline]:

  data_processing_pipeline = create_data_processing_pipeline()
  machine_learning_pipeline = create_machine_learning_pipeline()
  auto_ml_pipeline = create_auto_ml_pipeline()

  return {
      "data_processing": data_processing_pipeline,
      "machine_learning": machine_learning_pipeline,
      "auto_ml": auto_ml_pipeline,
      "__default__": data_processing_pipeline + machine_learning_pipeline + auto_ml_pipeline
  }
