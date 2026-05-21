import html as _html
import streamlit as st
import time
import pytz
from styles import styles
from chatbot import get_response
from datetime import datetime


st.set_page_config(
    page_title="CareerBot — AI Career Assistant", page_icon="💼", layout="centered"
)

st.markdown(styles, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "_pending" not in st.session_state:
    st.session_state._pending = ""

# HEADER
st.markdown(
    """
    <div class="page-header">
        <div class="header-badge">
            <span class="badge-dot"></span>
            <span>AI ONLINE</span>
        </div>
        <h1 class="header-title">Career<span class="title-accent">&nbsp;Assistant</span></h1>
        <p class="header-sub">
            Powered by intelligent FAQ matching &mdash;
            ask me anything about placements, resumes &amp; interviews.
        </p>
        <div class="header-glow"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# SUGGESTIONS GRID
SUGGESTIONS = [
    ("📄", "How to write a strong resume?"),
    ("💡", "Tips for technical interviews"),
    ("🎓", "How to prepare for campus placement?"),
    ("✉️", "What should a cover letter include?"),
    ("💰", "How to negotiate a salary offer?"),
    ("🗣️", "How to improve communication skills?"),
]

if not st.session_state.messages:
    st.markdown(
        '<div class="sugg-section"><p class="sugg-label">✦ Suggested questions</p>',
        unsafe_allow_html=True,
    )
    cols = st.columns(2, gap="medium")
    for i, (icon, text) in enumerate(SUGGESTIONS):
        with cols[i % 2]:
            st.markdown('<div class="sug-btn">', unsafe_allow_html=True)
            if st.button(f"{icon}  {text}", key=f"sug_{i}"):
                st.session_state._pending = text
            st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div><br>", unsafe_allow_html=True)


# AVATAR
def _make_avatar(idx: int) -> str:
    """Return a self-contained SVG bot avatar with a unique gradient ID."""
    gid = f"ag{idx}"
    return f"""<svg class="bot-avatar" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="36" height="36" rx="10" fill="url(#{gid})"/>
  <rect x="10" y="8" width="16" height="12" rx="3"
        fill="rgba(255,255,255,0.15)" stroke="rgba(100,210,255,0.6)" stroke-width="1"/>
  <circle cx="14" cy="13" r="2" fill="#64d2ff"/>
  <circle cx="22" cy="13" r="2" fill="#64d2ff"/>
  <rect x="17" y="7" width="2" height="2" rx="1" fill="rgba(100,210,255,0.8)"/>
  <path d="M13 22 Q18 26 23 22"
        stroke="rgba(100,210,255,0.7)" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  <rect x="8"  y="12" width="2" height="6" rx="1" fill="rgba(100,210,255,0.4)"/>
  <rect x="26" y="12" width="2" height="6" rx="1" fill="rgba(100,210,255,0.4)"/>
  <defs>
    <linearGradient id="{gid}" x1="0" y1="0" x2="36" y2="36">
      <stop offset="0%"   stop-color="#0d1f3c"/>
      <stop offset="100%" stop-color="#0a2a4a"/>
    </linearGradient>
  </defs>
</svg>"""


# MESSAGES RENDERERS 
def _render_user_msg(content: str, ts: str) -> None:
    safe = _html.escape(content)  
    st.markdown(
        f"""<div class="msg-wrap user">
                <div class="msg-meta user-meta">
                    <span class="msg-sender user-sender">You</span>
                    <span class="msg-time">{ts}</span>
                </div>
                <div class="msg-bubble user-bubble">{safe}</div>
            </div>""",
        unsafe_allow_html=True,
    )


def _render_bot_msg(content: str, ts: str, is_err: bool, idx: int) -> None:
    safe = _html.escape(content) 
    bubble_cls = (
        "msg-bubble bot-bubble error-bubble" if is_err else "msg-bubble bot-bubble"
    )
    avatar = _make_avatar(idx)
    st.markdown(
        f"""<div class="message-row msg-wrap bot">
  <div class="bot-row">
    {avatar}
    <div class="bot-content">
      <div class="msg-meta bot-meta">
        <span class="msg-sender bot-sender">CareerBot</span>
        <span class="msg-time">{ts}</span>
      </div>
      <div class="{bubble_cls}">{safe}</div>
    </div>
  </div>
</div>""",
        unsafe_allow_html=True,
    )


# CHAT MESSAGES
if st.session_state.messages:
    st.markdown('<div class="chat-area">', unsafe_allow_html=True)
    bot_counter = 0
    for msg in st.session_state.messages:
        role = msg["role"]
        content = msg["content"]
        ts = msg.get("time", "")
        is_err = msg.get("is_error", False)

        if role == "user":
            _render_user_msg(content, ts)
        else:
            _render_bot_msg(content, ts, is_err, bot_counter)
            bot_counter += 1

    st.markdown("</div>", unsafe_allow_html=True)
    
#INPUT BAR
st.markdown('<div class="input-wrap">', unsafe_allow_html=True)
with st.form(key="chat_form", clear_on_submit=True, border=False):
    col_inp, col_btn = st.columns([6, 1], gap="small")
    with col_inp:
        user_input = st.text_input(
            "input",
            value=st.session_state._pending,
            placeholder="Ask about placements, interviews, resumes…",
            label_visibility="collapsed",
        )
    with col_btn:
        send = st.form_submit_button("Send →",use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# SEND HANDLE 
def handle_send(query: str) -> None:
    query = query.strip()
    if not query:
        return
    india = pytz.timezone("Asia/Kolkata")
    ts = datetime.now(india).strftime("%I:%M %p")
    st.session_state.messages.append({"role": "user", "content": query, "time": ts})
    with st.spinner("Thinking…"):
        time.sleep(0.4)
        response = get_response(query)
    is_error = response.lower().startswith("sorry")
    st.session_state.messages.append(
        {"role": "assistant", "content": response, "time": ts, "is_error": is_error}
    )
    st.session_state._pending = ""
    st.rerun()


if send and user_input.strip():
    handle_send(user_input)
elif st.session_state._pending:
    handle_send(st.session_state._pending)
