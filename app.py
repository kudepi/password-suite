import streamlit as st
import random
import string
import math
import pandas as pd
import hashlib
import os
import secrets
import base64

# Page Configuration (Wide Layout)
st.set_page_config(
    page_title="Cryptic Core // Enterprise Intelligence Platform", 
    page_icon=None, 
    layout="wide"
)

# Professional, Zero-Emoji, Heavy-Duty Cyber-Security CSS Styling
st.markdown("""
<style>
    .stApp { background-color: #06080f; color: #e2e8f0; font-family: 'Courier New', Courier, monospace; }
    .stTabs [data-baseweb="tab-list"] { gap: 6px; background-color: #090d16; padding: 8px; border-radius: 4px; border: 1px solid #1e293b; }
    .stTabs [data-baseweb="tab"] { 
        height: 48px; 
        background-color: #0f172a; 
        border-radius: 4px; 
        font-weight: 700;
        font-size: 13px;
        color: #64748b;
        border: 1px solid #1e293b;
        padding-left: 20px;
        padding-right: 20px;
        letter-spacing: 1px;
    }
    .stTabs [aria-selected="true"] { 
        background-color: #0284c7 !important; 
        color: #ffffff !important; 
        border-color: #38bdf8 !important;
        box-shadow: inset 0 0 10px rgba(56, 189, 248, 0.3);
    }
    div[data-testid="stMetricValue"] { font-size: 20px; color: #38bdf8; font-weight: bold; }
    .terminal-box {
        background-color: #0b1120;
        border: 1px solid #334155;
        padding: 16px;
        border-radius: 4px;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# Top Header Console
st.markdown("## [ SYSTEM INTERFACE: CRYPTIC CORE v5.2 ]")
st.markdown("Advanced Cryptographic Intelligence, Multi-Vector Vulnerability Auditor, and High-Entropy Key Synthesis Terminal.")
st.markdown("---")

# Main Navigation Tabs
tab_audit, tab_generator, tab_matrix = st.tabs([
    "DEEP SECURITY & VULNERABILITY AUDITOR", 
    "ADVANCED KEY & PASSPHRASE SYNTHESIZER", 
    "ALGORITHMIC COMPLIANCE & ATTACK MATRIX"
])

# ==========================================
# TAB 1: DEEP SECURITY & VULNERABILITY AUDITOR
# ==========================================
with tab_audit:
    st.markdown("### TARGET PASSWORD ANALYSIS TERMINAL")
    col_input, col_meta = st.columns([2, 1])
    
    with col_input:
        password_input = st.text_input("Enter Target Password for Audit:", type="password", placeholder="Type or paste password string here...")
    with col_meta:
        st.markdown("**Scan Mode:** Full-Spectrum Entropy & Vulnerability Assessment")

    def run_advanced_audit(pwd):
        if not pwd:
            return None
        
        length = len(pwd)
        has_lower = any(c.islower() for c in pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(c in string.punctuation for c in pwd)
        has_extended = any(ord(c) > 127 for c in pwd)
        
        # Character Pool Calculation
        pool = 0
        if has_lower: pool += 26
        if has_upper: pool += 26
        if has_digit: pool += 10
        if has_special: pool += len(string.punctuation)
        if has_extended: pool += 32
        
        if pool == 0:
            return {"score": 0, "entropy": 0, "status": "INVALID"}

        # Shannon Entropy (Bits)
        entropy = length * math.log2(pool)
        
        # Hash Simulation (MD5 / SHA256)
        md5_hash = hashlib.md5(pwd.encode()).hexdigest()
        sha256_hash = hashlib.sha256(pwd.encode()).hexdigest()
        
        # Crack Times (Overflow-protected secure logarithmic calculation)
        try:
            sec_online = (2 ** entropy) / 100
            sec_cpu = (2 ** entropy) / 1e7
            sec_gpu = (2 ** entropy) / 1e10
            sec_cluster = (2 ** entropy) / 1e13
            sec_asic = (2 ** entropy) / 1e15
        except OverflowError:
            sec_online = float('inf')
            sec_cpu = float('inf')
            sec_gpu = float('inf')
            sec_cluster = float('inf')
            sec_asic = float('inf')

        # Advanced Vulnerability & Pattern Detection
        penalties = 0
        flaws = []
        
        # Keyboard Walks Check
        keyboard_walks = ["qwerty", "asdfgh", "zxcvbn", "123456", "qazwsx", "123321", "password", "admin", "letmein"]
        if any(walk in pwd.lower() for walk in keyboard_walks):
            penalties += 35
            flaws.append("Critical: Common keyboard walk or dictionary-based weak pattern detected.")

        # Sequential Characters Check
        sequential_count = 0
        for i in range(len(pwd) - 2):
            if ord(pwd[i]) + 1 == ord(pwd[i+1]) and ord(pwd[i+1]) + 1 == ord(pwd[i+2]):
                sequential_count += 1
        if sequential_count > 0:
            penalties += 15 * sequential_count
            flaws.append(f"Warning: {sequential_count} sequential character sequence(s) (e.g., 123, abc) detected.")

        # Repetitive Characters Check
        max_rep = max([pwd.count(c) for c in set(pwd)]) if pwd else 0
        if max_rep > length / 3 and length > 4:
            penalties += 20
            flaws.append("Warning: Excessive repetition of specific characters degrades entropy.")

        # Length Inspection
        if length < 12:
            penalties += 25
            flaws.append("Critical: Length is below the 12-character threshold. Minimum 16 is recommended.")

        # Leet-speak Detection
        leet_map = {'3': 'e', '4': 'a', '1': 'i', '0': 'o', '!': 'i', '$': 's'}
        leet_score = sum(1 for char in pwd if char in leet_map)
        if leet_score > 0 and length < 10:
            penalties += 15
            flaws.append("Notice: Shallow Leet-speak substitution used; vulnerable to advanced dictionary attacks.")

        # Final Score Calculation
        base_score = min(100, int((entropy / 110) * 100))
        final_score = max(0, base_score - penalties)

        if final_score < 35:
            rating = "CRITICAL VULNERABILITY LEVEL"
        elif final_score < 65:
            rating = "MODERATE RISK PROFILE"
        elif final_score < 85:
            rating = "SECURE STRUCTURING"
        else:
            rating = "MILITARY-GRADE RESISTANCE"

        return {
            "length": length,
            "pool": pool,
            "entropy": round(entropy, 2),
            "score": final_score,
            "rating": rating,
            "flaws": flaws,
            "md5": md5_hash,
            "sha256": sha256_hash,
            "sec_online": sec_online,
            "sec_cpu": sec_cpu,
            "sec_gpu": sec_gpu,
            "sec_cluster": sec_cluster,
            "sec_asic": sec_asic,
            "has_lower": has_lower,
            "has_upper": has_upper,
            "has_digit": has_digit,
            "has_special": has_special,
            "has_extended": has_extended
        }

    if password_input:
        res = run_advanced_audit(password_input)
        
        if res:
            st.markdown("---")
            st.markdown("### AUDIT METRICS & SCORES")
            
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.metric("Shannon Entropy", f"{res['entropy']} bits")
            with m2:
                st.metric("Security Index", f"{res['score']} / 100")
            with m3:
                st.metric("Status Evaluation", res['rating'])
            with m4:
                st.metric("Character Pool Size", f"{res['pool']} variations")
                
            st.progress(res['score'] / 100)
            
            st.markdown("---")
            col_det1, col_det2 = st.columns(2)
            
            with col_det1:
                st.markdown("#### STRUCTURAL & HASH ANALYSIS")
                st.markdown(f"""
                - **String Length:** `{res['length']} units`
                - **Lowercase Letters [a-z]:** `{'Present' if res['has_lower'] else 'Missing'}`
                - **Uppercase Letters [A-Z]:** `{'Present' if res['has_upper'] else 'Missing'}`
                - **Numeric Digits [0-9]:** `{'Present' if res['has_digit'] else 'Missing'}`
                - **Special Symbols [!@#$]:** `{'Present' if res['has_special'] else 'Missing'}`
                - **Extended Unicode:** `{'Present' if res['has_extended'] else 'None'}`
                - **MD5 Hash Digest:** `{res['md5']}`
                - **SHA-256 Hash Digest:** `{res['sha256']}`
                """)
                
                st.markdown("#### DETECTED VULNERABILITIES & RISKS")
                if res['flaws']:
                    for flaw in res['flaws']:
                        st.warning(f"[!] {flaw}")
                else:
                    st.success("[+] No known pattern-based flaws or sequential sequences detected.")

            with col_det2:
                st.markdown("#### CALCULATED BRUTE-FORCE CRACK TIMELINE")
                
                def format_time(seconds):
                    if seconds == float('inf'): return "Millennia (Practically Impossible)"
                    if seconds < 0.01: return "Instantly (< 0.01 sec)"
                    elif seconds < 60: return f"{int(seconds)} Seconds"
                    elif seconds < 3600: return f"{int(seconds/60)} Minutes"
                    elif seconds < 86400: return f"{int(seconds/3600)} Hours"
                    elif seconds < 31536000: return f"{int(seconds/86400)} Days"
                    elif seconds < 31536000 * 1000: return f"{int(seconds/31536000)} Years"
                    else: return "Millennia (Practically Impossible)"

                st.markdown(f"""
                - **Online Throttled Attack (100 req/s):** `{format_time(res['sec_online'])}`
                - **Single Standard CPU (10M/s):** `{format_time(res['sec_cpu'])}`
                - **Single Consumer GPU (RTX 4090):** `{format_time(res['sec_gpu'])}`
                - **Enterprise GPU Cluster (10T h/s):** `{format_time(res['sec_cluster'])}`
                - **Custom ASIC Rig (1P h/s):** `{format_time(res['sec_asic'])}`
                """)
                
                st.markdown("#### COMPLIANCE & HARDENING RECOMMENDATIONS")
                if res['score'] < 75:
                    st.markdown("""
                    1. **Complexity Enhancement:** Expand the character pool to include all available sets.
                    2. **Length Optimization:** Target a minimum length of 16 to 24 characters.
                    3. **Pattern Elimination:** Completely remove dictionary words or sequential number strings.
                    """)
                else:
                    st.success("[+] Password architecture complies with corporate and national security standards (NIST SP 800-63B).")

# ==========================================
# TAB 2: ADVANCED KEY & PASSPHRASE SYNTHESIZER
# ==========================================
with tab_generator:
    st.markdown("### CRYPTOGRAPHIC KEY & PASSWORD SYNTHESIS ENGINE")
    
    synth_mode = st.selectbox(
        "Select Synthesis Mode:", 
        [
            "Standard Character Pool Synthesizer", 
            "Diceware / Memorable Passphrase Generator", 
            "Custom Pattern & Keyword Injection Engine",
            "Cryptographic Token & Salt Generator (Hex / Base64)"
        ]
    )
    st.markdown("---")

    if synth_mode == "Standard Character Pool Synthesizer":
        c1, c2, c3 = st.columns(3)
        with c1:
            gen_len = st.slider("Key Length (Characters)", min_value=8, max_value=128, value=24, step=1)
            batch_qty = st.selectbox("Batch Generation Count", [1, 5, 10, 25], index=1)
        with c2:
            inc_u = st.checkbox("Include Uppercase [A-Z]", value=True)
            inc_l = st.checkbox("Include Lowercase [a-z]", value=True)
            inc_d = st.checkbox("Include Digits [0-9]", value=True)
        with c3:
            inc_s = st.checkbox("Include Special Symbols [!@#$]", value=True)
            exc_ambig = st.checkbox("Exclude Ambiguous Characters (l, I, O, 0)", value=True)
            enforce_types = st.checkbox("Enforce at least 1 from each selected set", value=True)

        if st.button("SYNTHESIZE STANDARD KEYS", type="primary"):
            pool_chars = ""
            if inc_l: pool_chars += string.ascii_lowercase
            if inc_u: pool_chars += string.ascii_uppercase
            if inc_d: pool_chars += string.digits
            if inc_s: pool_chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            if exc_ambig:
                for char in "lIO01":
                    pool_chars = pool_chars.replace(char, "")
                    
            if not pool_chars:
                st.error("[ERROR] Character pool cannot be empty. You must select at least one set.")
            else:
                st.markdown("#### SYNTHESIZED OUTPUT STREAM")
                for _ in range(batch_qty):
                    if enforce_types and gen_len >= 4:
                        temp_pwd = []
                        if inc_l: temp_pwd.append(random.choice(string.ascii_lowercase))
                        if inc_u: temp_pwd.append(random.choice(string.ascii_uppercase))
                        if inc_d: temp_pwd.append(random.choice(string.digits))
                        if inc_s: temp_pwd.append(random.choice("!@#$%^&*"))
                        
                        rem = gen_len - len(temp_pwd)
                        temp_pwd.extend(random.choices(pool_chars, k=rem))
                        random.shuffle(temp_pwd)
                        out_key = "".join(temp_pwd)
                    else:
                        out_key = "".join(random.choices(pool_chars, k=gen_len))
                    st.code(out_key, language="")

    elif synth_mode == "Diceware / Memorable Passphrase Generator":
        p1, p2, p3 = st.columns(3)
        with p1:
            w_count = st.slider("Word Count", min_value=3, max_value=10, value=5)
        with p2:
            w_sep = st.selectbox("Word Separator", ["-", "_", ".", "/", "+", "Space"])
        with p3:
            add_num_sfx = st.checkbox("Append Suffix Number", value=True)
            cap_init = st.checkbox("Capitalize Word Initials", value=True)

        lexicon = [
            "cyber", "nexus", "quantum", "matrix", "vertex", "vector", "binary", 
            "protocol", "firewall", "cipher", "packet", "kernel", "router", 
            "daemon", "proxy", "shield", "crypt", "node", "entropy", "syntax",
            "subnet", "gateway", "payload", "buffer", "token", "hash", "cluster"
        ]

        if st.button("SYNTHESIZE PASSPHRASE", type="primary"):
            chosen_words = random.choices(lexicon, k=w_count)
            if cap_init:
                chosen_words = [w.capitalize() for w in chosen_words]
            
            separator = " " if w_sep == "Space" else w_sep
            passphrase = separator.join(chosen_words)
            if add_num_sfx:
                passphrase += f"{separator}{random.randint(100, 999)}"
                
            st.markdown("#### SYNTHESIZED PASSPHRASE")
            st.code(passphrase, language="")
            st.info(f"Character Length: {len(passphrase)} | Readability & Memory Index: High")

    elif synth_mode == "Custom Pattern & Keyword Injection Engine":
        k1, k2 = st.columns(2)
        with k1:
            user_keyword = st.text_input("Mandatory Keyword / Name Input", placeholder="e.g., projectAlpha")
            total_target_len = st.slider("Target Total Length", min_value=12, max_value=64, value=20)
        with k2:
            key_pos = st.selectbox("Keyword Placement", ["Prepend (Start)", "Append (End)", "Randomized Mix"])
            wrap_sym = st.checkbox("Surround with Special Symbols", value=True)

        if st.button("SYNTHESIZE CUSTOM PATTERN", type="primary"):
            if not user_keyword:
                st.warning("[WARNING] You must enter a keyword to inject.")
            else:
                rem_len = max(4, total_target_len - len(user_keyword))
                random_string = "".join(random.choices(string.ascii_letters + string.digits + "!@#$*", k=rem_len))
                
                if key_pos == "Prepend (Start)":
                    final_key = user_keyword + ("#" if wrap_sym else "") + random_string
                elif key_pos == "Append (End)":
                    final_key = random_string + ("#" if wrap_sym else "") + user_keyword
                else:
                    mixed_list = list(user_keyword + random_string)
                    random.shuffle(mixed_list)
                    final_key = "".join(mixed_list)[:total_target_len]
                    
                st.markdown("#### CUSTOM INJECTION OUTPUT")
                st.code(final_key, language="")

    else: # Cryptic Token & Salt Generator
        t1, t2 = st.columns(2)
        with t1:
            token_format = st.selectbox("Format Type", ["Hexadecimal (Hex)", "Base64", "URL-Safe Token", "Pure Numeric PIN"])
            token_bytes = st.slider("Byte / Length Value", min_value=8, max_value=128, value=32, step=4)
        with t2:
            st.markdown("**Description:** This module is optimized for generating database salting, API keys, or secure session tokens.")

        if st.button("GENERATE TOKEN / SALT", type="primary"):
            if token_format == "Hexadecimal (Hex)":
                raw_token = os.urandom(token_bytes).hex()
            elif token_format == "Base64":
                raw_token = base64.b64encode(os.urandom(token_bytes)).decode('utf-8')
            elif token_format == "URL-Safe Token":
                raw_token = secrets.token_urlsafe(token_bytes)
            else:
                raw_token = "".join(random.choices(string.digits, k=token_bytes))

            st.markdown("#### CRYPTOGRAPHIC TOKEN OUTPUT")
            st.code(raw_token, language="")

# ==========================================
# TAB 3: ALGORITHMIC COMPLIANCE & ATTACK MATRIX
# ==========================================
with tab_matrix:
    st.markdown("### CRYPTOGRAPHIC ALGORITHM & HARDWARE RESISTANCE MATRIX")
    st.markdown("Comparative performance table of modern hashing functions and key derivation mechanisms.")

    matrix_data = pd.DataFrame({
        "Algorithm / Function": [
            "MD5 (Legacy Hash)", 
            "SHA-256 (Secure Hash Standard)", 
            "Bcrypt (Adaptive Cost 12)", 
            "Argon2id (Memory-Hard Function)", 
            "PBKDF2-HMAC-SHA256"
        ],
        "Throughput / Hashes per Sec (GPU)": [
            "~100 Billion Hashes/sec", 
            "~10 Billion Hashes/sec", 
            "~50,000 Hashes/sec", 
            "~1,000 Hashes/sec (Memory Bound)", 
            "~20,000 Hashes/sec"
        ],
        "ASIC / GPU Hardware Resistance": [
            "Extremely Low (Crackable)", 
            "Low (GPU Acceleration Prone)", 
            "High (Memory Costly)", 
            "Maximum (Side-Channel Resistant)", 
            "Medium (Balanced CPU/GPU)"
        ],
        "Recommended Enterprise Use Case": [
            "Deprecated (Except Checksums)", 
            "Integrity Verification / Digital Signatures", 
            "Traditional Password Hashing", 
            "Modern Enterprise Cryptography Standard", 
            "Key Derivation Functions (KDF)"
        ]
    })

    st.dataframe(matrix_data, use_container_width=True)
    
    st.markdown("### STANDARDS AND MATHEMATICAL FORMULATIONS")
    st.markdown("""
    - **Shannon Entropy Equation:** $H = L \\times \\log_2(R)$ (where $L$ represents length and $R$ represents character pool size).
    - **NIST SP 800-63B Compliance:** Advocates that enterprise password policies should focus on length (minimum 15-20 characters) and entropy rather than arbitrary complexity mandates.
    - **Salt and Pepper Integration:** Incorporating random bit strings (salt) into every hash input is mandatory to completely nullify pre-computed rainbow table attacks.
    """)

st.markdown("---")
st.markdown("Cryptic Core Enterprise Security Intelligence Suite • Local Sandbox Execution Environment • v5.2.0")
