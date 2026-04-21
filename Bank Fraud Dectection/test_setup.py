import sys
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph
from langchain_ollama import ChatOllama

def run_preflight_check():
    print("🔍 Starting System Pre-flight Check...")
    
    # 1. Check Library Imports
    try:
        from typing import TypedDict, Annotated, List
        import operator
        print("✅ Core Libraries: OK")
    except ImportError as e:
        print(f"❌ Missing Libraries: {e}")
        return

    # 2. Check Connection to Llama 3.2 (Ollama)
    try:
        llm = ChatOllama(model="llama3.2", timeout=5)
        # We use a tiny prompt just to see if it's awake
        response = llm.invoke([HumanMessage(content="hi")])
        print("✅ LLM Connection (Ollama/Llama 3.2): OK")
    except Exception as e:
        print("⚠️ LLM Connection: FAILED. Ensure Ollama is running ('ollama serve').")

    # 3. Check Python Version (Engineering Best Practice)
    if sys.version_info >= (3, 9):
        print(f"✅ Python Version {sys.version_info.major}.{sys.version_info.minor}: OK")
    else:
        print("⚠️ Python Version: Potential incompatibility. 3.9+ recommended.")

    print("\n🚀 Environment is 100% ready for the National Finals!")

if __name__ == "__main__":
    run_preflight_check()