"use strict";

const e = React.createElement;

// individual question
class Question extends React.Component {
  state = {};

  render() {
    return (
      <button
        className={
          "btn-link btn question" + (this.props.isActive ? " qactive" : "")
        }
        style={{ textDecoration: "none" }}
        onMouseOver={() => this.props.handleHover(this.props.question.id)}
        onClick={() => this.props.answerVisitor(this.props.question["goto"])}
      >
        {"\u2217\t" + this.props.question["question"]}
        <span className="blinking">{"_"}</span>
      </button>
    );
  }
}

// collection of Question elements
class Questions extends React.Component {
  state = {};

  render() {
    return (
      <React.Fragment>
        <ul
          className="question-ul"
          style={{
            listStyleType: "none"
          }}
        >
          {this.props.questions.map(question => (
            <li key={question.id}>
              <Question
                isActive={
                  this.props.activeQuestion == question.id ? true : false
                }
                key={question.id}
                handleHover={this.props.handleHover}
                answerVisitor={this.props.answerVisitor}
                question={question}
              />
            </li>
          ))}
        </ul>
      </React.Fragment>
    );
  }
}

// update the questions
function ShowQuestions({
  questions,
  handleHover,
  activeQuestion,
  handleDialogUpdate
}) {
  return (
    <Questions
      questions={questions}
      handleHover={handleHover}
      answerVisitor={handleDialogUpdate}
      activeQuestion={activeQuestion}
    />
  );
}

// main class
class Conversation extends React.Component {
  constructor(props) {
    super(props);
    this.dialogs = conversation; // assigns the json file to a class variable
    this.state = {
      questions: this.dialogs["Start"]["questions"],
      activeQuestionId: 1,
      typed: new Typed("#typed", {
        strings: this.dialogs["Start"]["strings"],
        typeSpeed: 40
      })
    };
  }

  // update the answer and show the next set of questions
  handleDialogUpdate = goto => {
    const newDialogElement = this.dialogs[goto];
    this.setState({ questions: newDialogElement["questions"] });
    this.state.typed.destroy();
    const typed = new Typed("#typed", {
      strings: newDialogElement["strings"],
      typeSpeed: 40
    });
    this.setState({ typed });
    this.setState({ activeQuestionId: 1 });
  };

  keyHandling = e => {
    const max_index = this.state.questions.length;
    let activeQuestionId = this.state.activeQuestionId;
    if (e.key == "Enter") {
      this.handleDialogUpdate(this.state.questions[activeQuestionId - 1].goto);
    } else {
      if (e.key == "ArrowUp" || e.key == "Up") {
        if (activeQuestionId == 1) activeQuestionId = max_index;
        else activeQuestionId--;
      } else if (e.key == "ArrowDown" || e.key == "Down") {
        if (activeQuestionId == max_index) activeQuestionId = 1;
        else activeQuestionId++;
      }
      this.setState({ activeQuestionId });
    }
  };

  handleHover = activeId => {
    this.setState({ activeQuestionId: activeId });
  };

  handleArrowKey = () => {
    window.addEventListener("keydown", this.keyHandling);
  };

  render() {
    this.handleArrowKey();

    return (
      <React.Fragment>
        {/* the questions are rendered here through the ShowQuestions function */}
        <div className="question-box console text-left">
          <div className="console-head">About Me</div>

          <div style={{ padding: "10px" }}>
            <span style={{ color: "#eb5d49" }}>
              {"website:~ visitor$ hellosudeep"}
            </span>
            <br />
            <span style={{ color: "#69ca42" }}>
              {"Please use arrow-keys or mouse pointer."}
            </span>
            <div>
              <ShowQuestions
                questions={this.state.questions}
                handleHover={this.handleHover}
                activeQuestion={this.state.activeQuestionId}
                handleDialogUpdate={this.handleDialogUpdate}
              />
            </div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

const domContainer = document.querySelector("#react-dialog");
ReactDOM.render(e(Conversation), domContainer);
