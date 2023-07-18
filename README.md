
# ML-Tools-Project

![Page_Web](/screenshots/video.gif?raw=true)

The idea is to set up a personalized conversational agent to answer any questions about the Ecole Polytechnique de Thiès using gpt Index.
The aim of this project is to collect and prepare data, implement embedding techniques and write prompts to personalize chatgpt.
For this project we use: LlamaIndex (formerly GPT Index) which is a data framework for LLM applications to ingest, structure, and access private or domain-specific data.




## Environment Variables

To run this project, you will need to:

Add the following environment variables to your .env file

`OPENAI_API_KEY=mykey`

Create and activate a virtual environment for the project. You can use tools like virtualenv or conda for this step.








## Installation

Install the required dependencies

```bash
  cd models
  pip install -r requirements.txt
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/Aida73/ML-Tools-Project.git
```

Go to the project directory

```bash
  cd project
  cd models
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```

## Deployment

This project is deployed on PythonAnywhere. 

To get response from the API: http://da73.pythonanywhere.com

To get response with Vue.js, run this:

```bash
  url: http://da73.pythonanywhere.com/eptinfos

  methods: {
    async postData(question) {
      try {
        const data = {
          question: question
        };
        const response = await axios.post('url', data);
        console.log(response.data);
        // Handle the response data or perform other operations
      }
      catch (error) {
        console.error(error);
        // Handle the error
      }
    }
  }
```

## Screenshots
Réponse attendue quand la clé ne fonctionne plus:
![App Screenshot](/screenshots/keyBlocked.png?raw=true)

Réponse attendue quand la clé ne fonctionne plus:
![App Screenshot](/screenshots/deployed.png?raw=true)

## Tech Stack

**Backend:** Flask
**Web:** HTML, JavaScript, CSS



## Data collection

The model is training by scrapping the website `www.ept.sn`

To get the data, run the extract.py script:

```
cd data_collection
python extract_data.py

```
txt files with be generated and saved into knowledge folder
