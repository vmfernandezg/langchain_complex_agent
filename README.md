# LangChain Complex Agent

A sophisticated AI agent built with LangGraph and Python, featuring:

- **Math Tools**: Calculator, power, modulus, factorial, is_prime.
- **Text Tools**: String reversal, case manipulation, vowel removal, word counting.
- **Interactive CLI**: A loop-based interface for chatting with the agent.
- **Spanish Localization**: Fully translated system prompts and UI.

## Setup

1. Run setup script:

    ```powershell
    .\setup_env.ps1
    ```

2. Start the agent:

    ```powershell
    .\start.ps1
    ```

    Then run:

    ```powershell
    python src/agent_app/main.py
    ```

## Project Structure

- `src/agent_app`: Main application code.
- `src/agent_app/tools`: Custom tools for math and text processing.
- `tests`: Unit tests.
