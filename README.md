# 🏥 SymptomAid - Professional AI Symptom Analysis

**SymptomAid** is a sophisticated, educational AI-powered symptom analysis application built with Streamlit and powered by local LLM technology (Mistral via Ollama). This professional-grade tool provides comprehensive symptom analysis while maintaining strict educational boundaries and emphasizing the critical importance of professional medical consultation.

## ✨ Key Features

- 🎨 **Professional UI/UX**: Clean, responsive design with medical-themed styling
- 🧠 **Advanced AI Analysis**: Powered by Mistral LLM for comprehensive symptom evaluation
- 📊 **Structured Output**: Organized analysis with causes, body systems, specialists, and warnings
- 🛡️ **Safety-First Design**: Multiple disclaimers and safety warnings throughout
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🔒 **Privacy-Focused**: All processing done locally with Ollama
- 📚 **Educational Focus**: Designed to inform and educate, not diagnose

## ⚠️ Critical Medical Disclaimer

**🛑 THIS APPLICATION IS FOR EDUCATIONAL PURPOSES ONLY**

SymptomAid does not provide medical advice, diagnosis, or treatment. It is designed as an educational tool to help users understand potential medical considerations. Always consult qualified healthcare professionals for medical concerns. In emergencies, contact emergency services immediately.

## 🎯 Application Structure

### Core Components

- **`app.py`**: Main Streamlit application with professional UI/UX
- **`ollama_helper.py`**: LLM integration and prompt management
- **`style.css`**: Professional CSS styling for enhanced visual appeal
- **`requirements.txt`**: Python dependencies

### Analysis Output Sections

1. **🧾 Possible Medical Causes**: Three potential causes with probability assessments
2. **🧠 Affected Body Systems**: Detailed system involvement analysis
3. **👩‍⚕️ Recommended Medical Specialist**: Primary and alternative specialist recommendations
4. **⚠️ Warning Signs to Monitor**: Symptoms requiring close observation
5. **🚨 Emergency Care Triggers**: Critical symptoms requiring immediate attention
6. **📋 Next Steps**: Actionable guidance for users

## 🧠 How the AI Analysis Works

### LLM Prompt Engineering

SymptomAid uses a sophisticated prompt engineering approach to ensure comprehensive and safe analysis:

```
You are a professional medical AI assistant designed for educational purposes only. 
Analyze the following symptoms and provide a comprehensive, structured response 
that helps users understand potential medical considerations while emphasizing 
the need for professional consultation.
```

### Analysis Framework

The AI follows a structured analysis framework:

1. **Symptom Interpretation**: Natural language processing of user input
2. **Medical Knowledge Application**: Cross-referencing symptoms with medical knowledge
3. **Risk Assessment**: Evaluating potential severity and urgency
4. **Specialist Matching**: Recommending appropriate medical specialists
5. **Safety Prioritization**: Emphasizing emergency signs and professional consultation

### Safety Mechanisms

- **Input Validation**: Filters inappropriate or harmful content
- **Response Validation**: Ensures medical disclaimers are present
- **Multiple Disclaimers**: Prominent warnings throughout the interface
- **Emergency Emphasis**: Clear guidance on when to seek immediate care

## 📋 Prerequisites

Before running the application, ensure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running
3. **Mistral model** downloaded in Ollama

## 🛠️ Installation & Setup

### Prerequisites

- **Python 3.8+**: Ensure you have Python installed
- **Ollama**: Local LLM runtime environment
- **Mistral Model**: The AI model for symptom analysis
- **8GB+ RAM**: Recommended for optimal performance

### Step 1: Install Ollama

