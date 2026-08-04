import { useState } from "react";
import { generateLearningPath } from "./api/api";


function App() {

  const [result, setResult] = useState(null);


  const testAPI = async () => {

    const requestData = {

      goal_role: "ML Engineer",

      known_skills: [
        "Python Programming"
      ],

      experience: "Beginner"

    };


    const response = await generateLearningPath(
      requestData
    );


    setResult(response);

  };


  return (

    <div>

      <h1>
        Learning Recommendation System
      </h1>


      <button onClick={testAPI}>
        Generate Learning Path
      </button>


      {
        result && (

          <pre>
            {JSON.stringify(
              result,
              null,
              2
            )}
          </pre>

        )
      }


    </div>

  );

}


export default App;