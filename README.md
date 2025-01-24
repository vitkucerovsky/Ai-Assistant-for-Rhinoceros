# AI Rhino Assistant 🤖🦏

AI Rhino Assistant is an intelligent chatbot that seamlessly integrates with **Rhinoceros 3D**. It allows users to interact with Rhino using natural language commands, leveraging the power of the **DeepSeeker R1 model** through API calls. Simplify complex workflows, automate repetitive tasks, and bring AI-driven creativity directly into your design process!

## 🚀 Features
![Demo GIF](https://youtu.be/JegjmLcmvIg)

- **Natural Language Commands**: Perform tasks in Rhino just by chatting with the assistant.
- **Powered by DeepSeeker R1**: Uses advanced AI capabilities for understanding and executing user requests.
- **Streamlined Workflow**: Save time by automating design tasks and eliminating the need for manual scripting.

## 🛠️ Installation & Setup

### Prerequisites
1. **Rhinoceros 3D** installed on your system.
2. An **API Key** for the DeepSeeker R1 model.

### Steps to Run
1. **Clone or download this repository**:
   ```bash
   git clone https://github.com/your-username/ai-rhino-assistant.git
   cd ai-rhino-assistant
   ```
2. **Add your API Key**:
   - Open the Python code file in this repository.
   - Locate the placeholder line:  
     ```python
     API_KEY = "your-api-key-here"
     ```
   - Replace `"your-api-key-here"` with your actual API key.

3. **Start Rhino**:
   - Open Rhinoceros 3D.
   - Type the command `RunPythonScript` in the command bar and hit **Enter**.
   - Select the Python script from this repository.

4. **Chat with the Assistant**:
   - Once the script is running, start chatting with the bot.
   - Give your commands (e.g., "Create a cube" or "Generate a parametric surface").
   - Wait for the bot to process and execute your request. 🎉

## 📋 Examples
Here are some commands you can try:
- create an architectural plan for a 10 bedroom hotel, you can generate cordinates of the spaces and then draw polylines to show the plans

## ⚠️ Notes
- Ensure your system is connected to the internet for the bot to communicate with the DeepSeeker R1 API.
- The bot might take a few moments to process commands, depending on the complexity of the task and network speed.

## 🧩 Future Plans
- Extend functionality for more advanced parametric modeling.
- Add Vision to the assistant

## 💬 Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

