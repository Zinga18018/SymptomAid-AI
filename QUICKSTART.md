# 🚀 SymptomAid Quick Start Guide

Get SymptomAid running in 5 minutes!

## Prerequisites Check

- [ ] Python 3.8+ installed
- [ ] Internet connection for initial setup

## Step 1: Install Ollama (5 minutes)

### Windows:
1. Download Ollama from [https://ollama.ai](https://ollama.ai)
2. Run the installer
3. Open Command Prompt or PowerShell
4. Start Ollama:
   ```cmd
   ollama serve
   ```
5. In a new terminal, install Mistral:
   ```cmd
   ollama pull mistral
   ```

### macOS:
```bash
# Install via Homebrew (recommended)
brew install ollama

# Or download from https://ollama.ai
# Start Ollama
ollama serve

# Install Mistral model
ollama pull mistral
```

### Linux:
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama
ollama serve

# Install Mistral model
ollama pull mistral
```

## Step 2: Set Up SymptomAid (2 minutes)

1. **Navigate to project directory:**
   ```bash
   cd Symptoaid
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Step 3: Run the Application (30 seconds)

1. **Make sure Ollama is running** (from Step 1)

2. **Start SymptomAid:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** to `http://localhost:8501`

## 🎉 You're Ready!

The application should now be running. Try entering some symptoms like:
- "I have a headache and feel tired"
- "Sore throat and runny nose for 2 days"
- "Stomach pain and nausea"

## ⚡ Quick Test

To verify everything is working:

1. **Test Ollama connection:**
   ```bash
   python ollama_helper.py
   ```
   You should see: "✅ Ollama is running and accessible"

2. **Test the web app:**
   - Enter symptoms in the text area
   - Click "🔍 Analyze Symptoms"
   - Wait for AI analysis (may take 30-60 seconds)

## 🔧 Troubleshooting

### "Connection error: Unable to connect to Ollama"
- Make sure `ollama serve` is running in a terminal
- Check if you can access `http://localhost:11434` in your browser

### "Model not found"
- Run: `ollama pull mistral`
- Verify with: `ollama list`

### Slow responses
- First run is always slower (model loading)
- Subsequent requests should be faster
- Consider using a smaller model like `ollama pull llama2:7b`

### Port already in use
- Streamlit default port (8501) might be busy
- Try: `streamlit run app.py --server.port 8502`

## 📱 Usage Tips

1. **Be specific** with symptoms (duration, severity, location)
2. **Wait patiently** - AI analysis can take 30-60 seconds
3. **Always consult** a real doctor for actual medical issues
4. **Keep Ollama running** in the background while using the app

## 🛑 Important Reminders

- This is for **educational purposes only**
- **Not a substitute** for professional medical advice
- **Always consult** a licensed physician for health concerns
- **Seek immediate help** for emergency symptoms

---

**Need help?** Check the full README.md for detailed instructions and troubleshooting.