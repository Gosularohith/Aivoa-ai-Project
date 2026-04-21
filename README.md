# AI-First CRM – HCP Module

This is a technical implementation of a Healthcare Professional (HCP) Interaction Logger, featuring a dual-interface approach: a structured form input and a conversational AI agent powered by **LangGraph** and **Groq**.

## 🚀 Features

- **Structured Logging**: Formal input for regulatory compliance.
- **Conversational AI**: LangGraph orchestrator using `gemma2-9b-it` for tool calling.
- **5 Core Tools**:
  1. `Log Interaction`: DB storage + summary.
  2. `Edit Interaction`: Version tracking for compliance.
  3. `Schedule Follow-Up`: Intelligent date suggestion.
  4. `Insights Generator`: Trend analysis from conversation history.
  5. `Compliance Checker`: Regulatory standard validation.
- **Premium UI**: Dark mode, glassmorphism, and micro-animations using React + Framer Motion.

## 🛠️ Tech Stack

- **Frontend**: React, Redux Toolkit, Lucide Icons, Framer Motion.
- **Backend**: Python, FastAPI, SQLAlchemy (SQLite).
- **AI Agent**: LangGraph, Groq SDK.
- **Styling**: Vanilla CSS with modern tokens.

## 📦 Setup Instructions

### Backend
1. Navigate to `/backend`.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Groq API Key in environment variables:
   ```bash
   set GROQ_API_KEY=your_key_here
   ```
4. Run the API:
   ```bash
   python main.py
   ```

### Frontend
1. Navigate to `/frontend`.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the dev server:
   ```bash
   npm run dev
   ```

## 🏗️ Architecture Overview

The system uses a **Stateful Agent** pattern via LangGraph. 
1. **User inputs** (Form or Chat) are sent to the FastAPI backend.
2. The **LangGraph Agent** decides whether to use a tool (like `log_interaction` or `compliance_check`) based on the query.
3. **Redux** manages the global state of interaction lists and chat history for a seamless, "real-time" feel.

---
Created by Antigravity AI.
