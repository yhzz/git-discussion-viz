import wordcloud from './wordcloud.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={wordcloud} className="App-logo" alt="logo" />
        <p>
          Terraform Repository Issue comment wordcloud
        </p>
      </header>
    </div>
  );
}

export default App;
