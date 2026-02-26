import os

# from dotenv import load_dotenv
# load_dotenv()
# api_key = os.getenv("GROQ_API_KEY")

from groq import Groq
import streamlit as st

api_key = st.secrets.get("GROQ_API_KEY")

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Naija cooks 🍳",
    page_icon="🍛",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Lora:ital,wght@0,400;0,500;1,400&display=swap');

/* ---- Root palette ---- */
:root {
    --clay:     #C2673A;
    --yam:      #E8A04B;
    --cream:    #FDF6EC;
    --bark:     #3B2A1A;
    --leaf:     #4A7C59;
    --smoke:    #F5EDE0;
}

/* ---- Global ---- */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--cream) !important;
    font-family: 'Lora', Georgia, serif;
    color: var(--bark);
}

/* ---- Hide default Streamlit chrome ---- */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

/* ---- Hero banner ---- */
.hero {
    background: linear-gradient(135deg, var(--clay) 0%, #008000 55%, var(--bark) 100%);
    border-radius: 20px;
    padding: 2.8rem 2rem 2.2rem;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(59,42,26,0.18);
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.hero-emoji { font-size: 3.2rem; display: block; margin-bottom: 0.4rem; }
.hero h1 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.6rem;
    font-weight: 900;
    color: #FDF6EC;
    margin: 0 0 0.5rem;
    letter-spacing: -0.5px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.25);
}
.hero p {
    color: rgba(253,246,236,0.82);
    font-style: italic;
    font-size: 1.05rem;
    margin: 0;
}

/* ---- Card ---- */
.card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(59,42,26,0.08);
    border: 1px solid rgba(194,103,58,0.12);
    margin-bottom: 1.5rem;
}

/* ---- Label tweak ---- */
label[data-testid="stTextAreaLabel"] p,
.stTextArea label {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: var(--bark) !important;
}

/* ---- Text area ---- */
textarea {
    border: 2px solid rgba(194,103,58,0.3) !important;
    border-radius: 12px !important;
    font-family: 'Lora', serif !important;
    font-size: 0.97rem !important;
    background: var(--smoke) !important;
    color: var(--bark) !important;
    transition: border-color 0.2s;
}
textarea:focus {
    border-color: var(--clay) !important;
    box-shadow: 0 0 0 3px rgba(194,103,58,0.15) !important;
}

/* ---- Button ---- */
.stButton > button {
    background: linear-gradient(135deg, var(--clay), #108000) !important;
    color: white !important;
    font-family: 'Playfair Display', serif !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.7rem 2.2rem !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 4px 14px rgba(194,103,58,0.4) !important;
    transition: all 0.25s ease !important;
    width: 100%;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #A0522D, var(--bark)) !important;
    box-shadow: 0 6px 20px rgba(194,103,58,0.5) !important;
    transform: translateY(-1px) !important;
}

/* ---- Recipe result card ---- */
.recipe-box {
    background: linear-gradient(160deg, #fffaf4 0%, #fff8f0 100%);
    border-left: 5px solid var(--clay);
    border-radius: 0 16px 16px 0;
    padding: 1.8rem 2rem;
    margin-top: 1.5rem;
    box-shadow: 0 4px 20px rgba(59,42,26,0.07);
}
.recipe-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--clay);
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.recipe-content {
    font-family: 'Lora', serif;
    font-size: 0.98rem;
    line-height: 1.6;
    color: var(--bark);
    /* white-space: pre-wrap; REMOVED to fix table spacing */
}

/* ---- Warning ---- */
.stAlert {
    border-radius: 12px !important;
    font-family: 'Lora', serif !important;
}

/* ---- Divider ---- */
hr { border-color: rgba(194,103,58,0.18) !important; margin: 1.5rem 0; }

/* ---- Tip strip ---- */
.tip-strip {
    background: var(--leaf);
    color: white;
    border-radius: 12px;
    padding: 0.9rem 1.3rem;
    font-size: 0.88rem;
    font-style: italic;
    margin-bottom: 1.5rem;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <span class="hero-emoji">🍛</span>
    <h1>Naija cooks</h1>
    <p>Your personal Nigerian kitchen guide.</p>
</div>
""", unsafe_allow_html=True)

# ── Tip strip ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="tip-strip">
    💡 Try entering ingredients like: <em>tatashe, onion, palm oil, goat meat, crayfish</em>
</div>
""", unsafe_allow_html=True)

# ── Input card ────────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)

ingredients = st.text_area(
    "🧺 What ingredients do you have?",
    placeholder="e.g. chicken, ugu leaves, ogiri, stockfish, onion, palm oil...",
    height=130,
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    suggest = st.button("✨ Suggest My Nigerian Recipe")

st.markdown('</div>', unsafe_allow_html=True)

# ── API call & result ─────────────────────────────────────────────────────────
if suggest:
    if ingredients.strip():
        client = Groq(api_key=api_key)

        with st.spinner("Naija cooks is thinking… 🔥"):
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": """You are Mama cooks, a warm and knowledgeable 
                        Nigerian chef with expertise in cuisines from across Nigeria — 
                        Yoruba, Igbo, Hausa, and Delta cooking traditions. 
                        
                        When given ingredients, you always:
                        - Suggest a Nigerian dish first before any other cuisine
                        - Use local ingredient names (e.g. tatashe not red bell pepper, 
                          iru not locust beans)
                        - Structure your response as: Dish Name, Ingredients with 
                          quantities, Step-by-step method, Cooking time, and one 
                          serving suggestion
                        - Write in a warm, encouraging tone like a trusted friend 
                          teaching you in their kitchen
                        - If the ingredients don't suggest a clear Nigerian dish, 
                          suggest the closest traditional equivalent"""
                    },
                    {
                        "role": "user",
                        "content": f"I have these ingredients: {ingredients}. What Nigerian dish can I make?"
                    }
                ]
            )

        recipe_text = response.choices[0].message.content

        # ── FIXED SPACING LOGIC ──────────────────────────────────────────
        # Opening the container
        st.markdown('<div class="recipe-box"><div class="recipe-header">🍽️ Naija cooks Says…</div><div class="recipe-content">', unsafe_allow_html=True)
        
        # Display the recipe (Streamlit's markdown handles tables and normal breaks perfectly)
        st.markdown(recipe_text)
        
        # Closing the container
        st.markdown('</div></div>', unsafe_allow_html=True)
        # ────────────────────────────────────────────────────────────────

    else:
        st.warning("⚠️ Please enter some ingredients before asking Naija cooks!")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#9B8070; font-size:0.82rem; font-style:italic;'>"
    "Made with ❤️ from group 3</p>",
    unsafe_allow_html=True
)
