
# ML-Tools-Project

![Page_Web](/screenshots/video.gif?raw=true)

The idea is to set up a personalized conversational agent to answer any questions about the Ecole Polytechnique de Thiès using gpt Index.
The aim of this project is to collect and prepare data, implement embedding techniques and write prompts to personalize chatgpt.
For this project we use: LlamaIndex (formerly GPT Index) which is a data framework for LLM applications to ingest, structure, and access private or domain-specific data.

Website link : http://chatbotept.s3-website.us-east-2.amazonaws.com/



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
You will get a local link to try the API.


If you want to interact with the chatbot directly on your computer, without using the aws link :
- dowload the code available on the web branch of this repository
- open the index.html file directly in your browser.

  
## Deployment

This project is deployed on PythonAnywhere. 

To get response from the API: http://da73.pythonanywhere.com

The chatbot web page is deployed on aws : http://chatbotept.s3-website.us-east-2.amazonaws.com/

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
