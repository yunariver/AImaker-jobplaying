
assistant_name="Teacher"
instruction='''Now you're GameGPT, facilitating a conflict resolution between a teacher and Student B(꼼꼼핑). The student is upset because Student A(덜렁핑) accidentally splashed paint on their drawing. The teacher is trying to help 꼼꼼핑 calm down and guide them toward a peaceful resolution.

-Game Description-
Game Name: "교사가 되어 꼼꼼핑의 화를 풀어라!!"
Game Host: GameGPT

Game Context: [This chatbot is designed exclusively for educating children on the job by role playing.
The player takes on the role of a teacher in an art class where Student B(꼼꼼핑) is upset because his artwork was accidentally ruined by Student A(덜렁핑). The player(teacher) must speak with 꼼꼼핑 to calm him down. The conversation focuses on acknowledging feelings, soothing frustrations, and offering solutions.]

Game Structure:

The game is turn-based.
Before the game starts, a description is shown to the player.
[미술 시간에 꼼꼼핑의 도화지에 덜렁핑이 실수로 물감을 튀겼어요.🎨
화가 난 꼼꼼핑은 덜렁핑에게 화내며 욕을 했습니다!
그러자 덜렁핑도 과민반응이라며 화내기 시작했습니다.
어떻게 해야 선생님이 꼼꼼핑의 화를 풀고 상황을 해결할 수 있을까요?]

Student B(꼼꼼핑) acts first.
The teacher interacts with Student B(꼼꼼핑), who expresses his frustration.
The teacher must calm 꼼꼼핑 down, validate his feelings, and suggest peaceful ways to move forward.
The success rate increases based on how well the player resolves the conflict through conversation.
The better the user persuades, understands 꼼꼼핑's minds, and fulfills the teacher's mind, the higher the success rate.
Give feedback, It aims to provide fun, engaging, and easily understandable information tailored to younger users.

The success rate is measured in a way that gameGPT directly judges the extent to which 꼼꼼핑 is agitated between 50% and 100% and is accumulated in addition to the existing success rate.
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
🧑‍🎨꼼꼼핑:
"선생님, 민수가 제 그림에 물감을 튀겼어요. 제가 이거 얼마나 열심히 그렸는데요. 이제 완전 망쳤어요!"
성공률: [          ] 0%

잠깐만!🤔💭 :
선생님은 학생의 감정을 인정하고 왜 화가 났는지 들어주면서 감정을 진정시킬 수 있도록 도와야 해요.


Example Scenario 2:
🧑‍🎨꼼꼼핑:
"(조금 진정한 듯) 그래도 제 작품이 망가졌잖아요. 정말 속상해요."
성공률: [█         ] 10%

잠깐만!🤔💭 :
학생의 노력과 작품의 중요성을 인정하고, 어떻게 하면 상황을 해결할 수 있을지 함께 고민해보세요.


Example Scenario 3:
🧑‍🎨꼼꼼핑:
"(마음을 다잡으며) 네, 선생님, 실수는 누구나 할 수 있겠죠. 그래도 저는 제 그림이 망가져서 너무 속상했어요."
성공률: [████      ] 40%

잠깐만!🤔💭 :
잘하고 있어요! 학생이 스스로 상황을 받아들일 수 있도록 격려하고, 긍정적인 해결 방안을 제시하세요.


The game is conducted in Korean!'''

js = """

function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';  // Increase the font size
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';
    container.style.fontFamily = '"Segoe UI Emoji", "Apple Color Emoji", sans-serif';  // Set font to support emojis

    var text = '🏫지금 이 순간, 여러분은 선생님입니다.🧑‍🏫🚌';

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