#### Windows:
1. Download Ollama from [https://ollama.ai](https://ollama.ai)
2. Run the installer and follow the setup wizard
3. Open Command Prompt or PowerShell as Administrator
4. Verify installation: `ollama --version`

#### macOS:
```bash
# Using Homebrew (recommended)
brew install ollama

# Or download from website
# Visit https://ollama.ai and download the macOS installer
```

#### Linux:
```bash
# Official installation script
curl -fsSL https://ollama.ai/install.sh | sh

# Verify installation
ollama --version
```

### Step 2: Install and Configure Mistral Model

```bash
# Pull the Mistral model (this may take several minutes)
ollama pull mistral

# Verify the model is installed
ollama list
```

### Step 3: Start Ollama Service

```bash
# Start the Ollama service
ollama serve

# The service will run on http://localhost:11434
# Keep this terminal window open while using SymptomAid
```

### Step 4: Setup SymptomAid Application

```bash
# Clone the repository
git clone <repository-url>
cd symptoaid

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

### Quick Start

1. **Ensure Ollama is running**:
   ```bash
   # In a separate terminal window
   ollama serve
   ```

2. **Launch SymptomAid**:
   ```bash
   # In your project directory with virtual environment activated
   streamlit run app.py
   ```

3. **Access the application**:
   - Open your browser and navigate to `http://localhost:8501`
   - The application will automatically open in your default browser

### Alternative Ports

If port 8501 is busy, Streamlit will automatically use the next available port (8502, 8503, etc.)

## 💡 How to Use SymptomAid

### Step-by-Step Guide

1. **📝 Enter Symptoms**:
   - Use the multi-line text area to describe your symptoms
   - Be specific about duration, severity, and associated factors
   - Example: "I've had a persistent headache for 3 days, along with sensitivity to light and nausea"

2. **🔍 Analyze Symptoms**:
   - Click the "🔍 Analyze Symptoms" button
   - Wait for the AI analysis (typically 10-30 seconds)
   - A loading spinner will indicate processing

3. **📊 Review Comprehensive Results**:
   - **Possible Causes**: Three potential medical causes with probability assessments
   - **Body Systems**: Detailed analysis of affected body systems
   - **Specialist Recommendations**: Primary and alternative healthcare providers
   - **Warning Signs**: Symptoms that require monitoring
   - **Emergency Triggers**: When to seek immediate medical attention
   - **Next Steps**: Actionable guidance for follow-up

4. **🔄 Reset or Analyze Again**:
   - Use the "Reset" button to clear the form
   - Enter new symptoms for additional analysis

### Best Practices

- **Be Descriptive**: Include timing, severity, location, and associated symptoms
- **Use Natural Language**: No need for medical terminology
- **Consider Context**: Mention recent activities, medications, or changes
- **Read Completely**: Review all sections of the analysis
- **Follow Disclaimers**: Always consult healthcare professionals for medical decisions

## 📊 Sample Output

**Input**: "I have been experiencing headaches, fatigue, and dizziness for the past 3 days"

**Output**:

## Possible Medical Causes:
- **Tension Headache**: Often caused by stress, poor posture, or muscle tension
- **Dehydration**: Can cause headaches, fatigue, and dizziness
- **Viral Infection**: Common cold or flu can present with these symptoms

## Affected Body Systems:
- **Nervous System**: Headaches and dizziness indicate potential neurological involvement
- **Cardiovascular System**: Fatigue and dizziness may suggest blood pressure or circulation issues

## Recommended Specialist:
- **Primary recommendation**: Primary Care Physician - Best starting point for general symptoms
- **Alternative**: Neurologist - If headaches persist or worsen

## Important Notes:
- Monitor for fever, severe headache, or vision changes
- Seek immediate attention if symptoms worsen rapidly

**DISCLAIMER: This is not medical advice. Always consult a licensed physician for proper diagnosis and treatment.**

## 🗂️ Project Structure

```
Symptoaid/
├── app.py                 # Main Streamlit application
├── ollama_helper.py       # Ollama API integration and LLM logic
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Configuration

You can modify the following settings in `ollama_helper.py`:

- `MODEL_NAME`: Change the Ollama model (default: "mistral")
- `REQUEST_TIMEOUT`: Adjust API timeout (default: 60 seconds)
- `OLLAMA_URL`: Change Ollama endpoint if needed

## 🔧 Troubleshooting

### Common Issues

1. **🔌 Connection Issues**:
   ```bash
   # Check if Ollama is running
   curl http://localhost:11434/api/tags
   
   # Restart Ollama if needed
   ollama serve
   ```

2. **🐌 Performance Issues**:
   - **RAM Requirements**: Ensure 8GB+ available RAM
   - **CPU Usage**: Close resource-intensive applications
   - **Model Size**: Mistral requires significant resources
   - **Network**: Ensure stable internet for initial model download

3. **📦 Model Issues**:
   ```bash
   # Verify installed models
   ollama list
   
   # Reinstall Mistral if needed
   ollama rm mistral
   ollama pull mistral
   ```

4. **🌐 Streamlit Issues**:
   ```bash
   # Update Streamlit
   pip install --upgrade streamlit
   
   # Clear Streamlit cache
   streamlit cache clear
   
   # Run on different port
   streamlit run app.py --server.port 8502
   ```

5. **🐍 Python Environment Issues**:
   ```bash
   # Recreate virtual environment
   deactivate
   rm -rf venv
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

### File Descriptions

- **`app.py`**: Core Streamlit application featuring professional UI, responsive design, and comprehensive user experience
- **`ollama_helper.py`**: Advanced LLM integration with sophisticated prompt engineering and safety mechanisms
- **`style.css`**: Professional CSS styling for enhanced visual appeal and user experience
- **`requirements.txt`**: Carefully curated Python dependencies with version specifications
- **Documentation**: Comprehensive guides for setup, usage, and troubleshooting

### Testing the Setup:

Run the helper module directly to test Ollama connection:
```bash
python ollama_helper.py
```

## 🔒 Security and Privacy

### Privacy-First Design
- **🏠 Local Processing**: All AI analysis happens locally on your machine
- **🚫 No Data Collection**: SymptomAid does not collect, store, or transmit personal health information
- **🔐 Privacy Protection**: Your symptom data never leaves your device
- **👁️ Full Transparency**: Open source code for complete visibility
- **🛡️ No Tracking**: No analytics, cookies, or user tracking

### Security Features
- **Input Validation**: Filters inappropriate or harmful content
- **Response Sanitization**: Ensures safe and appropriate AI responses
- **Local LLM**: No external API calls that could expose data
- **Secure Dependencies**: Regularly updated and vetted packages

## 🏥 Medical Safety

### Built-in Safety Mechanisms
- **Multiple Disclaimers**: Prominent warnings throughout the application
- **Emergency Guidance**: Clear instructions for urgent medical situations
- **Professional Emphasis**: Consistent reminders to consult healthcare providers
- **Educational Focus**: Designed to inform, not diagnose or treat

### Limitations
- **Not a Medical Device**: Not FDA approved or medically certified
- **Educational Only**: Cannot replace professional medical judgment
- **No Emergency Response**: Not suitable for urgent medical situations
- **General Information**: Cannot account for individual medical history

## 🚀 Performance Optimization

### System Requirements
- **Minimum**: 8GB RAM, 4-core CPU, 10GB free disk space
- **Recommended**: 16GB RAM, 8-core CPU, SSD storage
- **Network**: Required only for initial Ollama and model download

### Optimization Tips
- Close unnecessary applications during analysis
- Ensure adequate system cooling for sustained use
- Consider upgrading hardware for faster response times
- Monitor system resources during operation

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

### MIT License Summary
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❌ No warranty provided
- ❌ No liability assumed

## ⚖️ Legal Notice

**🚨 CRITICAL LEGAL DISCLAIMER 🚨**

**EDUCATIONAL PURPOSE ONLY**: This application is designed exclusively for educational and informational purposes. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment.

**PROFESSIONAL CONSULTATION REQUIRED**: Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read in this application.

**EMERGENCY SITUATIONS**: In case of a medical emergency, call your doctor or emergency services immediately. This application is not designed for emergency medical situations.

**NO WARRANTY**: The developers provide this software "as is" without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.

## 🤝 Contributing

### How to Contribute
1. **🍴 Fork the Repository**: Create your own copy
2. **🌿 Create a Branch**: `git checkout -b feature/amazing-feature`
3. **💻 Make Changes**: Implement your improvements
4. **✅ Test Thoroughly**: Ensure everything works correctly
5. **📝 Commit Changes**: `git commit -m 'Add amazing feature'`
6. **🚀 Push to Branch**: `git push origin feature/amazing-feature`
7. **🔄 Open Pull Request**: Submit your changes for review

### Contribution Guidelines
- Follow existing code style and conventions
- Add appropriate documentation for new features
- Include tests for new functionality
- Ensure medical safety and accuracy
- Maintain educational focus and disclaimers

### Areas for Contribution
- 🎨 UI/UX improvements
- 🧠 Enhanced prompt engineering
- 🔧 Performance optimizations
- 📚 Documentation improvements
- 🌐 Internationalization
- ♿ Accessibility enhancements

## 📞 Support

### Getting Help
- **📖 Documentation**: Check this README and other docs first
- **🐛 Issues**: Open a GitHub issue for bugs or feature requests
- **💬 Discussions**: Use GitHub Discussions for questions
- **📧 Contact**: Reach out to maintainers for urgent matters

### Reporting Issues
When reporting issues, please include:
- Operating system and version
- Python version
- Ollama version
- Error messages and logs
- Steps to reproduce the issue

---

**Built with ❤️ using Streamlit and Ollama**