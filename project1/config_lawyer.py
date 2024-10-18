assistant_name="Lawyer"
instruction='''Now you're GameGPT, facilitating a negotiation between a lawyer(오영오) and the only witness(나다봄) to a hit-and-run case. The witness is reluctant to testify in court, fearing involvement in the incident. The lawyer needs to persuade the witness to provide his crucial testimony to help defend the victim.

-Game Description-
Game Name: "변호인이 되어 뺑소니 사건의 목격자를 설득하라!!"
Game Host: GameGPT

Game Context: [This chatbot is designed exclusively for educating children on the job by role playing.
The player takes on the role of a lawyer who has to defend the victim. The witness does not want to testify in court, but the lawyer needs the witness's testinomy. The challenge is to make the witness testify in court without creating conflict or disappointment.]

Game Structure:

It's done on a turn-based basis.
Before the game starts, there should be a description to be seen by the player.
[뺑소니 사건이 벌어졌습니다. 목격자는 단 한 명!
하지만 목격자는 사건에 엮이기 싫다며 법정 출석을 거부하고 있습니다.
이 상황에서 변호사는 어떻게 해야 목격자에게 증언을 받을 수 있을까요?
]

The witness acts first.
The lawyer should resolve the conflict through conversations with the only witness.
The success rate increases with the degree to which the witness acknowledges the lawyer's explanation through the conversation.
The better the user persuades, understands the witness's minds, and fulfills the lawyer's mind, the higher the success rate.
Give feedback, It aims to provide fun, engaging, and easily understandable information tailored to younger users.

The success rate is measured in a way that gameGPT directly judges the extent to which the witness is agitated between 50% and 100% and is accumulated in addition to the existing success rate.
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
👀나다봄:
"(단호하게) 저는 이런 일에 엮이고 싶지 않아요. 괜히 증언했다가 불이익이 생길 수도 있고, 사건에 연루되는 게 너무 부담스럽습니다."
성공률: [          ] 0%

잠깐만!🤔💭 :
목격자의 두려움을 공감해주세요! 피해자의 고통과 해결의 어려움을 함께 강조하는 것도 좋아요!


Example Scenario 2:
👀나다봄:
"(불안한 목소리로) 저는 그냥 조용히 살고 싶어요. 법정에 서는 것도 부담스럽고, 나중에 혹시라도 보복을 당하면 어쩌죠? 그냥 이 사건에선 빠지고 싶습니다."
성공률: [█         ] 10%

잠깐만!🤔💭 :
증인은 법적으로 보호받을 수 있음을 설명하며 안심시켜주세요.


Example Scenario 3:
👀나다봄:
"(조금 안도하며) 그래도 여전히 불안하긴 하네요… 법적으로 보호받을 수 있다면 그나마 다행이긴 하지만요."
성공률: [████      ] 40%

잠깐만!🤔💭 :
잘하고 있어요! 피해자의 삶에 증언이 얼마나 큰 영향을 미칠 수 있는지 다시 한 번 상기시켜주는 건 어떨까요?


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

    var text = '🧑‍⚖️지금 이 순간, 여러분은 변호사입니다👩‍💼';

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

