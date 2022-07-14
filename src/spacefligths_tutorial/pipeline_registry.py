"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from spacefligths_tutorial.pipelines import data_preprocessing as dp
from spacefligths_tutorial.pipelines import model as mdl


def register_pipelines() -> Dict[str, Pipeline]:

    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    data_preprocessing_pipeline = dp.create_pipeline()
    model_pipeline = mdl.create_pipeline()

    return {"__default__": data_preprocessing_pipeline + model_pipeline, # kedro run --> project pipeline
            'dp': data_preprocessing_pipeline,
            'mdl': model_pipeline
    }
