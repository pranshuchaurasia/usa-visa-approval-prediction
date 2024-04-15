import os
from pathlib import Path

def create_project_structure():
    project_name = "us_visa"
    base_path = Path(os.getcwd())  # Get the current working directory
    project_path = base_path / project_name

    # List of files and directories to be created
    list_of_files = [
        project_path / "__init__.py",
        project_path / "components" / "__init__.py",
        project_path / "components" / "data_ingestion.py",
        project_path / "components" / "data_validation.py",
        project_path / "components" / "data_transformation.py",
        project_path / "components" / "model_trainer.py",
        project_path / "components" / "model_evaluation.py",
        project_path / "components" / "model_pusher.py",
        project_path / "configuration" / "__init__.py",
        project_path / "constant" / "__init__.py",
        project_path / "entity" / "__init__.py",
        project_path / "entity" / "config_entity.py",
        project_path / "entity" / "artifact_entity.py",
        project_path / "logger" / "__init__.py",
        project_path / "exception" / "__init__.py",
        project_path / "pipeline" / "__init__.py",
        project_path / "pipeline" / "prediction_pipeline.py",
        project_path / "utils" / "__init__.py",
        project_path / "pipeline" / "main_utils.py",
        base_path / "app.py",
        base_path / "requirements.txt",
        base_path / "Dockerfile",
        base_path / ".dockerignore",
        base_path / "demo.py",
        base_path / "setup.py",
        project_path / "config" / "model.yaml",
        project_path / "config" / "schema.yaml",
    ]

    for path in list_of_files:
        if not path.parent.exists():
            print(f"Creating directory: {path.parent}")
            path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists():
            print(f"Creating file: {path}")
            with open(path, 'w') as file:
                pass
        else:
            print(f"File already exists: {path}")

# Run the function
create_project_structure()
