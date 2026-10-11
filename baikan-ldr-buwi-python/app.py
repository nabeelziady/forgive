import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# ============================================================
# EDIT BAGIAN INI SAJA UNTUK MENGGANTI KATA-KATA WEBSITE
# Kamu bisa mengganti teks di antara tanda kutip.
# ============================================================

NAMA_PANGGILAN = "Buwi"
JUDUL = "A little letter for us ♡"
SUBJUDUL = "someone who i adore the most."

PEMBUKA_SURAT = """
Dear buwi,
I made this little thing for you, not just because i only seek for your forgiveness. 
I'm sorry. Even after i do my best, i'm still not enough to treat you right, it's always been my biggest ick too to make you feel this way.
"""

ISI_SURAT = """
I'm sorry, i thought i managed to do it right, i thought i really get better, i really thought so. But still, i cant make it 0% to ever happen again.

I wont get defensive on myself. I really wanna be the best for you, not anybody else. It's just i always try my best even until now, to make everything set.

I really hope, that you'd stay with me. Choose me. Believe in me again. Thought i may be failed many times already. I know it's really tiring for you too, but trust me that it's tiring for me too. Yet[...]
"""

PENUTUP_SURAT = """
Aku ga berharap that this page would just fix everything or you forgive me after this.
I just want you to know again, that i would never ever give up on us, As i said it thousand times.

If you're ready, let's talk about it again, about how we should manage, how we should fix, and how we get better.

Thank you for reading my words.
With Love,
Buyi ♡
def
"""

KENANGAN = [
    {
        "tanggal": "[5th of September 2026]",
        "judul": "[Foto PAS]",
        "cerita": "[It was so cute. We look so adore together]",
        "foto": "buwi3.jpeg",
    },
    {
        "tanggal": "[23rd of July 2026]",
        "judul": "[Obihiro Things]",
        "cerita": "[let's eat obihiro together again.]",
        "foto": "buwi1.jpeg",
    },
    {
        "tanggal": "[11th of May 2026]",
        "judul": "[TSB Date]",
        "cerita": "[Let's go to more theme park we could go.]",
        "foto": "buwi2.jpeg",
    },
]

AJAKAN_BAIKAN = "Let's do everything together again, shall we?"
PESAN_TOMBOL = "Yes ♡"

# ============================================================
# BAGIAN TAMPILAN - tidak perlu diubah untuk mengganti pesan.
# ============================================================


