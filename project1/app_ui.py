import gradio as gr
from chat_assistantAPI import chat_fn
from config_flight import js, css 
from speech_recognition import update_chat_with_transcription


# Run main chat user interface

with gr.Blocks(js=js,theme=gr.themes.Soft(), css=css) as demo:
  chat_history = gr.State([])
  with gr.Group():
      chatbot=gr.Chatbot([],elem_id="chatbot", bubble_full_width=False)
  with gr.Row():
      chatbox = gr.Textbox(placeholder="여기에 입력하세요... 엔터치면 전송⏎")
      # 챗봇 입력이 있을 때 응답 생성
      chatbox.submit(fn=chat_fn, inputs=[chatbox, chat_history], outputs=chat_history)
      # 대화 기록을 챗봇에 연결
      chat_history.change(fn=lambda history: history, inputs=chat_history, outputs=chatbot)



  with gr.Row():

      with gr.Column(scale=0.5):
        audio_input = gr.Audio(sources="microphone", label="음성 입력🎙️")
      with gr.Column(scale=0.5):
        text_output = gr.Textbox(label="내가 한 말", interactive=True,
                                container=True)  # 사용자가 수정할 수 있도록 설정
              # 변환된 텍스트가 확인되면 챗봇에 입력
        submit_button = gr.Button("말 전달하기")  # 버튼 추가
        submit_button.click(fn=lambda text, chat_history: chat_fn(text, chat_history), inputs=[text_output, chat_history], outputs=chat_history)

      # 음성 입력이 있을 때 텍스트 출력
      audio_input.change(fn=update_chat_with_transcription, inputs=audio_input, outputs=text_output)



demo.queue()
demo.launch(share=True)