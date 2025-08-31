const questions = [
    {
      question: "What is the fastest land animal?",
      answers: [
        { text: "Cheetah", correct: true },
        { text: "Lion", correct: false },
        { text: "Horse", correct: false },
        { text: "Ostrich", correct: false }
      ]
    },
    {
      question: "Which animal is known as the King of the Jungle?",
      answers: [
        { text: "Elephant", correct: false },
        { text: "Tiger", correct: false },
        { text: "Lion", correct: true },
        { text: "Leopard", correct: false }
      ]
    },
    {
      question: "Which mammal lays eggs?",
      answers: [
        { text: "Kangaroo", correct: false },
        { text: "Platypus", correct: true },
        { text: "Dolphin", correct: false },
        { text: "Bat", correct: false }
      ]
    },
    {
      question: "How many legs does a spider have?",
      answers: [
        { text: "6", correct: false },
        { text: "8", correct: true },
        { text: "10", correct: false },
        { text: "12", correct: false }
      ]
    }
  ];
  
  const questionElement = document.getElementById('question');
  const answerButtons = document.getElementById('answer-buttons');
  const nextButton = document.getElementById('next-btn');
  const resultContainer = document.getElementById('result-container');
  const scoreElement = document.getElementById('score');
  
  let currentQuestionIndex = 0;
  let score = 0;
  
  function startQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerText = 'Next';
    resultContainer.classList.add('hide');
    document.getElementById('question-container').classList.remove('hide');
    showQuestion();
  }
  
  function showQuestion() {
    resetState();
    let currentQuestion = questions[currentQuestionIndex];
    questionElement.innerText = currentQuestion.question;
  
    currentQuestion.answers.forEach(answer => {
      const button = document.createElement('button');
      button.innerText = answer.text;
      button.classList.add('btn');
      if (answer.correct) {
        button.dataset.correct = answer.correct;
      }
      button.addEventListener('click', selectAnswer);
      answerButtons.appendChild(button);
    });
  }
  
  function resetState() {
    nextButton.classList.add('hide');
    answerButtons.innerHTML = '';
  }
  
  function selectAnswer(e) {
    const selectedBtn = e.target;
    const isCorrect = selectedBtn.dataset.correct === "true";
    if (isCorrect) {
      selectedBtn.style.backgroundColor = '#4caf50';
      score++;
    } else {
      selectedBtn.style.backgroundColor = '#f44336';
    }
  
    Array.from(answerButtons.children).forEach(button => {
      button.disabled = true;
      if (button.dataset.correct === "true") {
        button.style.backgroundColor = '#4caf50';
      }
    });
  
    nextButton.classList.remove('hide');
  }
  
  nextButton.addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
      showQuestion();
    } else {
      showScore();
    }
  });
  
  function showScore() {
    document.getElementById('question-container').classList.add('hide');
    resultContainer.classList.remove('hide');
    scoreElement.innerText = `${score} / ${questions.length}`;
  }
  
  startQuiz();