def resolve_photo_path(filename: str) -> Path:
    base_dir = Path(__file__).resolve().parent
    candidates = [
        base_dir / filename,
        base_dir / "images" / filename,
        Path(filename),
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return candidates[0]


st.set_page_config(
    page_title=JUDUL,
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Playfair+Display:wght@500;600&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.stApp {
  background: linear-gradient(180deg, #fff7f7 0%, #fffaf0 48%, #fff2f5 100%);
  color: #5e4550;
}
.block-container { max-width: 760px; padding-top: 2rem; padding-bottom: 3rem; }
.hero {
  background: rgba(255,255,255,.86); border: 1px solid #f4dce4;
  border-radius: 28px; padding: 2rem 1.4rem; text-align: center;
  box-shadow: 0 12px 35px rgba(183, 112, 140, .10);
}
.kicker { color: #b96f8b; font-weight: 800; letter-spacing: 2px; font-size: .8rem; }
h1 { font-family: 'Playfair Display', serif !important; color: #92546c !important; }
h2, h3 { color: #92546c !important; }
.chibi { font-size: 3rem; margin: .4rem 0; }
.card {
  background: rgba(255,255,255,.9); border: 1px solid #f2dce4;
  border-radius: 20px; padding: 1.2rem 1.3rem; margin: .8rem 0;
  box-shadow: 0 7px 22px rgba(183, 112, 140, .07);
}
.date { color: #b96f8b; font-size: .86rem; font-weight: 800; }
.small-note { color: #8d7881; font-size: .9rem; }
div.stButton > button {
  border-radius: 999px; border: 1px solid #e6b8ca;
  background: #f7dce6; color: #78485d; font-weight: 800;
  padding: .65rem 1.2rem;
}
div.stButton > button:hover { background: #f2c8d8; color: #67374c; border-color: #dca1b9; }
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
  <div class="kicker">A LITTLE NOTE FOR YOU</div>
  <div class="chibi">🐰 💌 🐱</div>
  <h1>{JUDUL}</h1>
  <p>{SUBJUDUL}</p>
  <p class="small-note">Specially Made for {NAMA_PANGGILAN} ♡</p>
</div>
""", unsafe_allow_html=True)

st.write("")
with st.expander("💌 Click Here to Open", expanded=False):
    st.markdown(f'<div class="card">{PEMBUKA_SURAT.replace(chr(10), "<br>")}<br><br>{ISI_SURAT.replace(chr(10), "<br>")}<br><br>{PENUTUP_SURAT.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

st.write("")
st.markdown("## 📸 Pieces of Us")
st.caption("Just some cute memories of us.")
cols = st.columns(3)
for i, item in enumerate(KENANGAN):
    with cols[i]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        photo_path = resolve_photo_path(item["foto"])
        if photo_path.exists():
            st.image(str(photo_path), use_container_width=True)
        else:
            st.markdown("<div style='font-size:2.4rem;text-align:center;padding:1rem 0'>📷🌷</div>", unsafe_allow_html=True)
            st.caption("Foto bisa ditambahkan")
        st.markdown(f'<div class="date">{item["tanggal"]}</div>', unsafe_allow_html=True)
        st.markdown(f'**{item["judul"]}**')
        st.write(item["cerita"])
        st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.markdown("## 🧸 Let's Do It Slowly")
st.markdown(f'<div class="card" style="text-align:center"><div style="font-size:2.2rem">🐰 🤍 🐱</div><h3>{AJAKAN_BAIKAN}</h3><p class="small-note">You can take your time to respond.</p></div>', unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  * {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    font-family: 'Nunito', sans-serif;
    background: transparent;
  }

  .button-area {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
}

#result {
  display: block;
  min-height: 65px;
  padding: 16px 8px;
  text-align: center;
  color: #92546c;
  font-size: 16px;
  font-weight: 800;
  line-height: 1.6;
  overflow-wrap: break-word;
}

  .choice {
    position: absolute;
    border: 1px solid #e6b8ca;
    border-radius: 999px;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: 800;
    cursor: pointer;
    white-space: nowrap;
  }

  #yes {
    left: 18%;
    top: 35px;
    background: #f7dce6;
    color: #78485d;
  }

  #no {
    left: 57%;
    top: 35px;
    background: #fff;
    color: #78485d;
    transition: left 0.12s ease, top 0.12s ease;
  }

  #result {
    text-align: center;
    color: #92546c;
    font-size: 16px;
    font-weight: bold;
    padding-top: 10px;
  }
</style>
</head>

<body>
  <div class="button-area" id="area">
    <button class="choice" id="yes">💗 Yes ♡</button>
    <button class="choice" id="no">No..</button>
  </div>

  <div id="result"></div>

<script>
  const area = document.getElementById("area");
  const no = document.getElementById("no");
  const yes = document.getElementById("yes");
  const result = document.getElementById("result");

  function moveNo() {
    const maxX = area.clientWidth - no.offsetWidth;
    const maxY = area.clientHeight - no.offsetHeight;

    const x = Math.random() * Math.max(0, maxX);
    const y = Math.random() * Math.max(0, maxY);

    no.style.left = x + "px";
    no.style.top = y + "px";
  }

  // Tombol No kabur saat kursor mendekat.
  no.addEventListener("pointerenter", moveNo);

  // Jika tetap dicoba ditekan, tombol berpindah lagi.
  no.addEventListener("click", function(event) {
    event.preventDefault();
    moveNo();
  });

  // Tombol Yes menampilkan pesan ketika dipilih.
  yes.addEventListener("click", function() {
    result.textContent =
      "Thank you, Buwi 🥹💗 Let's talk and fix things together.";
    yes.textContent = "💖 Yeay!";
  });
</script>
</body>
</html>
""", height=270, scrolling=False)

st.write("")
st.caption("Made With Love. ♡")
