# YoutubeIdeaGeneratorCrew Crew

Welcome to the YoutubeIdeaGeneratorCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/youtube_idea_generator_crew/config/agents.yaml` to define your agents
- Modify `src/youtube_idea_generator_crew/config/tasks.yaml` to define your tasks
- Modify `src/youtube_idea_generator_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/youtube_idea_generator_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the youtube-idea-generator-crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The youtube-idea-generator-crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the YoutubeIdeaGeneratorCrew Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.


Environment setup instructions.

```markdown:README.md
# YouTube Idea Generator Crew

A CrewAI-powered tool for generating and analyzing YouTube video ideas.

## Environment Setup

### 1. Create and Activate Conda Environment

First, create a new conda environment:
```bash
conda create --name crewai-dev python=3.12.9
```

Activate the conda environment:

```bash
conda activate crewai-dev
```

### 2. Install CrewAI

With the conda environment activated, install CrewAI:

```bash
pip install crewai
```

### 3. Install Project Dependencies

Install the project dependencies using Poetry:

```bash
poetry install
```

This will create a `.venv` folder in your project directory with all the required dependencies.

### 4. Activate the Virtual Environment

After Poetry creates the virtual environment, activate it:

For Unix/Linux/Git Bash:

```bash
source .venv/bin/activate  # Unix/Linux
# OR
source .venv/Scripts/activate  # Windows with Git Bash
```

For Windows Command Prompt:

```bash
.venv\Scripts\activate.bat
```

For PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

### 5. Verify Installation

You can verify you're in the correct environment by checking:

```bash
which python  # Unix/Linux/Git Bash
# OR
where python  # Windows
```

The path should point to the Python interpreter in your `.venv` folder.

## Environment Variables

Create a `.env` file in the project root and add your YouTube API key:

```env
YOUTUBE_API_KEY=your_api_key_here
```
