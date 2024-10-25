
# 청소년을 위한 직업 체험 롤플레잉 게임🎮🧑‍💻🧑‍💻
Job+Role Playing! using openAI assistant API, whisper, gradio.

<p align="center">
  <img src="https://github.com/user-attachments/assets/0728ead3-2cda-4164-9afe-d502c944de80" alt="무제3">
</p>
게임 완료 시


https://github.com/user-attachments/assets/991b4ebd-95d3-4fff-95e3-8e3cbc532ded


(2024.10.5 ~2024.10.26 )
# 매뉴얼
'''markdown


#코랩 사용법 
https://drive.google.com/drive/u/1/folders/1X51Jkzlh0luXZ8uzTqaInqTT773QgvPP 

- 실행 : 코랩 상단탭에 [런타임-> 모두 실행]을 진행하면 하단에 링크가  Running on public URL이 뜹니다.

- 주의점 :  72시간 동안 public url을 통하여 연결 가능하지만, Gradio URL은 Colab에서 실행 중인 세션과 연결되어 있습니다. 따라서 런타임을 해제하거나 노트북을 종료하면 해당 URL은 더 이상 유효하지 않게 됩니다. 

- 해결 방법 : 런타임 유지- Colab에서 작업을 수행하는 동안 런타임을 해제하지 않도록 하세요. 세션이 계속 활성화되어 있어야 URL이 유지됩니다.  따라서 interface 에러가 났을 때는 다시 [런타임-> 모두 실행]을 해주시면 됩니다. 

- (참고) 이모지에 에러가 난 경우, 저는 다시 실행했을 때, 해결이 되었습니다. 


#인터페이스 사용법
https://github.com/yunariver/AImaker-jobplaying/blob/main/README.md 
영상과 gif로 보면 쉽게 이해될거에요!

[가이드]
- ctrl(cmd)+shift+F : 전체화면
- 처음 시작은 “게임시작”을 입력하게 해주세요

[문자 입력]
- 텍스트박스에 타이핑 후 엔터를 누르면 전송이 됩니다. 잠시 대기(10초 이내)가 필요합니다.
- 다시 텍스트박스에 있는 글자를 수동으로 지워야합니다. 
[음성입력]
- 마이크 입력(원) 후 중지 버튼(네모) 누르면 자동으로 ‘내가 한 말’ 칸에 텍스트로 입력됩니다. 
- “말 전달하기”버튼을 눌러 챗봇으로 전송합니다.
- 다시 입력 시 음성 입력 상단의 “X” 버튼을 누르고 다시 반복합니다. 

[오류]
- 유저의 말을 할 때가 있는데, 그러면 다시 상대를 지칭해야함! 
    - 예) 시스템이 환자의 입장에서 말을 해야하는데 의사 입장에 말을 할 때 -> ‘환자분, ~~~” 지칭을 명확하게 해야함. 
- 
[완료 시]
- 챗봇 우측 상단의 ‘X”를 누르면 다시 시작됩니다. 



'''



## 🦹‍ Team
**SEOUL AI MAKER** : 시립서울청소년센터 자치단으로, 인공지능을 활용하여 청소년을 위한 서비스와 교육을 기획하는 단체입니다. 
AI 기술을 활용한 창의적인 문제 해결과 청소년들에게 긍정적인 변화를 이끌어내기 위해 함께 노력하고 있습니다.
A self-governing group of the Seoul Youth Center, this organization plans services and education for young people using artificial intelligence. We strive together to creatively solve problems using AI technology and to bring about positive changes for youth.

## 👶 팀원

<table border="" cellspacing="0" cellpadding="0" max-width="2000px">
    <tr width="100%">
        <td align="center"><a href="#">최유정</a></td>
        <td align="center"><a href="https://github.com/yunariver">강윤하</a></td>
        <td align="center"><a href="https://github.com/suuuujinnnn">박수진</a></td>
        <td align="center"><a href="#">박윤서</a></td>
        <td align="center"><a href="#">이다영</a></td>
    </tr>
    <tr width="100%">
        <td align="center">
          <a href="#">
            🥑 <!-- Replace with the actual image URL -->
          </a>
        </td>
        <td align="center">
          <a href="https://github.com/yunariver">
            🍎
          </a>
        </td>
        <td align="center">
          <a href="https://github.com/suuuujinnnn">
            🍊
          </a>
        </td>
        <td align="center">
          <a href="#">
            🍋 <!-- Replace with the actual image URL -->
          </a>
        </td>
        <td align="center">
          <a href="#">
            🍉 <!-- Replace with the actual image URL -->
          </a>
        </td>
    </tr>
    <tr width="100%">
      <td align="center">
        <small>
        담당 선생님💛
        </small>
      </td>
      <td align="center">
        <small>
        대화 처리 시스템 구축,<br>
        UI 설계,<br>
        게임 기획 및 로직 구현,<br>
        프로그램 구체화 및 문서화
        </small>
      </td>
      <td align="center">
        <small>
        직업별 코드 최적화,<br>
        안정성 테스트,<br>
        교육 자료 및 매뉴얼 제작,<br>
        프로그램 구체화 및 문서화
        </small>
      </td>
      <td align="center">
        <small>
        게임 로직 구현,<br>
        성공률 밸런스 테스트,<br>
        팜플렛 디자인,<br>
        프롬프트 엔지니어링
        </small>
      </td>
      <td align="center">
        <small>
        프롬프트 엔지니어링,<br>
        시뮬레이션 테스트 및 최적화
        </small>
      </td>
   </tr>
