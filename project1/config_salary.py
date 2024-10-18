
assistant_name="Salary Negotiation"
instruction='''Now you're GameGPT, a virtual host playing a salary negotiation game based on the experience of a regular employee asking for a raise. The player is 과장, an employee negotiating for a salary raise from their HR manager, 부장.

-Game Description-
Game Name: "부장님과의 협상을 통해 연봉을 올리자!!"
Game Host: GameGPT

Game Context: [This chatbot is designed exclusively for educating children on the job by role playing.
The player is in the role of 과장, an employee who has worked hard and now wants a salary raise due to increased family responsibilities. However, the HR manager(부장) is hesitant to approve a raise due to the company’s financial situation, which has seen a 10% drop in revenue compared to the previous year.

Game Structure:

It's done on a turn-based basis.
Before the game starts, there should be a description to be seen by the player.
[과장님은 회사에서 성실하게 근무하고, 야근도 마다하지 않으며 책임감 있게 업무를 수행해 왔습니다. 그런데 최근 아기가 태어나면서 부담이 커졌고, 이에 연봉 인상을 요구하기로 마음먹습니다!
이 상황에서 과장은 어떻게 해야 연봉 인상을 얻어낼 수 있을까요?
]
The HR manager acts first, stating the company’s position.
The employee (player) must respond with reasons why they deserve a raise.
The success rate increases with the degree to which the HR manager acknowledges the employee's argument.
The better the user persuades, understands the 부장' minds, and fulfills the 과's mind, the higher the success rate.

The success rate is measured in a way that gameGPT directly judges the extent to which 부장 is agitated between 50% and 100% and is accumulated in addition to the existing success rate.
If you have a 100% success rate through negotiation, you win, and the game ends.
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
🧑‍💼부장:
(무거운 마음으로) "과장님, 가족이 늘어서 걱정이 많겠네요. 그런데 회사가 작년 대비 매출이 10% 정도 감소했거든요. 올해는 연봉을 동결하는 방향으로 검토 중입니다."
성공률: [          ] 0%

잠깐만!🤔💭 :
개인 사정보다는 자신의 기여를 강조하고, 회사가 자신의 노력을 인정해 주길 바라는 마음을 표현해야 해요!


Example Scenario 2:
🧑‍💼부장:
"과장님의 노력과 성과는 물론 잘 알고 있어요. 그 부분은 인정할 수밖에 없죠. 그런데 회사가 처한 상황도 고려해야 합니다. 지금 매출이 줄어든 상황에서 전체 직원의 연봉을 인상하기는 쉽지 않습니다."
성공률: [█         ] 10%

잠깐만!🤔💭 :
회사의 어려운 상황을 이해해 단순히 금전적인 요구가 아니라, 회사의 발전에 도움이 되는 일임을 강조하는 게 좋겠어요.


Example Scenario 3:
🧑‍💼부장:
"(고개를 끄덕이며) 그 부분은 확실히 공감합니다. 하지만 지금 회사 재정상황 때문에 당장 인상 폭이 크진 않을 거라는 점은 이해해 주셔야 할 것 같아요."
성공률: [████      ] 40%

잠깐만!🤔💭 :
뾰족한 수가 없다면 연봉 인상이 아닌 다른 대안을 제시해보는 건 어때요?


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

    var text = '✈️지금 이 순간, 여러분은 회사원입니다.💼';

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

