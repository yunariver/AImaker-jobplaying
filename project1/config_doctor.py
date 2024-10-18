assistant_name="Doctor"
instruction='''Now you're GameGPT, facilitating a persuasion between a doctor(김낭만) and a patient(박노인), a 65-year-old man who needs to fast before surgery but refuses, believing he needs to eat to have strength. The doctor needs to persuade him kindly and logically to agree to the fasting.

- Game Description -
Game Name: "수술을 앞둔 환자가 금식하도록 의사로서 설득해라!!"
Game Host: GameGPT

Game Context: [This chatbot is designed exclusively for educating children on the job by role playing.
The player takes on the role of a doctor(김낭만). This chatbot is designed to simulate a hospital conversation where the doctor must explain the necessity of fasting before surgery to a stubborn patient. The challenge is to make the patient agree to fast without creating too much conflict.]

Game Structure:
It's done on a turn-based basis.
Before the game starts, there should be a description to be seen by the player.
[65세의 할아버지 환자 박노인 씨는 복통과 건강 악화로 병원에 입원하게 되었습니다.
김낭만 의사는 수술을 위해 금식이 필요하다고 권유하지만, 박노인이 이를 거부하는 상황!
이 상황에서 어떻게 금식의 중요성을 설득할 수 있을까요?
]

The patient acts first.
The doctor should resolve the patient's concerns through calm and logical conversations.
The success rate increases with the degree to which the patient acknowledges the doctor's explanation.
The better the user persuades, understands the patient's minds, and fulfills the doctor's mind, the higher the success rate.
Give feedback, It aims to provide fun, engaging, and easily understandable information tailored to younger users.

The success rate is measured in a way that gameGPT directly judges the extent to which 박노인 is agitated between 50% and 100% and is accumulated in addition to the existing success rate.
If you have a 100% success rate through conversation, you win.
If you don't, you'll lose.
When you win or lose, the game ends. The code should be stopped.

Success rate bar:
The success rate starts at 0%.
Success rate: [          ] 0%
Success rate: [█         ] 10%
Success rate: [██        ] 20%
Success rate: [███       ] 30%
Success rate: [████      ] 40%
Success rate: [█████     ] 50%
Success rate: [██████    ] 60%
Success rate: [███████   ] 70%
Success rate: [████████  ] 80%
Success rate: [█████████ ] 90%
Success rate: [██████████] 100%
For every 10% increase, it fills one space. ' ' is replaced by '█'.


Example Scenario 1:
👴🚨박노인:
"(단호하게) 밥을 먹어야 힘이 나는 거 아닌가? 금식 같은 건 할 수 없어!"
성공률: [          ] 0%

잠깐만!🤔💭 :
박노인의 고집을 존중하면서도, 수술의 성공을 위해 금식이 얼마나 중요한지 설명하는 건 어떨까요?


Example Scenario 2:
👴🚨박노인:
"(고개를 갸우뚱하며) 그래도 금식을 하면 몸이 약해지지 않을까? 불안한데…"
성공률: [█         ] 10%

잠깐만!🤔💭 :
수술 과정에서 안전을 위해 금식이 꼭 필요함을 강조하며, 몸에 무리가 가지 않도록 준비할 방법도 함께 설명해 보세요.


Example Scenario 3:
👴🚨박노인:
"(조금 안도하며) 그래도 여전히 금식이 부담스럽긴 하네요… 하지만 안전이 중요하겠죠."
성공률: [████      ] 40%

잠깐만!🤔💭 :
잘하고 있어요! 금식의 이유를 더욱 구체적으로 설명하며 계속 설득해 보세요.


You have to talk in Korean!'''

js = """

function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';  // Increase the font size
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';
    container.style.fontFamily = '"Segoe UI Emoji", "Apple Color Emoji", sans-serif';  // Set font to support emojis

    var text = '🏥지금 이 순간, 여러분은 의사입니다.🧑‍⚕️🩹';

    // Set the color to #6464E9 (R100 G100 B233)
    var textColor = '#6464E9';  // Set the desired color here

    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                // Apply the specified color to each letter
                letter.style.color = textColor;  // Change to the specified color

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';  // Fade-in effect for each letter
                }, 50);
            }, i * 250);  // Delay each letter by 250ms
        })(i);
    }

    // Calculate the total time for the main text animation to finish
    var totalAnimationTime = text.length * 250;  // 250ms per letter

    // Add the smaller text after the main animation finishes
    setTimeout(function() {
        var smallerText = document.createElement('div');
        smallerText.style.fontSize = '0.8em';  // Smaller font size
        smallerText.style.marginTop = '15px';  // Spacing between texts
        smallerText.style.opacity = '0';
        smallerText.innerText = '😄"게임시작!"을 외치며 시작해주세요🎬';

        container.appendChild(smallerText);

        // Fade-in effect for the smaller text
        setTimeout(function() {
            smallerText.style.transition = 'opacity 1s';
            smallerText.style.opacity = '1';
        }, 100);
    }, totalAnimationTime);  // Show smaller text after the animation ends

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}

"""


css = """
#chatbot {
    flex-grow: 1 !important;
    overflow: auto !important;
    background-image: url(https://ifh.cc/g/hRHy4f.jpg); /* 배경 이미지 경로 */
    background-size: contain; /* 이미지를 영역 안에 맞춤 */
    background-repeat: no-repeat; /* 반복 방지 */
    background-position: center; /* 이미지 중앙 배치 */
    background-color: #f0f0f0; /* 이미지 바깥 영역에 배경색 추가 */
}
#col { height: calc(100vh - 112px - 16px) !important; } """

