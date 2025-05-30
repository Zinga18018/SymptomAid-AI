import streamlit as st
import requests
from ollama_helper import analyze_symptoms

# Page configuration
st.set_page_config(
    page_title="SYMPTOMAID - Professional AI Symptom Analysis",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS for professional look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .hero-title {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.3rem;
        font-weight: 400;
        margin-bottom: 0;
        letter-spacing: 0.5px;
    }
    
    .hero-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));
    }
    
    /* Warning Banner */
    .warning-banner {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        text-align: center;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);
        border: none;
    }
    
    /* Disclaimer Box */
    .disclaimer-box {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        border-left: 6px solid #e17055;
        box-shadow: 0 8px 25px rgba(253, 203, 110, 0.3);
    }
    
    /* Input Section */
    .input-section {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8eeff 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.1);
    }
    
    /* Results Container */
    .results-container {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.1);
    }
    
    /* Result Sections */
    .result-section {
        background: linear-gradient(135deg, #f1f3ff 0%, #e8eeff 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        border-left: 5px solid #667eea;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.1);
    }
    
    /* Emergency Section */
    .emergency-section {
        background: linear-gradient(135deg, #ffe8e8 0%, #ffcccc 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        border-left: 5px solid #ff6b6b;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.2);
    }
    
    /* Warning Box */
    .warning-box {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #f39c12;
        box-shadow: 0 6px 20px rgba(243, 156, 18, 0.2);
    }
    
    /* Emergency Box */
    .emergency-box {
        background: linear-gradient(135deg, #ffe8e8 0%, #ffcccc 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #e74c3c;
        box-shadow: 0 6px 20px rgba(231, 76, 60, 0.2);
    }
    
    /* Disclaimer Box Enhanced */
    .disclaimer-box-enhanced {
        background: linear-gradient(135deg, #e8f4fd 0%, #d1ecf1 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border-left: 5px solid #3498db;
        box-shadow: 0 8px 25px rgba(52, 152, 219, 0.2);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Final Disclaimer */
    .final-disclaimer {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8eeff 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
        border: 2px solid rgba(102, 126, 234, 0.2);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        font-size: 0.9rem;
        border-top: 1px solid #eee;
        margin-top: 3rem;
    }
    
    /* How to Use Section */
    .how-to-use {
        background: linear-gradient(135deg, #f1f8ff 0%, #e3f2fd 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border-left: 5px solid #2196f3;
        box-shadow: 0 8px 25px rgba(33, 150, 243, 0.1);
    }
    
    /* Text Area Styling */
    .stTextArea > div > div > textarea {
        border-radius: 12px;
        border: 2px solid rgba(102, 126, 234, 0.2);
        padding: 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8eeff 100%);
        border-radius: 12px;
        border: 1px solid rgba(102, 126, 234, 0.2);
        font-weight: 600;
    }
    
    /* Section Headers */
    .section-header {
        color: #2c3e50;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-icon">🏥</div>
    <h1 class="hero-title">SYMPTOMAID</h1>
    <p class="hero-subtitle">Professional AI-Powered Symptom Analysis</p>
</div>
""", unsafe_allow_html=True)

# Warning Banner
st.markdown("""
<div class="warning-banner">
    <strong>⚠️ MEDICAL DISCLAIMER:</strong> This tool is for educational purposes only. 
    Always consult healthcare professionals for medical advice.
</div>
""", unsafe_allow_html=True)

# Disclaimer Box
st.markdown("""
<div class="disclaimer-box">
    <h3>🔍 Important Information</h3>
    <p><strong>SymptomAid</strong> uses advanced AI to provide structured analysis of symptoms. 
    This tool is designed to help you organize your thoughts before consulting with healthcare professionals.</p>
    <ul>
        <li><strong>Not a substitute</strong> for professional medical diagnosis</li>
        <li><strong>Educational tool</strong> to help understand potential connections</li>
        <li><strong>Always seek professional help</strong> for health concerns</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# How to Use Section
with st.expander("📋 How to Use SymptomAid", expanded=False):
    st.markdown("""
    <div class="how-to-use">
        <h4>Step-by-Step Guide:</h4>
        <ol>
            <li><strong>Describe Your Symptoms:</strong> Be as specific as possible about what you're experiencing</li>
            <li><strong>Include Duration:</strong> Mention how long you've had these symptoms</li>
            <li><strong>Add Context:</strong> Include relevant medical history, medications, or recent changes</li>
            <li><strong>Review Results:</strong> Carefully read the AI analysis and recommendations</li>
            <li><strong>Consult Professionals:</strong> Use this information to have informed discussions with healthcare providers</li>
        </ol>
        
        <h4>Example Input:</h4>
        <p><em>"I've been experiencing persistent headaches for the past week, mainly in the morning. 
        I also feel nauseous and have been more sensitive to light than usual. I'm a 28-year-old female 
        with no significant medical history."</em></p>
    </div>
    """, unsafe_allow_html=True)

# Main Input Section
st.markdown("""
<div class="input-section">
    <h2 class="section-header">Describe Your Symptoms</h2>
</div>
""", unsafe_allow_html=True)

symptoms = st.text_area(
    "Please describe your symptoms in detail:",
    height=150,
    placeholder="Example: I've been experiencing persistent headaches for 3 days, along with fatigue and mild fever. The headaches are worse in the morning and I feel dizzy when standing up quickly...",
    help="Be as specific as possible. Include duration, severity, triggers, and any other relevant details."
)

# Analysis Button
if st.button("🔍 Analyze Symptoms", type="primary"):
    if symptoms.strip():
        with st.spinner("🤖 AI is analyzing your symptoms..."):
            try:
                analysis = analyze_symptoms(symptoms)
                if analysis:
                    display_analysis_results(analysis)
                else:
                    st.error("❌ Unable to analyze symptoms. Please try again or check your Ollama setup.")
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
    else:
        st.warning("⚠️ Please describe your symptoms before analyzing.")

def display_analysis_results(analysis):
    """Display the analysis results in a structured format"""
    
    st.markdown("""
    <div class="results-container">
        <h2 class="section-header">AI Analysis Results</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Parse the analysis text into sections
    sections = {
        'Possible Medical Causes': '',
        'Affected Body Systems': '',
        'Recommended Medical Specialist': '',
        'Warning Signs to Monitor': '',
        'Seek Emergency Care If': '',
        'Next Steps': ''
    }
    
    current_section = None
    lines = analysis.split('\n')
    
    for line in lines:
        line = line.strip()
        if any(section in line for section in sections.keys()):
            for section in sections.keys():
                if section in line:
                    current_section = section
                    break
        elif current_section and line:
            sections[current_section] += line + '\n'
    
    # Display each section
    for section_title, content in sections.items():
        if content.strip():
            if 'Emergency' in section_title or 'Warning' in section_title:
                st.markdown(f"""
                <div class="emergency-section">
                    <h3>🚨 {section_title}</h3>
                    <div>{content.strip()}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-section">
                    <h3>📋 {section_title}</h3>
                    <div>{content.strip()}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Emergency Warning
    st.markdown("""
    <div class="emergency-box">
        <h3>🚨 Emergency Warning</h3>
        <p><strong>Seek immediate medical attention if you experience:</strong></p>
        <ul>
            <li>Severe chest pain or difficulty breathing</li>
            <li>Signs of stroke (sudden weakness, speech problems, facial drooping)</li>
            <li>Severe allergic reactions</li>
            <li>Loss of consciousness or severe confusion</li>
            <li>Severe bleeding or trauma</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Disclaimer
    st.markdown("""
    <div class="disclaimer-box-enhanced">
        <h3>📋 Important Disclaimer</h3>
        <p>This AI analysis is for <strong>educational purposes only</strong> and should not replace professional medical advice, 
        diagnosis, or treatment. Always consult with qualified healthcare professionals for proper medical evaluation.</p>
    </div>
    """, unsafe_allow_html=True)

# Final Disclaimer
st.markdown("""
<div class="final-disclaimer">
    <h3>🏥 Professional Medical Consultation Required</h3>
    <p>This tool provides educational information only. For accurate diagnosis and treatment, 
    please consult with licensed healthcare professionals who can properly evaluate your condition.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>SymptomAid v2.0 | Powered by Ollama AI | For Educational Use Only</p>
    <p>Always prioritize professional medical advice over AI-generated content</p>
</div>
""", unsafe_allow_html=True)
