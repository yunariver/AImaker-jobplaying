from transformers import pipeline
import numpy as np


# 음성 인식 모델 로드
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base", generate_kwargs={"language": "korean"})


def transcribe(audio):
    sr, y = audio

    # 스테레오를 모노로 변환
    if y.ndim > 1:
        y = y.mean(axis=1)

    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    return transcriber({"sampling_rate": sr, "raw": y})["text"]


# 음성 인식 인터페이스
def update_chat_with_transcription(audio):
    transcribed_text = transcribe(audio)
    return transcribed_text  # 변환된 텍스트를 반환, none을 반환하여 오디오 입력 비우기


