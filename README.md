# Remi Virtual Assistant (In Development)

**Remi Virtual Assistant** is my graduate project, built using the LLaMA-3 model with Retrieval-Augmented Generation (RAG) for enhanced responses. The assistant features text-to-speech via ElevenLabs and includes a 3D character in Unity. Users can interact with Remi using speech recognition in Unity or chat with her via text through a Telegram chatbot.

**Demo link:** [https://youtu.be/oCxqDoF6ggI]

## Code Files Overview

### 1. `remi-llama3.ipynb`
This notebook handles the integration of the LLaMA-3 model with the Telegram bot. It uses RAG, semantic search, and intent recognition to enhance response accuracy and control function calling (e.g., fetching news, weather updates, setting timers, etc.).

#### Telegram Bot Features:
- **Session Separation:** All user sessions are handled separately based on `chat_id`, ensuring individualized conversations.
- **Local Session History:** Conversations are saved locally, preventing loss of dialogue even if the server restarts. Each user and character has separate session histories.
- **Voice Generation:** Responses are delivered in Remi's voice, using ElevenLabs text-to-speech.

#### LLaMA-3 Model Features:
- **Retrieval-Augmented Generation (RAG):** For improved accuracy and contextual relevance.
- **Tool Usage Integration:** The model can interact with external tools, such as retrieving news or setting reminders.
- **Intent Recognition:** The system identifies user intents to select appropriate actions or call specific functions.
- **Semantic Search:** Enables Remi to find the most relevant information and respond in a meaningful way.

---

### 2. `wakeword.py`
This script contains code for wake word detection using Picovoice, allowing Remi to activate through a specific voice command. Note: We will update this soon to use our custom wake word model, previously implemented from scratch. Picovoice is currently being used for its high accuracy.

---

### 3. `speech.py`
This file includes two key functions:
- **Speech to Text:** Utilizes Google's speech recognition to convert voice input into text.
- **Text to Speech:** Uses ElevenLabs to convert text responses back into speech for a more interactive user experience.

---

### Unity Files
The Unity project files (including the 3D character model and interaction system) will be added soon.

---

## To-Do List:
- [ ] Fine-tune the model to act like a female virtual assistant using all stored data.
- [ ] Implement the custom wake word detection network.
- [ ] Give Remi vision by adding eyes, enabling more interaction with the user.

---

