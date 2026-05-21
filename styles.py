styles = """

<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

/* DESIGN TOKENS */
:root {
    --bg:             #080c14;
    --bg2:            #0c1220;
    --surface:        rgba(12, 20, 38, 0.85);
    --glass:          rgba(16, 28, 52, 0.6);
    --glass-border:   rgba(64, 160, 255, 0.12);
    --glass-border-h: rgba(64, 160, 255, 0.38);
    --muted:          rgba(100, 130, 180, 0.45);
    --text:           #c8d8f0;
    --text-dim:       #5a7099;
    --text-bright:    #e8f0ff;
    --cyan:           #64d2ff;
    --cyan-dim:       rgba(100, 210, 255, 0.18);
    --cyan-glow:      rgba(100, 210, 255, 0.35);
    --blue:           #3b82f6;
    --blue-dim:       rgba(59, 130, 246, 0.15);
    --user-bg:        rgba(29, 60, 110, 0.75);
    --user-border:    rgba(64, 130, 230, 0.3);
    --user-text:      #bdd5f8;
    --bot-bg:         rgba(12, 22, 44, 0.82);
    --bot-border:     rgba(64, 160, 255, 0.15);
    --error-bg:       rgba(30, 12, 12, 0.85);
    --error-border:   rgba(200, 60, 60, 0.3);
    --error-text:     #e08080;
    --radius-sm:      8px;
    --radius:         14px;
    --radius-lg:      20px;
    --font-head:      'Syne', sans-serif;
    --font-body:      'DM Sans', sans-serif;
    --ease:           cubic-bezier(0.4, 0, 0.2, 1);
    --transition:     0.22s cubic-bezier(0.4, 0, 0.2, 1);
}

/* RESET & BASE */

html, body {
    background: var(--bg) !important;
    font-family: var(--font-body);
    color: var(--text);
    -webkit-font-smoothing: antialiased;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main {
    background: var(--bg) !important;
}

[data-testid="stMainBlockContainer"] {
    max-width: 860px !important;
    padding: 0 24px 140px !important;   
    margin: 0 auto !important;
}

#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stBottom"] > div { display: none !important; }

/* AMBIENT BACKGROUND */

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 70% 50% at 80% -10%, rgba(59,130,246,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at -10% 60%, rgba(100,210,255,0.07) 0%, transparent 55%),
        radial-gradient(ellipse 40% 30% at 50% 100%, rgba(59,130,246,0.06) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}

[data-testid="stAppViewContainer"]::after {
    content: "";
    position: fixed;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(100,210,255,0.04) 0%, transparent 70%);
    top: -200px;
    right: -150px;
    pointer-events: none;
    z-index: 0;
    animation: ambientPulse 12s ease-in-out infinite;
}


/* PAGE HEADER */

.page-header {
    position: relative;
    padding: 36px 0 28px;
    margin-bottom: 8px;
    text-align: center;
}

.header-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(100, 210, 255, 0.08);
    border: 1px solid rgba(100, 210, 255, 0.2);
    border-radius: 100px;
    padding: 4px 12px 4px 8px;
    font-family: var(--font-head);
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    color: var(--cyan);
    margin-bottom: 16px;
    animation: fadeDown 0.6s var(--ease) both;
}

.badge-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--cyan);
    box-shadow: 0 0 8px var(--cyan);
    animation: blink 2s ease-in-out infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1;   }
    50%       { opacity: 0.3; }
}

.header-title {
    font-family: var(--font-head) !important;
    font-size: clamp(1.8rem, 4vw, 2.6rem) !important;
    font-weight: 800 !important;
    color: var(--text-bright) !important;
    letter-spacing: -0.02em !important;
    line-height: 1.1 !important;
    margin: 0 0 10px !important;
    animation: fadeDown 0.7s var(--ease) 0.1s both;
}

.title-accent {
    background: linear-gradient(135deg, var(--cyan) 0%, var(--blue) 60%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.header-sub {
    font-size: 0.85rem !important;
    color: var(--text-dim) !important;
    max-width: 480px;
    margin: 0 auto !important;
    line-height: 1.6 !important;
    animation: fadeDown 0.7s var(--ease) 0.2s both;
}

.header-glow {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--glass-border-h), transparent);
}

@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-12px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* SUGGESTION SECTION */

.sugg-section {
    animation: fadeUp 0.6s var(--ease) 0.3s both;
    margin-bottom: 4px;
}

.sugg-label {
    font-family: var(--font-head);
    font-size: 0.68rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    color: var(--text-dim) !important;
    margin-bottom: 12px !important;
    text-transform: uppercase;
}

.sug-btn [data-testid="stButton"] > button {
    background: var(--glass) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius) !important;
    color: var(--text-dim) !important;
    font-family: var(--font-body) !important;
    font-size: 0.8rem !important;
    font-weight: 400 !important;
    padding: 13px 16px !important;
    height: auto !important;
    text-align: left !important;
    white-space: normal !important;
    line-height: 1.45 !important;
    width: 100% !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.03) !important;
    transition: all var(--transition) !important;
    min-height: 62px !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

.sug-btn [data-testid="stButton"] > button:hover {
    border-color: var(--glass-border-h) !important;
    background: rgba(20, 38, 72, 0.82) !important;
    color: var(--text-bright) !important;
    transform: translateY(-3px) !important;
    box-shadow:
        0 0 0 1px rgba(100,210,255,0.12),
        0 8px 24px rgba(0,0,0,0.45),
        0 0 22px rgba(100,210,255,0.1) !important;
}

/* CHAT AREA */

.chat-area {
    display: flex;
    flex-direction: column;
    gap: 28px;          
    padding-bottom: 24px;
    animation: fadeUp 0.4s var(--ease);
    padding-bottom: 120px;

}



/* MESSAGE WRAPPERS */

.message-row {
    margin-bottom: 28px !important;
}

.msg-wrap {
    display: flex;
    flex-direction: column;
    animation: msgIn 0.32s cubic-bezier(0.16, 1, 0.3, 1) both;
    padding: 0 4px;
}

.msg-wrap.user { align-items: flex-end; }
.msg-wrap.bot  { align-items: flex-start; }

@keyframes msgIn {
    from { opacity: 0; transform: translateY(10px) scale(0.98); }
    to   { opacity: 1; transform: translateY(0)    scale(1);    }
}

.msg-meta {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 5px;
}

.user-meta { flex-direction: row-reverse; }

.msg-sender {
    font-family: var(--font-head);
    font-size: 0.63rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.user-sender { color: rgba(147, 197, 253, 0.7); }
.bot-sender  { color: var(--cyan); opacity: 0.8; }

.msg-time {
    font-size: 0.6rem;
    color: var(--muted);
    font-family: var(--font-body);
}

.bot-row {
    display: flex;
    align-items: flex-start;
    gap: 11px;
}

.bot-content {
    display: flex;
    flex-direction: column;
    flex: 1;
    min-width: 0;  
}

.bot-meta { padding-left: 2px; }

/* AVATAR */

.bot-avatar {
    width: 34px;
    height: 34px;
    border-radius: 10px;
    flex-shrink: 0;
    margin-top: 2px;
    border: 1px solid rgba(100, 210, 255, 0.22);
    box-shadow: 0 0 14px rgba(100, 210, 255, 0.12), 0 4px 12px rgba(0,0,0,0.4);
    
}

/* MSG BUBBLES */

.msg-bubble {
    padding: 13px 18px;
    font-size: 0.88rem;
    line-height: 1.7;
    word-break: break-word;
    position: relative;
}

.user-bubble {
    max-width: 72%;
    background: linear-gradient(135deg, rgba(29,60,120,0.9) 0%, rgba(20,45,90,0.85) 100%) !important;
    border: 1px solid var(--user-border) !important;
    border-radius: var(--radius) var(--radius-sm) var(--radius) var(--radius) !important;
    color: var(--user-text) !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06) !important;
    backdrop-filter: blur(10px);
}

.bot-bubble {
    width: 100%;
    background: var(--bot-bg) !important;
    border: 1px solid var(--bot-border) !important;
    border-radius: var(--radius-sm) var(--radius) var(--radius) var(--radius) !important;
    color: var(--text) !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.03) !important;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
}

.error-bubble {
    background: var(--error-bg) !important;
    border-color: var(--error-border) !important;
    color: var(--error-text) !important;
}

.bot-bubble::before {
    content: "";
    position: absolute;
    left: 0;
    top: 12px;
    bottom: 12px;
    width: 2px;
    background: linear-gradient(180deg, var(--cyan) 0%, var(--blue) 100%);
    border-radius: 2px;
    opacity: 0.45;
}

/* INPUT BAR */

.input-wrap {
    position: fixed !important;

    bottom: 0 !important;
    left: 0 !important;

    width: 100% !important;

    z-index: 99999 !important;

    background: rgba(8, 12, 20, 0.96) !important;

    backdrop-filter: blur(18px);

    border-top: 1px solid rgba(80,130,255,0.12);

    padding: 14px 24px !important;
}

.input-wrap form {
    max-width: 860px;
    margin: 0 auto;
}

[data-testid="stMainBlockContainer"] {
    max-width: 860px !important;
    margin: 0 auto !important;

    padding-top: 0 !important;
    padding-left: 24px !important;
    padding-right: 24px !important;

    padding-bottom: 90px !important;
}

.input-wrap .row-widget.stHorizontal{
    align-items: center !important;
}

.input-wrap::before{
    content:"";
    position:absolute;
    top:0;
    left:0;
    right:0;
    height:1px;

    background:linear-gradient(
        90deg,
        transparent,
        rgba(100,210,255,0.4),
        transparent
    );
}

[data-testid="stTextInput"] > label { display: none !important; }

[data-testid="stTextInput"] > div > div {
    background: var(--glass) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: var(--radius) !important;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.04) !important;
    transition: border-color var(--transition), box-shadow var(--transition) !important;
    backdrop-filter: blur(16px) !important;
}

[data-testid="stTextInput"] > div > div:focus-within {
    border-color: rgba(100, 210, 255, 0.42) !important;
    box-shadow:
        0 4px 24px rgba(0,0,0,0.4),
        0 0 0 3px rgba(100,210,255,0.07),
        0 0 22px rgba(100,210,255,0.12) !important;
}

[data-testid="stTextInput"] input {
    background: transparent !important;
    color: var(--text-bright) !important;
    font-family: var(--font-body) !important;
    font-size: 0.88rem !important;
    border: none !important;
    box-shadow: none !important;
    caret-color: var(--cyan) !important;
}

[data-testid="stTextInput"] input::placeholder {
    color: var(--text-dim) !important;
    font-style: italic;
}

/* SEND BUTTON */

[data-testid="stMainBlockContainer"] [data-testid="stButton"] > button {
    background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 60%, #1d4fcc 100%) !important;
    border: 1px solid rgba(100,210,255,0.2) !important;
    border-radius: var(--radius) !important;
    color: #fff !important;
    font-family: var(--font-head) !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em !important;
    padding: 8px 16px !important;
    height: 40px !important;
    width: 100% !important;
    box-shadow: 0 4px 16px rgba(29,78,216,0.35), inset 0 1px 0 rgba(255,255,255,0.15) !important;
    transition: all var(--transition) !important;
    white-space: nowrap !important;
    position: relative;
}

[data-testid="stMainBlockContainer"] [data-testid="stButton"] > button::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, transparent 60%);
    pointer-events: none;
}

[data-testid="stMainBlockContainer"] [data-testid="stButton"] > button:hover {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 26px rgba(37,99,235,0.52), 0 0 22px rgba(100,210,255,0.18) !important;
}

[data-testid="stMainBlockContainer"] [data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
}

/* SPINNER */
[data-testid="stSpinner"] { color: var(--cyan) !important; }

/* SCROLLBAR */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(100,130,180,0.2); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: rgba(100,210,255,0.32); }

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
    [data-testid="stMainBlockContainer"] {
        padding: 0 14px 140px !important;
    }
    .input-wrap { padding: 14px 14px 22px; }
    .user-bubble { max-width: 90%; }
    .header-title { font-size: 1.6rem !important; }
}

</style>
"""
