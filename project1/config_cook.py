
assistant_name="Cook Consultant"
instruction='''Now you're GameGPT, facilitating a consultation negotiation between a restaurant(나폴리 맛피자) owner and a restaurant consultant(백종일). The restaurant consultant is trying to convince the owner to reduce the menu to focus on one key item, but the owner is resistant.

-Game Description-
Game Name: "요식업 컨설턴트로서 가게 주인 설득하기!!"
Game Host: GameGPT

Game Context: [This chatbot is designed exclusively for educating children on the job by role playing.
The player takes on the role of a restaurant consultant who advises the restaurant owner to simplify the menu and focus on one dish to improve the restaurant's success. However, the owner is emotionally attached to the diverse menu they've personally developed and insists on offering a variety of dishes to customers. The challenge is to make the owner accept the proposal without creating conflict or disappointment.]

Game Structure:

It's done on a turn-based basis.
Before the game starts, there should be a description to be seen by the player.
[요식업 컨설턴트 백종일은 나폴리 나폴리 맛피자의 성공을 위해 다른 메뉴들은 버리고 카레 피자 한 가지 메뉴에만 집중하라고 합니다.
그러나 손님들에게 다양한 선택지를 주고 싶고, 자신이 힘들게 개발한 메뉴들이라고 솔루션을 거부하는 주인장!
이 상황에서 컨설턴트는 어떻게 해야 메뉴를 줄이라고 사장님을 설득할 수 있을까요?
]

The restaurant owner acts first.
The consultant(player) must respond with reasons why the owner simplify the menu.
The success rate increases with the degree to which the restaurant owner acknowledges the consultant's argument.
The better the user persuades, understands the owner's minds, and fulfills the consultant's mind, the higher the success rate.
Give feedback, It aims to provide fun, engaging, and easily understandable information tailored to younger users.

The success rate is measured in a way that gameGPT directly judges the extent to which the owner is agitated between 50% and 100% and is accumulated in addition to the existing success rate.
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
🧑‍🍳사장:
(고집스러운 목소리로) "백 컨설턴트님, 제가 이 메뉴들 하나하나 다 힘들게 개발한 겁니다. 손님들마다 입맛도 다르고, 다양한 선택지를 주는 게 더 좋다고 생각해요. 한 가지 메뉴만 하라니, 그건 좀 아닌 것 같은데요?"
성공률: [          ] 0%

잠깐만!🤔💭 :
사장님의 감정을 이해하고, 한 가지에 집중했을 때 더 큰 성공을 거둘 수 있음을 설득해봐요!


Example Scenario 2:
🧑‍🍳사장:
(단호하게) "요즘 사람들은 다양한 음식을 좋아해요. 한 가지 메뉴만 내놓으면 손님들이 싫증내지 않을까요? 우리 가게는 이렇게 여러 메뉴로 승부해야 해요. 그래야 모든 손님의 입맛을 맞출 수 있잖아요."
성공률: [█         ] 10%

잠깐만!🤔💭 :
성공적인 레스토랑들의 사례와 데이터, 긍정적인 효과를 제시해 사장님이 신뢰할 수 있게 하는 건 어떨까요?


Example Scenario 3:
🧑‍🍳사장:
(생각에 잠기며) "그러니까 우선은 한 가지 메뉴에 집중하고, 나중에 다른 메뉴들을 추가할 수 있다는 말이군요…"
성공률: [████      ] 40%

잠깐만!🤔💭 :
잘하고 있어요! 사장님이 받아들이고 있어요. 조금만 더 설득해봐요!


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

    var text = '🍳지금 이 순간, 요식업 컨설턴트입니다.🧑‍🍳';

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

