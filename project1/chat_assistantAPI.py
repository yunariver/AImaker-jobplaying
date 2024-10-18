import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import time
from config_flight import instruction, assistant_name


load_dotenv()  # .env 파일을 로드하여 환경 변수를 불러옴
api_key = os.environ.get("OPENAI_API_KEY")


turn_counter = 0
success_rate = 0
max_turns = 11

client = OpenAI(api_key =api_key)
deployment_name = 'gpt-4o-mini'


assistant = client.beta.assistants.create(
  name= assistant_name,
  instructions=instruction,
  model=deployment_name)

# Create Thread
thread = client.beta.threads.create()


# Get response from AI
"""
Note with Assistents API session state is stored on server, there is no need to construct whole sequence of message history
"""
def chat_fn(message, chat_history):
    global turn_counter, success_rate

    if turn_counter >= max_turns:
        return "[10턴 도달!] 😂😂😂 게임이 끝났습니다!😇 10번의 시도 안에 성공해보세요!."

    if success_rate >= 100:
        return "🎉성공! 🥳 역할을 잘 해내어 미션을 완료했어요!🎶"

    # Create message based on user input
    next_message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )

    # Create run
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    # Retrieve the status of the run
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    # Wait for thread status to be complete or requires_action (waiting for function execution)
    while run.status !="completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run.status == "requires_action":
            print(">> Calling get_catalog function")

         

    # Get latest message
    thread_message = client.beta.threads.messages.list(thread_id=thread.id, order="desc",limit=1)
    last_thread_message = thread_message.data[0].content[0].text.value
    turn_counter += 1
    # print(thread_message.model_dump_json(indent=2))
    chat_history.append((message, last_thread_message))
    return chat_history

