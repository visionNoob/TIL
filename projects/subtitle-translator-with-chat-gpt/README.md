# 영어 자막 한글 번역 

ChatGPT API로 영어로 된 `.srt` 자막 파일을 한글로 번역합니다. 

## 주요 기능
- `.srt` 파일을 읽고 자막 블록 단위로 분할
- ChatGPT API(`gpt-4o`)를 호출하여 영어 대사를 한글로 번역
- 순번, 시간 정보 등은 그대로 유지
- 번역된 결과를 `.srt` 파일로 저장

## RUN Samples
```python3
python translator.py samples/sample.srt
```
- 성공 시 `outputs/sample(ko).srt` 파일이 생성됩니다.