# AI Transcript Summarizer with Custom MCP Integration

This project is part of an AI training program and demonstrates how to create a custom integration with the Model Context Protocol (MCP) to summarize transcript files. It leverages multiple MCP servers, including file system access and Gmail, along with OpenAI's GPT-4o model to process user prompts and return summarized content.

## 🧠 Purpose

The application helps users:
- Summarize content from transcript or document files located in a specified local directory.
- Generate professional and concise summaries suitable for email.
- (Optionally) Prepare summaries to be sent via Gmail, when provided with recipient details.

The application uses MCP tools to simulate interaction with real-world data sources, focusing on document summarization and automation through LangChain agents.

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/arijnafi/Custom-MCP-Integration
   cd Custom-MCP-Integration
   ```

2. **Install dependencies**
   Ensure you have Python 3.10 and Node.js installed. Then:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare credentials**
   - Place your Gmail credentials JSON file as `credentials.json` in the root directory.
   - Replace the placeholder `...` in the script with your actual OpenAI API key or set it in your environment:
     ```bash
     export OPENAI_API_KEY="your-key-here"
     ```

4. **Ensure Node packages can be run via `npx`**
   The project uses `npx` to run MCP servers for Gmail and file system integration. You must have a working internet connection for package resolution.

---

## ▶️ Usage Example

Run the script and input your request:

```bash
python client.py
```

Example prompt:
```
Please summarize the file: transcript_meeting_april.txt and prepare it for an email to john@example.com.
```

If the email is not specified in the prompt, the assistant will request it.

---

## 🚫 Limitations / Known Issues

- **Gmail integration** requires valid credentials and may fail silently if setup incorrectly.
- **File system access** is limited to the local `files` directory only.
- **Long documents** are summarized based on key points but may miss low-priority details.
- **Email sending** is not triggered unless the prompt explicitly includes recipient information.
- **No GUI** – currently CLI-only.
- **Security** – Do not include sensitive content without validation; summaries do not redact private info unless prompted.

---

## 📁 Project Structure

```
.
├── credentials.json          # Gmail OAuth credentials
├── files/                    # Directory containing transcript files
├── summarize.py              # Main script
└── README.md                 # Project documentation
```

---

## 📬 Contact

For questions or support, please open an issue or contact the repository owner.
