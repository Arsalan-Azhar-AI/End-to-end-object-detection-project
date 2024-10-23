import os,sys,zipfile,shutil
import yaml
from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.entity.artifacts_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config


    
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            with zipfile.ZipFile('sign%20language%20dataset.zip', 'r') as zip_ref:
                zip_ref.extractall()
            os.remove('sign%20language%20dataset.zip')
            
            with open("sign language dataset/data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)


            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)
            dataset_path = os.path.join("../../sign language dataset", "data.yaml")

            os.system(f"python yolov5/train.py --img 640 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data '../../sign language dataset/data.yaml' --cfg ./yolov5/models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache")
            shutil.copy('yolov5/runs/train/yolov5s_results/weights/best.pt', 'yolov5/')
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            shutil.copy('yolov5/runs/train/yolov5s_results/weights/best.pt', f"{self.model_trainer_config.model_trainer_dir}/")
            '''
            os.remove('sign language dataset.zip')
        
            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            '''
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise SignException(e, sys)


'''
python 'yolov5/train.py' --img 640 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data 'sign language dataset/data.yaml' --cfg 'yolov5/models/custom_yolov5s.yaml' --weights {self.model_trainer_config.weight_name} --name 'yolov5s_results' --cache


python yolov5/train.py --img 640 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data 'sign language dataset/data.yaml' --cfg ./yolov5/models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache


python 'yolov5/train.py' --img 640 --batch 16 --epochs 1 --data 'sign language dataset/data.yaml' --cfg 'yolov5/models/custom_yolov5s.yaml' --weights --name 'yolov5s_results' --cache
'''