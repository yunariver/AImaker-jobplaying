

# Job+Role Playing! using openAI assistant api

This project is a role-playing game designed for teenagers to explore different careers. Users can take on roles such as a doctor, teacher, or composer, and interact with an AI assistant that responds flexibly to their actions. Through various simulations, teenagers can solve problems and gain a deeper understanding of different professions. The system includes conversation handling, speech recognition, and a user-friendly interface.


이 프로젝트는 청소년을 위한 직업 체험 롤플레잉 게임입니다. 사용자는 의사, 교사, 작곡가 등 다양한 직업을 맡아보며, AI 어시스턴트가 유연하게 대응하여 실감 나는 직업 경험을 제공합니다. 이를 통해 청소년들은 다양한 시뮬레이션에서 문제를 해결하며 각 직업에 대해 깊이 이해할 수 있습니다. 이 시스템은 대화 처리, 음성 인식, 그리고 사용자 친화적인 인터페이스를 갖추고 있습니다.




```markdown
## Installation / 설치 방법

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd AImaker/project1
   ```

3. Set up and activate the virtual environment:
   가상 환경을 설정하고 활성화합니다:
   ```bash
   python3 -m venv test1
   source test1/bin/activate  # On macOS/Linux
   ```

4. Install the required packages:
   필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run / 실행 방법

1. **Activate the virtual environment** (if not already active):
   가상 환경을 활성화합니다 (이미 활성화되어 있지 않은 경우):
   ```bash
   source test1/bin/activate
   ```

2. **Launch the main application**:
   메인 애플리케이션을 실행합니다:
   ```bash
   python app_ui.py
   ```

This will start the Gradio interface, where you can interact with the AI assistants.
이 명령을 실행하면 Gradio 인터페이스가 열리며, AI 어시스턴트들과 상호작용할 수 있습니다.

---

## Files Overview / 파일 개요

- **app_ui.py**: Main file for the Gradio-based user interface.
  Gradio 기반 사용자 인터페이스의 메인 파일입니다.
  
- **chat_assistantAPI.py**: Handles conversation logic and interaction with the OpenAI API.
  대화 로직과 OpenAI API와의 상호작용을 처리하는 파일입니다.
  
- **config_*.py**: Configuration files for various assistant roles (e.g., doctor, teacher, lawyer).
  다양한 어시스턴트 역할(의사, 교사, 변호사 등)을 위한 설정 파일들입니다.
  
- **speech_recognition.py**: Manages speech-to-text functionality using models like Whisper.
  Whisper 모델을 사용한 음성 인식 기능을 처리하는 파일입니다.
  
- **requirements.txt**: Lists the required Python packages.
  필요한 Python 패키지 목록을 담은 파일입니다.

