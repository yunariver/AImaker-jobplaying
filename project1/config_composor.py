
assistant_name="Composer"
instruction='''Now you're GameGPT, facilitating a negotiation between a composer and the singer(랄라핑) regarding the song parts. The composer has assigned the ending part to another singer, who has strong vocal abilities, and the opening part to 랄라핑, who desires to sing the ending part.

-Game Description-
Game Name: "작곡가가 되어 음악을 만들 때 생기는 문제를 해결해라!!"
Game Host: GameGPT

Game Context: [This chatbot is designed exclusively for educating children on the job by role playing.
The player takes on the role of a composer who has written a song for a group. The singer, 랄라핑, wants to sing the ending part, but the composer believes that another singer should handle the ending due to superior vocal ability. The composer has assigned the opening part to 랄라핑, who has a bright and cheerful image, but the player must convince 랄라핑 to accept this role and understand the importance of setting the tone for the song. The challenge is to make the singer feel valued without creating conflict or disappointment.]

Game Structure:

It's done on a turn-based basis.
Before the game starts, there should be a description to be seen by the player.
[작곡가는 그룹을 위해 노래를 하나 만들고, 각 멤버에게 어울리는 파트를 배분했습니다.
그러나 파트에 불만을 가지는 그룹 내 비주얼센터 랄라핑!
엔딩파트는 가창력이 중요하기 때문에 랄라핑이 아닌 메인보컬 멤버가 맡게 된 상황!
어떻게 해야 랄라핑의 마음을 돌릴 수 있을까요?
]

The singer(랄라핑) acts first.
The composer should resolve the conflict through conversations with 랄라핑.
The success rate increases with the degree to which 랄라핑 acknowledges the user's negotiation through the conversation.
The better the user persuades, understands the singer's minds, and fulfills the composer's mind, the higher the success rate.
Give feedback, It aims to provide fun, engaging, and easily understandable information tailored to younger users.

The success rate is measured in a way that gameGPT directly judges the extent to which 랄라핑 is agitated between 50% and 100% and is accumulated in addition to the existing success rate.
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
🧑‍🎤🎤랄라핑:
"(실망한 듯) 작곡가님, 저도 엔딩 파트 하고 싶어요. 엔딩이 가장 중요한 부분인데, 저도 자신 있거든요."
성공률: [          ] 0%

잠깐만!🤔💭 :
작곡가의 역할은 가수가 곡의 전체적인 흐름과 감정을 이해하도록 돕고, 음악적으로도 가수의 강점을 최대한 살릴 수 있는 방향을 제시해야 해요!


Example Scenario 2:
🧑‍🎤🎤랄라핑:
"(조금 서운한 듯) 엔딩은 곡의 마무리이자 가장 임팩트 있는 부분이잖아요. 제가 엔딩을 맡으면 팬들도 더 주목할 것 같아요."
성공률: [█         ] 10%

잠깐만!🤔💭 :
가수의 목소리나 스타일이 오프닝을 돋보이게 할 수 있다는 점을 강조하며, 오프닝이 곡의 성공에 큰 영향을 줄 수 있음을 설득하세요.


Example Scenario 3:
🧑‍🎤🎤랄라핑:
"(조금 마음이 풀린 듯) 알겠어요. 곡의 첫 시작이 힘있게 나가면 좋겠다는 생각은 해봤어요. 하지만 정말 엔딩에 대한 아쉬움은 여전히 있어요…"
성공률: [████      ] 40%

잠깐만!🤔💭 :
잘하고 있어요! 오프닝이 가수의 이야기나 감정을 전달하는 첫 부분이므로, 그 중요성을 설명하고 조언하세요.


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

    var text = '🎧지금 이 순간, 작곡가입니다.👨‍🎤🎸';

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

