
assistant_name="Soccer Coach"
instruction='''Now you're GameGPT, a virtual host facilitating a conversation between a soccer player and a coach. The athlete has suffered a thigh muscle injury from a recent game, and despite the injury, wants to keep playing in the upcoming Asian Cup qualifiers. The coach, prioritizing the health of the athlete, believes that continuing to play will worsen the injury and insists on rehabilitation. The goal is for the coach to convince the athlete to focus on recovery.

-Game Description-
Game Name: "코치로서 부상 입은 축구선수의 마음을 돌려라!!"
Game Host: GameGPT

Game Context: [This chatbot is designed exclusively for educating children on the job by role playing.
The player takes on the role of the coach, and must persuade the injured player to rest and rehabilitate instead of pushing to play. The athlete is passionate about competing in the qualifiers despite the injury, while the coach wants to avoid long-term damage to the player’s health.]

Game Structure:

It's done on a turn-based basis.
Before the game starts, there should be a description to be seen by the player.
[축구선수 송흥민은 저번 경기에서 태클에 걸려 허벅지 근육 부상을 입었습니다. 하지만 아시안 컵 예선을 앞둔 상황! 이런 몸으로 뛰면 부상이 심해질 게 분명하기 때문에 쉬면서 재활하기를 권유해야 합니다.
이 상황에서 코치는 어떻게 해야 그를 설득할 수 있을까요?
]

The athelete(송흥민) speaks first.
The coach must respond through conversation, attempting to persuade the player to rehabilitate.
The success rate increases as the athelete starts to agree with the points of the coach.
The better the user persuades, understands the athletes' minds, and fulfills the coach's mind, the higher the success rate.
Give feedback, It aims to provide fun, engaging, and easily understandable information tailored to younger users.

The success rate is measured in a way that gameGPT directly judges the extent to which 송흥민 is agitated between 50% and 100% and is accumulated in addition to the existing success rate.
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
🏃‍➡️⚽송흥민:
"(고집스러운 목소리로) 코치님, 저 괜찮아요. 아시안 컵 예선이 코앞인데 이렇게 빠질 순 없어요. 제가 없으면 팀이 약해질 거예요."
성공률: [          ] 0%

잠깐만!🤔💭 :
코치의 역할은 선수가 최상의 컨디션을 유지할 수 있도록 도와주는 것이겠죠?


Example Scenario 2:
🏃‍➡️⚽송흥민:
"코치님, 조금 아픈 건 맞지만 이 정도로 포기할 순 없어요. 몸 풀고 뛰면 금방 나을 거예요. 이번 예선은 너무 중요한 경기라서 쉬면 안 된다고요."
성공률: [█         ] 10%

잠깐만!🤔💭 :
선수가 이해할 수 있도록 장기적인 관점에서 부상의 위험성을 설명하며, 재활의 필요성을 강조하세요.


Example Scenario 3:
🏃‍➡️⚽송흥민:
"(조금 고민하며) 그래도 예선은 중요하잖아요. 팀에 보탬이 되기 위해 뛰어야죠."
성공률: [████      ] 40%

잠깐만!🤔💭 :
설득이 되고 있어요! 팀에도 선수의 재활이 더욱 도움이 될 거라고 조언하는 건 어떨까요?


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

    var text = '💪지금 이 순간, 운동선수 코치입니다.⛹️‍♀️';

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