</table>

<table border="" cellspacing="0" cellpadding="0" max-width="2000px">
    <tr width="100%">
        <td align="center"><a href="#">강민주</a></td>
        <td align="center"><a href="#">김강민</a></td>
        <td align="center"><a href="#">김영우</a></td>
        <td align="center"><a href="#">박재영</a></td>
        <td align="center"><a href="#">송현수</a></td>
    </tr>
    <tr width="100%">
        <td align="center">
          <a href="#">
            🍑 <!-- Replace with the actual image URL -->
          </a>
        </td>
        <td align="center">
          <a href="#">
            🫐 <!-- Replace with the actual image URL -->
          </a>
        </td>
        <td align="center">
          <a href="#">
            🍓 <!-- Replace with the actual image URL -->
          </a>
        </td>
        <td align="center">
          <a href="#">
            🥝 <!-- Replace with the actual image URL -->
          </a>
        </td>
        <td align="center">
          <a href="#">
            🥥 <!-- Replace with the actual image URL -->
          </a>
        </td>
    </tr>
    <tr width="100%">
      <td align="center">
        <small>
        팜플렛 기획 및 디자인,<br>
        부스 디자인
        </small>
      </td>
      <td align="center">
        <small>
        프로그램 기획서,<br>
        예산 관리
        </small>
      </td>
      <td align="center">
        <small>
        직업별 페르소나 설정 ,<br>
          스토리라인 구체화,<br>
        피드백 수집
        </small>
      </td>
      <td align="center">
        <small>
        포스터, 팜플렛 디자인,<br>
        예산 관리
        </small>
      </td>
      <td align="center">
        <small>
        포스터, 팻말, 현수막 디자인,<br>
        직업별 역할 문서화
        </small>
      </td>
   </tr>
</table>





이 프로젝트는 청소년을 위한 직업 체험 롤플레잉 게임입니다! 
사용자는 의사, 교사, 작곡가 등 다양한 직업을 맡고, AI 어시스턴트가 유연하게 대응하여 실감 나는 직업 경험을 제공합니다.
성공률이 100%에 도달하면 사용자가 이기는 게임으로, 사용자가 직업을 깊이 이해하고, 직업 윤리에 맞게 행동할수록 성공률이 높아집니다!
다양한 시뮬레이션에서 문제를 해결하며 청소년들은 각 직업에 대해 깊이 이해할 수 있습니다. 


This project is a role-playing game designed for teenagers to explore different careers. Users can take on roles such as a doctor, teacher, or composer, and interact with an AI assistant that responds flexibly to their actions. Through various simulations, teenagers can solve problems and gain a deeper understanding of different professions. The system includes conversation handling, speech recognition, and a user-friendly interface.


## 주요 기능 : 직업 시뮬레이션 / 실시간 대화 / 음성 및 텍스트 입력 
## 기술 구성 요소
- Assistant API를 통한 대화 처리:사용자는 직업별 시뮬레이션 내에서 자연어로 질문을 하거나 지시를 내릴 수 있으며, AI 어시스턴트는 해당 직업에 맞는 적절한 대응을 제공합니다.
- Whisper 음성 인식을 활용한 사용자 입력 :  음성 입력을 텍스트로 변환하여 대화형 인터페이스에서 사용됩니다.
  지난 상반기 교육에서 초등학교 저학년 학생들이 타자치는 것에 미숙하다는 것을 확인하였고, 음성 인식 기술을 도입하였습니다. 
- gradio를 통한 사용자 친화적인 인터페이스
- 
Conversation processing through the Assistant API: Users can ask questions or give instructions in natural language within job simulations, and the AI assistant provides appropriate responses based on the profession. An interesting element of success rates is introduced, making it a game that distinguishes between success and failure.

User input utilizing Whisper voice recognition: Voice input is converted into text for use in a conversational interface. The reason for implementing voice recognition was that during training in the first half of the year, it was observed that younger elementary school students struggled with typing, leading to the adoption of voice recognition technology.

User-friendly interface through Gradio: We quickly created a solution using Gradio, which does not require a server. In the future, we plan to develop a complete web application using FastAPI and other technologies.







# 02. 시작가이드
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
  
## 기술 스택
AI 대화 모델: Assistant API (OpenAI GPT 등)
음성 인식: Whisper
사용자 인터페이스: Gradio
프레임워크: Python
