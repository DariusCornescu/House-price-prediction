import joblib
from pathlib import Path
from typing import Any
import os

# Global pipeline cache - loaded at startup
_pipeline_cache: dict[str, Any] = {}

def load_pipeline(pipeline_path: str = "final_project/ml_models/complete_pipeline.joblib"):
    # Return from cache if already loaded
    if pipeline_path in _pipeline_cache:
        return _pipeline_cache[pipeline_path]
    
    # Load from disk - handle relative paths from project root
    path = Path(pipeline_path)
    
    # If path doesn't exist, try from project root
    if not path.exists():
        # Get the project root (2 levels up from backend directory)
        backend_dir = Path(__file__).parent
        project_root = backend_dir.parent.parent
        path = project_root / pipeline_path
    
    if not path.exists():
        raise FileNotFoundError(f"Pipeline not found: {path}")
    
    pipeline = joblib.load(path)
    
    # Cache it
    _pipeline_cache[pipeline_path] = pipeline
    print(f"Loaded complete pipeline from {path}")
    
    return pipeline


def get_pipeline(): return load_pipeline()

def preload_pipeline():

    try:
        load_pipeline()
        print(" Pipeline preloaded successfully")
    except FileNotFoundError as e:
        print(f" Failed to preload pipeline: {e}")
        raise