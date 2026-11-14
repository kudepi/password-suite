import streamlit as st
import random
import string
import math
import pandas as pd

# Sayfa Yapılandırması (Geniş Ekran Modu)
st.set_page_config(
    page_title="Cryptic OS // Enterprise Security Terminal", 
    page_icon="🛡️", 
    layout="wide"
)

# Profesyonel, Dolu Dolu ve Cyber-Security Tarzı Özel CSS Tasarımı (Minimalist değil, ağır ve teknik)
st.markdown("""
<style>
    .stApp { background-color: #07090e; color: #e2e8f0; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: #0b0f19; padding: 10px; border-radius: 8px; border: 1px solid #1e293b; }
    .stTabs [data-baseweb="tab"] { 
        height: 50px; 
        background-color: #111827; 
        border-radius: 6px; 
        font-weight: 600;
        color: #94a3b8;
        border: 1px solid #1f2937;
        padding-left: 25px;
        padding-right: 25px;
    }
    .stTabs [aria-selected="true"] { 
        background-color: #1d4ed8 !important; 
        color: #ffffff !important; 
        border-color: #3b82f6 !important;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.4);
    }
    .metric-box {
        background-color: #0f172a;
        border: 1px solid #334155;
        padding: 18px;
        border-radius: 8px;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Üst Bilgi Paneli
st.markdown("### 🛡️ CRYPTIC OS // ADVANCED CRYPTOGRAPHIC & SECURITY AUDIT TERMINAL")
st.markdown("Deep entropy calculation, multi-vector hash cracking simulation, algorithmic flaw detection, and high-entropy synthesis engine.")
st.divider()

# Ana Sekmeler
tab_audit, tab_generator, tab_matrix = st.tabs([
    "🔍 DEEP SECURITY & VULNERABILITY AUDITOR", 
    "⚙️ MASTER PASSWORD & PASSPHRASE SYNTHESIZER", 
    "📊 ALGORITHMIC CRACK TIME & ATTACK MATRIX"
])

# ==========================================
# SEKME 1: DERİN GÜVENLİK VE ZAFİYET ANALİZİ
# ==========================================
with tab_audit:
    col_input, col_info = st.columns([2, 1])
    
    with col_input:
        st.subheader("Target Password Inspection")
        password_input = st.text_input("Enter target password for full-spectrum audit:", type="password", placeholder="Type or paste complex string...")
        
    with col_info:
        st.info("💡 **Audit Mode:** Real-time Shannon entropy calculation combined with simulated multi-threaded GPU/ASIC brute-force vectors.")

    def run_deep_audit(pwd):
        if not pwd:
            return None
        
        length = len(pwd)
        has_lower = any(c.islower() for c in pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(c in string.punctuation for c in pwd)
        has_extended = any(ord(c) > 127 for c in pwd)
        
        # Karakter Havuzu Büyüklüğü
        pool = 0
        if has_lower: pool += 26
        if has_upper: pool += 26
        if has_digit: pool += 10
        if has_special: pool += len(string.punctuation)
        if has_extended: pool += 32
        
        if pool == 0:
            return {"score": 0, "entropy": 0, "rating": "INVALID"}

        # Entropi (Bits)
        entropy = length * math.log2(pool)
        
        # Kombinasyon ve Kırılma Süreleri (Farklı Donanımlar)
        total_combos = 2 ** entropy
        sec_online = total_combos / 100            # Ağ kısıtlı (100 istek/sn)
        sec_gpu_single = total_combos / 1e10       # Tekli RTX 4090 (10B hash/sn)
        sec_cluster = total_combos / 1e13          # Kurumsal GPU Farm (10T hash/sn)
        sec_asic = total_combos / 1e15             # Özel ASIC Rig (1P hash/sn)

        # Zafiyet / Kalıp Tespiti
        penalties = 0
        flaws = []
        
        # Ardışık karakterler (abc, 123 vb.)
        sequential = False
        for i in range(len(pwd) - 2):
            if ord(pwd[i]) + 1 == ord(pwd[i+1]) and ord(pwd[i+1]) + 1 == ord(pwd[i+2]):
                sequential = True
                penalties += 20
                flaws.append("Sequential sequence detected (e.g., 123 or abc)")
                break

        # Tekrarlayan karakterler
        repeating = any(pwd.count(c) > len(pwd) / 3 for c in set(pwd))
        if repeating:
            penalties += 15
            flaws.append("High repetition of specific characters")

        # Uzunluk kontrolü
        if length < 10:
            penalties += 30
            flaws.append("Critical: Length is below recommended 12-character threshold")
        elif length < 14:
            penalties += 10
            flaws.append("Warning: Length is moderate; 16+ recommended for high security")

        # Skor Hesaplama
        base_score = min(100, int((entropy / 100) * 100))
        final_score = max(0, base_score - penalties)

        if final_score < 30:
            rating, color_code = "CRITICAL VULNERABILITY", "red"
        elif final_score < 60:
            rating, color_code = "MODERATE RISK", "orange"
        elif final_score < 85:
            rating, color_code = "SECURE", "yellow"
        else:
            rating, color_code = "MILITARY GRADE RESISTANCE", "green"

        return {
            "length": length,
            "pool": pool,
            "entropy": round(entropy, 2),
            "score": final_score,
            "rating": rating,
            "flaws": flaws,
            "sec_online": sec_online,
            "sec_gpu": sec_gpu_single,
            "sec_cluster": sec_cluster,
            "sec_asic": sec_asic,
            "has_lower": has_lower,
            "has_upper": has_upper,
            "has_digit": has_digit,
            "has_special": has_special,
            "has_extended": has_extended
        }

    if password_input:
        res = run_deep_audit(password_input)
        
        if res:
            st.markdown("---")
            st.subheader("📊 Comprehensive Audit Metrics")
            
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.metric("Shannon Entropy", f"{res['entropy']} bits")
            with m2:
                st.metric("Security Index Score", f"{res['score']} / 100")
            with m3:
                st.metric("Estimated Strength", res['rating'])
            with m4:
                st.metric("Character Pool Size", f"{res['pool']} variations")
                
            st.progress(res['score'] / 100)
            
            # Detaylı Tablolar ve Matrisler
            col_left, col_right = st.columns(2)
            
            with col_left:
                st.markdown("#### 🔬 Detailed Vector Breakdown")
                st.markdown(f"""
                - **Total Length:** `{res['length']} characters`
                - **Lowercase Letters [a-z]:** `{'Present ✅' if res['has_lower'] else 'Missing ❌'}`
                - **Uppercase Letters [A-Z]:** `{'Present ✅' if res['has_upper'] else 'Missing ❌'}`
                - **Numeric Digits [0-9]:** `{'Present ✅' if res['has_digit'] else 'Missing ❌'}`
                - **Special Symbols [!@#$]:** `{'Present ✅' if res['has_special'] else 'Missing ❌'}`
                - **Extended Unicode / Symbols:** `{'Present ✅' if res['has_extended'] else 'None'}`
                """)
                
                st.markdown("#### 🚨 Vulnerabilities & Flaws Identified")
                if res['flaws']:
                    for flaw in res['flaws']:
                        st.warning(f"⚠️ {flaw}")
                else:
                    st.success("✅ No structural flaws or common pattern vulnerabilities detected.")

            with col_right:
                st.markdown("#### ⏱️ Brute-Force Crack Duration Matrix")
                
                def format_time(seconds):
                    if seconds < 1: return "Instantly (< 0.01 sec)"
                    elif seconds < 60: return f"{int(seconds)} Seconds"
                    elif seconds < 3600: return f"{int(seconds/60)} Minutes"
                    elif seconds < 86400: return f"{int(seconds/3600)} Hours"
                    elif seconds < 31536000: return f"{int(seconds/86400)} Days"
                    elif seconds < 31536000 * 1000: return f"{int(seconds/31536000)} Years"
                    else: return "Millennia (Practically Impossible)"

                st.markdown(f"""
                - **Online Throttled Attack (100 req/s):** `{format_time(res['sec_online'])}`
                - **Single Consumer GPU (RTX 4090):** `{format_time(res['sec_gpu'])}`
                - **Enterprise GPU Cluster (10T h/s):** `{format_time(res['sec_cluster'])}`
                - **Custom ASIC Rig (1P h/s):** `{format_time(res['sec_asic'])}`
                """)
                
                st.markdown("#### 🛠️ Actionable Hardening Recommendations")
                if res['score'] < 80:
                    st.markdown("""
                    1. **Increase Length:** Aim for a minimum of 16-20 characters.
                    2. **Diversify Pool:** Combine uppercase, lowercase, digits, and punctuation.
                    3. **Remove Predictability:** Avoid dictionary words, sequential numbers, or names.
                    """)
                else:
                    st.success("🛡️ Your password structure meets high enterprise compliance standards. Store it securely in a password manager.")

# ==========================================
# SEKME 2: GELİŞMİŞ ŞİFRE VE PAROLA ÜRETİCİSİ
# ==========================================
with tab_generator:
    st.subheader("Advanced Cryptographic Synthesis Engine")
    st.markdown("Configure enterprise-grade generation parameters, custom keywords, passphrases, and batch generation sets.")

    gen_mode = st.radio("Select Synthesis Mode:", ["Standard Character Randomizer", "Diceware / Memorable Passphrase", "Custom Pattern / Keyword Injector"], horizontal=True)
    st.divider()

    if gen_mode == "Standard Character Randomizer":
        g1, g2, g3 = st.columns(3)
        with g1:
            length = st.slider("Key Length (Characters)", min_value=8, max_value=128, value=24, step=1)
            batch_size = st.selectbox("Batch Generation Output Count", [1, 5, 10, 20], index=1)
        with g2:
            inc_upper = st.checkbox("Include Uppercase [A-Z]", value=True)
            inc_lower = st.checkbox("Include Lowercase [a-z]", value=True)
            inc_digits = st.checkbox("Include Digits [0-9]", value=True)
        with g3:
            inc_symbols = st.checkbox("Include Special Symbols [!@#$]", value=True)
            exclude_ambiguous = st.checkbox("Exclude Ambiguous Characters (l, I, O, 0)", value=True)
            force_all_types = st.checkbox("Enforce At Least 1 of Each Selected Set", value=True)

        if st.button("🚀 Synthesize Standard Keys", type="primary"):
            pool = ""
            if inc_lower: pool += string.ascii_lowercase
            if inc_upper: pool += string.ascii_uppercase
            if inc_digits: pool += string.digits
            if inc_symbols: pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            if exclude_ambiguous:
                for c in "lIO01": pool = pool.replace(c, "")
                
            if not pool:
                st.error("Error: Character pool is empty!")
            else:
                st.markdown("### Generated Cryptographic Keys")
                passwords = []
                for _ in range(batch_size):
                    if force_all_types and length >= 4:
                        pwd_chars = []
                        if inc_lower: pwd_chars.append(random.choice(string.ascii_lowercase))
                        if inc_upper: pwd_chars.append(random.choice(string.ascii_uppercase))
                        if inc_digits: pwd_chars.append(random.choice(string.digits))
                        if inc_symbols: pwd_chars.append(random.choice("!@#$%^&*"))
                        
                        remaining = length - len(pwd_chars)
                        pwd_chars.extend(random.choices(pool, k=remaining))
                        random.shuffle(pwd_chars)
                        pwd = "".join(pwd_chars)
                    else:
                        pwd = "".join(random.choices(pool, k=length))
                    passwords.append(pwd)
                    st.code(pwd, language="")

    elif gen_mode == "Diceware / Memorable Passphrase":
        p1, p2, p3 = st.columns(3)
        with p1:
            word_count = st.slider("Word Count in Passphrase", min_value=3, max_value=10, value=5)
        with p2:
            separator = st.selectbox("Word Separator", ["-", "_", ".", "@", "#", "Space"])
        with p3:
            add_number = st.checkbox("Append Random Suffix Number", value=True)
            capitalize_words = st.checkbox("Capitalize Word Initials", value=True)

        # Basit kelime listesi
        sample_words = ["cyber", "nexus", "quantum", "matrix", "vertex", "vector", "binary", "protocol", "firewall", "cipher", "packet", "kernel", "router", "daemon", "proxy", "shield", "crypt", "node", "entropy", "syntax"]

        if st.button("🚀 Synthesize Passphrase", type="primary"):
            selected_words = random.choices(sample_words, k=word_count)
            if capitalize_words:
                selected_words = [w.capitalize() for w in selected_words]
            
            sep = " " if separator == "Space" else separator
            passphrase = sep.join(selected_words)
            if add_number:
                passphrase += f"{sep}{random.randint(10, 999)}"
                
            st.markdown("### Generated Secure Passphrase")
            st.code(passphrase, language="")
            st.info(f"📏 Length: {len(passphrase)} characters | 🧠 High Memorable Index")

    else: # Custom Pattern / Keyword Injector
        c1, c2 = st.columns(2)
        with c1:
            keyword = st.text_input("Mandatory Keyword or Name Injection", placeholder="e.g., projectX")
            custom_len = st.slider("Total Target Length", min_value=12, max_value=64, value=20)
        with c2:
            position = st.selectbox("Keyword Placement", ["Start", "End", "Randomized Mix"])
            inject_symbols = st.checkbox("Surround with Complex Symbols", value=True)

        if st.button("🚀 Synthesize Custom Pattern", type="primary"):
            if not keyword:
                st.warning("Please enter a keyword to inject.")
            else:
                rem = max(4, custom_len - len(keyword))
                extra_pool = string.ascii_letters + string.digits + "!@#$%^&*"
                rand_part = "".join(random.choices(extra_pool, k=rem))
                
                if position == "Start":
                    res_pwd = keyword + ("!" if inject_symbols else "") + rand_part
                elif position == "End":
                    res_pwd = rand_part + ("!" if inject_symbols else "") + keyword
                else:
                    combined = list(keyword + rand_part)
                    random.shuffle(combined)
                    res_pwd = "".join(combined)[:custom_len]
                    
                st.markdown("### Synthesized Custom Key")
                st.code(res_pwd, language="")

# ==========================================
# SEKME 3: HASH & ALGORİTMA MATRİSİ
# ==========================================
with tab_matrix:
    st.subheader("📊 Hash Algorithm Comparison & Brute-Force Resistance Matrix")
    st.markdown("Technical breakdown of how modern hashing functions (MD5, SHA-256, Bcrypt, Argon2id) handle cracking workloads.")

    df_matrix = pd.DataFrame({
        "Algorithm / Function": ["MD5 (Legacy)", "SHA-256 (Standard)", "Bcrypt (Cost 12)", "Argon2id (Memory Hard)", "PBKDF2-HMAC-SHA256"],
        "Speed / Hashes per Sec (GPU)": ["~100 Billion / sec", "~10 Billion / sec", "~50,000 / sec", "~1,000 / sec (Memory bound)", "~20,000 / sec"],
        "Vulnerability to ASIC/GPU": ["Extreme High", "High", "Low (Memory Hard)", "Very Low (Resistant)", "Low (CPU/GPU balanced)"],
        "Recommended Use Case": ["Obsolete (Do Not Use)", "Checksums / Non-crypto", "Password Hashing", "Modern Enterprise Hashing", "Key Derivation / Compliance"]
    })

    st.dataframe(df_matrix, use_container_width=True)
    
    st.markdown("### 🔬 Cryptographic Formulas & Entropy Reference")
    st.markdown("""
    - **Shannon Entropy Formula:** $H = L \\times \\log_2(R)$ where $L$ is length and $R$ is radix (pool size).
    - **Key Space Growth:** Every additional character exponentially increases the computational work required for brute-force attacks.
    - **Salt & Pepper:** Enterprise systems must always incorporate cryptographic salts and pepper variables to nullify pre-computed rainbow table attacks.
    """)

st.divider()
st.caption("Cryptic OS Enterprise Edition • Secure Local Sandbox Execution Environment • v3.5.0")
