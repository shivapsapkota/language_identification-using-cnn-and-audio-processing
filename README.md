# Language Identification using CNN PyTorch

#### Language and Libraries

<p>
<a><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="python"/></a>
<a><img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas"/></a>
<a><img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white" alt="numpy"/></a>
<a><img src="https://img.shields.io/badge/PyAudio-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="pyaudio"/></a>
<a><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="pytorch"/></a>
<a><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)" alt="docker"/></a>
<a><img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white" alt="gcp"/></a>
<a><img src="https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white" alt="actions"/></a>
<a><img src="https://img.shields.io/badge/AWS_S3-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"/></a>
</p>


## Problem statement
The goal of this project is to develop a Language Identification system that can accurately identify the spoken language from an audio file. The system should be able to process audio files in various formats, such as .mp3, and predict the language with high accuracy.

## Solution Proposed
To address this problem, we proposed a solution that utilizes the Pytorch framework for machine learning and the Torchaudio library for audio processing. The audio is first converted to a Mel Spectrogram, which is then fed into an image classification model. We created a custom Language Identification network using Pytorch, which is trained on a dataset of audio samples in various languages.

The system was tested on a set of audio samples and was able to achieve high accuracy in identifying the spoken language. We also developed an API that takes in an audio file in the form of an .mp3 file and returns the predicted language. Finally, the application was containerized using Docker and deployed on the AWS cloud for easy access and scalability.

## Dataset Used

This is a dataset of audio samples of 4 different Nepali languages. Each audio sample is of 10 seconds duration. This dataset was created using VoxLingua107 and regional videos available on YouTube.

This is constrained to 5 Regional Nepali Languages only but could be extended.

Languages present in the dataset -
Nepali, Hindi, Snaskrit, Newari, Maithali.

## Points to Improve:

- Incorporation of more diverse dataset of audio samples from different languages and accents to improve the accuracy of the model.

- Experimentation with different audio processing techniques to see if it improves the performance of the model.

- Integration of the system with a user-friendly interface for easier access and usage for non-technical users.

- Further optimization of the model to reduce the latency of the API and improve the overall efficiency of the system.

- Incorporation of additional features such as speaker identification and text transcription to make the system more versatile.

- Evaluate the performance of the model with different languages and accents, and if needed retrain the model with more diverse dataset.

## How to run?

### Step 1: Clone the repository
```bash
git clone "https://github.com/shivapsapkota/language_identification-using-cnn-and-audio-processing.git" repository
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -p env python=3.10 -y
```

```bash
conda activate env/
```
Alternatively you can also use venv

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 5 - Run the application server
```bash
python app.py
```

### Step 6. Train application
```bash
http://localhost:8080/train
```

### Step 7. Prediction application
```bash
http://localhost:8080
```

👨‍💻 Tech Stack Used
1. Python
2. Flask
3. Pytorch
4. Docker
5. CNN

🌐 Infrastructure Required.
1. Local Computer

## `src` is the main package folder which contains 

**Artifact** : Stores all artifacts created from running the application

**Components** : Contains all components of Machine Learning Project
- DataIngestion
- DataTransformation
- ModelTrainer
- ModelEvaluation
- ModelPusher

**Custom Logger and Exceptions** are used in the project for better debugging purposes.


## Conclusion

This Language Identification system can be used in a variety of applications such as:

- Speech-to-text transcription: The system can be used to automatically identify the language of the audio input and transcribe it to text in the corresponding language, improving the accuracy of the transcription.
- Contact centers: The system can be integrated into contact center systems to automatically identify the language spoken by the customer and route the call to an appropriate agent.
- Language identification in the field of speech recognition: The system can be used to identify the spoken language of the speaker, thus allowing speech recognition systems to adapt to the speaker's accent and language.
- Audio/Video Translation: The system can be used to identify the language of the audio/video, then use the language to translate the audio/video in real-time.


=====================================================================
