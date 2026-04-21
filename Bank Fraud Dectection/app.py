import streamlit as st
from langchain_core.messages import HumanMessage

# Initialize session state for the Ledger at the very top
if "demo_log" not in st.session_state:
    st.session_state.demo_log = []

# Try to import graph logic
try:
    from graph_logic import graph
except ImportError as e:
    st.error(f"⚠️ Critical Error: graph_logic.py not found or contains errors: {e}")
    st.stop()

# 1. Page Configuration
st.set_page_config(page_title="AI Sentinel | Fraud Engine", page_icon="🛡️", layout="wide")

# 2. Sidebar Branding
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=60)
    st.title("AI Sentinel")
    st.markdown("### National Hackathon 2026")
    st.info("System Status: **Live & Operational**")
    st.divider()
    
    st.subheader("🛠️ Control Panel")
    if st.button("🔄 Reset Session", use_container_width=True):
        st.session_state.demo_log = []
        st.rerun()
    
    st.divider()
    st.markdown("**Core Tech Stack:**\n- LangGraph (Agentic Orchestration)\n- Llama 3.2 (Reasoning)\n- RAG (Behavioral Context)")

# 3. Main Interface Header
st.title("🛡️ Fraud Detection & Behavioral Analytics")
st.markdown("##### Agentic RAG System for Real-Time Transaction Verification")

# 4. User Input Area
user_input = st.text_area("Input Transaction Stream:", height=100, 
                          placeholder="Example: User 405 is sending ₹15,000 using a VPN...")

# 5. Execution Logic
if st.button("🚀 Execute Forensic Analysis", type="primary", use_container_width=True):
    if not user_input:
        st.warning("Please enter transaction details to analyze.")
    else:
        try:
            with st.status("🕵️ Investigating Transaction Patterns...", expanded=True) as status:
                st.write("Fetching behavioral profile from vector database...")
                # Running the graph logic
                final_state = graph.invoke({"messages": [HumanMessage(content=user_input)]})
                st.write("Calculating multi-factor risk weights...")
                status.update(label="Analysis Complete", state="complete", expanded=False)

            # Extract data from state
            score = final_state.get("risk_score", 0.0)
            verdict_msg = final_state["messages"][-1].content
            history = final_state.get("user_history", {})

            # --- UPDATE LEDGER HISTORY ---
            st.session_state.demo_log.insert(0, {
                "Timestamp": "Live",
                "Transaction": user_input[:60] + "...", 
                "Risk %": f"{int(score*100)}%", 
                "Status": "✅ APPROVED" if score < 0.2 else "⚠️ REVIEW" if score < 0.9 else "❌ BLOCKED"
            })

            # 6. Dashboard Results
            st.markdown("---")
            col1, col2, col3 = st.columns([1.5, 1, 1.5])

            with col1:
                st.subheader("Decision Result")
                if score < 0.2:
                    st.success(verdict_msg)
                elif score >= 0.8:
                    st.error(verdict_msg)
                else:
                    st.warning(verdict_msg)
                
            with col2:
                st.subheader("Risk Metrics")
                st.metric("Probability", f"{int(score*100)}%", 
                          delta="HIGH RISK" if score >= 0.8 else "STABLE", 
                          delta_color="inverse" if score >= 0.8 else "normal")

            with col3:
                st.subheader("User Context")
                with st.expander("View Retrieved Profile"):
                    st.json(history.get("profile", {}))

            # 7. Technical Deep-Dive Tabs
            tab1, tab2 = st.tabs(["🧠 Agent Reasoning", "📊 System State"])
            with tab1:
                with tab1:
                 st.markdown("#### Logic Verification")
                # 1. Keep your checkboxes for a quick visual overview
                st.checkbox("Geographic Anomaly", value=(score >= 0.3), disabled=True)
                st.checkbox("Monetary Deviation", value=(score >= 0.6), disabled=True)
                st.checkbox("Technical Red-Flag", value=("VPN" in user_input.upper()), disabled=True)

                st.divider()

                # 2. THE WINNER FEATURE: Show the actual Agent Thinking
                st.markdown("#### 🧠 Multi-Agent Reasoning Trace")
                trace = final_state.get("reasoning", [])
                if trace:
                    for item in trace:
                        # Displays each agent's finding in a nice callout box
                        if "✅" in item:
                            st.success(item)
                        elif "ℹ️" in item:
                            st.info(item)
                        else:
                            st.warning(item)
                else:
                    st.write("No reasoning trace generated.")
            with tab2:
                st.write("Full State Object (JSON):")
                st.json({k: v for k, v in final_state.items() if k != "messages"})

        except Exception as e:
            st.error(f"Execution Error: {e}")

# 8. LIVE TRANSACTION LEDGER (The Winner Feature)
if st.session_state.demo_log:
    st.divider()
    st.subheader("📜 Live Transaction Ledger")
    st.dataframe(st.session_state.demo_log, use_container_width=True)

st.divider()
st.caption("© 2026 AI Sentinel | Developed for National Technology Hackathon | Team FinArch")

