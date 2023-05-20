
from src.pipe.prediction_pipeline import LanguageData
from src.entity.config_entity import PredictionPipelineConfig
from src.pipe.prediction_pipeline import LanguageData, SinglePrediction

input_sounds_path = r"prediction_artifacts\user_inputs\inputSound.wav"

predictor = SinglePrediction(PredictionPipelineConfig())

signal = LanguageData().load_data(input_sounds_path)
signal.unsqueeze_(0)
result = predictor.predict_language(input_signal=signal)
print(result)