Vanna example
=============
Github: https://github.com/vanna-ai/vanna

Docs: https://vanna.ai/docs/index.html

## Setup
### Install pipenv
```bash
pip install pipenv
```

### Install dependencies
```bash
pipenv sync
```

### Environment Variables
```bash
cp .env.example .env
```
Fill in the environment variables in `.env`
* `EMAIL`: Email address used in get_started.py. Vanna will send you an email with a login code.
* `OPENAI_ACCESS_TOKEN`: OpenAI API key used in training_example.

## Examples
### Example 1: Get started
```bash
pipenv run python get_started.py
```

### Example 2: Training Example
```bash
cd training_example

# First, train the model
pipenv run python main.py train

# Then, ask the model a question. e.g. "What are the top 5 artists by sales?"
pipenv run python main.py ask "[QUESTION]"

# Or launch UI
pipenv run python main.py ui
```
