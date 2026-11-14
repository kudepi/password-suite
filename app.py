import streamlit as st
import random
import string
import math
import pandas as pd
import hashlib
import os
import secrets
import base64

# Sayfa Yapılandırması (Geniş Ekran Modu)
st.set_page_config(
    page_title="Cryptic Core // Enterprise Intelligence Platform", 
    page_icon=None, 
    layout="wide"
)

# Profesyonel, Sıfır Emoji, Ağır Siklet Cyber-Security CSS Tasarımı
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

# Üst Bilgi Konsolu
st.markdown("## [ SYSTEM INTERFACE: CRYPTIC CORE v5.2 ]")
st.markdown("Advanced Cryptographic Intelligence, Multi-Vector Vulnerability Auditor, and High-Entropy Key Synthesis Terminal.")
st.markdown("---")

# Ana Sekmeler
tab_audit, tab_generator, tab_matrix = st.tabs([
    "DEEP SECURITY & VULNERABILITY AUDITOR", 
    "ADVANCED KEY & PASSPHRASE SYNTHESIZER", 
    "ALGORITHMIC COMPLIANCE & ATTACK MATRIX"
])

# ==========================================
# SEKME 1: DERİN GÜVENLİK VE ZAFİYET AUDITOR
# ==========================================
with tab_audit:
    st.markdown("### TARGET PAROLA ANALİZ TERMİNALİ")
    col_input, col_meta = st.columns([2, 1])
    
    with col_input:
        password_input = st.text_input("Analiz Edilecek Parolayı Girin:", type="password", placeholder="Parola dizilimini buraya yazın...")
    with col_meta:
        st.markdown("**Tarama Modu:** Tam Spektrumlu Entropi ve Zafiyet Analizi")

    def run_advanced_audit(pwd):
        if not pwd:
            return None
        
        length = len(pwd)
        has_lower = any(c.islower() for c in pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(c in string.punctuation for c in pwd)
        has_extended = any(ord(c) > 127 for c in pwd)
        
        # Karakter Havuzu Hesaplama
        pool = 0
        if has_lower: pool += 26
        if has_upper: pool += 26
        if has_digit: pool += 10
        if has_special: pool += len(string.punctuation)
        if has_extended: pool += 32
        
        if pool == 0:
            return {"score": 0, "entropy": 0, "status": "INVALID"}

        # Shannon Entropi (Bits)
        entropy = length * math.log2(pool)
        
        # Hash tespiti (MD5 / SHA256 simulasyonu)
        md5_hash = hashlib.md5(pwd.encode()).hexdigest()
        sha256_hash = hashlib.sha256(pwd.encode()).hexdigest()
        
        # Kırılma Süreleri (Farklı Donanım Vektörleri)
        total_combos = 2 ** entropy
        sec_online = total_combos / 100            # Ağ kısıtlı (100 istek/sn)
        sec_cpu = total_combos / 1e7               # CPU Brute-force (10M/sn)
        sec_gpu = total_combos / 1e10              # Tekli GPU RTX 4090 (10B/sn)
        sec_cluster = total_combos / 1e13          # Kurumsal GPU Farm (10T/sn)
        sec_asic = total_combos / 1e15             # ASIC Donanım (1P/sn)

        # Gelişmiş Zafiyet ve Kalıp Tespiti
        penalties = 0
        flaws = []
        
        # Klavye yürüyüşleri kontrolü (Keyboard walks)
        keyboard_walks = ["qwerty", "asdfgh", "zxcvbn", "123456", "qazwsx", "123321", "password", "admin", "letmein"]
        if any(walk in pwd.lower() for walk in keyboard_walks):
            penalties += 35
            flaws.append("Kritik: Yaygın klavye yürüyüşü veya sözlük tabanlı zayıf kalıp tespit edildi.")

        # Ardışık karakterler
        sequential_count = 0
        for i in range(len(pwd) - 2):
            if ord(pwd[i]) + 1 == ord(pwd[i+1]) and ord(pwd[i+1]) + 1 == ord(pwd[i+2]):
                sequential_count += 1
        if sequential_count > 0:
            penalties += 15 * sequential_count
            flaws.append(f"Uyarı: {sequential_count} adet ardışık karakter dizilimi (örn: 123, abc) tespit edildi.")

        # Tekrarlayan karakterler
        max_rep = max([pwd.count(c) for c in set(pwd)]) if pwd else 0
        if max_rep > length / 3 and length > 4:
            penalties += 20
            flaws.append("Uyarı: Belirli karakterlerin aşırı tekrarı entropiyi düşürüyor.")

        # Uzunluk denetimi
        if length < 12:
            penalties += 25
            flaws.append("Kritik: Uzunluk 12 karakter eşiğinin altında. Minimum 16 önerilir.")

        # Leet-speak tespiti (örn: e->3, a->@)
        leet_map = {'3': 'e', '4': 'a', '1': 'i', '0': 'o', '!': 'i', '$': 's'}
        leet_score = sum(1 for char in pwd if char in leet_map)
        if leet_score > 0 and length < 10:
            penalties += 15
            flaws.append("Bilgi: Sığ Leet-speak (karakter değişimi) kullanılmış; gelişmiş dictionary saldırılarına karşı savunmasız.")

        # Final Skor
        base_score = min(100, int((entropy / 110) * 100))
        final_score = max(0, base_score - penalties)

        if final_score < 35:
            rating = "KRİTİK ZAFİYET SEVİYESİ"
        elif final_score < 65:
            rating = "ORTA DÜZEY RİSK"
        elif final_score < 85:
            rating = "GÜVENLİ DİZİLİM"
        else:
            rating = "ASKERİ DÜZEYDE DAYANIKLILIK"

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
            st.markdown("### DENETİM METRİKLERİ VE SKORLAR")
            
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.metric("Shannon Entropi", f"{res['entropy']} bits")
            with m2:
                st.metric("Güvenlik İndeksi", f"{res['score']} / 100")
            with m3:
                st.metric("Durum Değerlendirmesi", res['rating'])
            with m4:
                st.metric("Karakter Havuz Boyutu", f"{res['pool']} varyasyon")
                
            st.progress(res['score'] / 100)
            
            st.markdown("---")
            col_det1, col_det2 = st.columns(2)
            
            with col_det1:
                st.markdown("#### STRÜKTÜREL YAPI VE HASH ANALİZİ")
                st.markdown(f"""
                - **Karakter Uzunluğu:** `{res['length']} birim`
                - **Küçük Harf [a-z]:** `{'Mevcut' if res['has_lower'] else 'Eksik'}`
                - **Büyük Harf [A-Z]:** `{'Mevcut' if res['has_upper'] else 'Eksik'}`
                - **Sayısal Rakam [0-9]:** `{'Mevcut' if res['has_digit'] else 'Eksik'}`
                - **Özel Semboller [!@#$]:** `{'Mevcut' if res['has_special'] else 'Eksik'}`
                - **Genişletilmiş Unicode:** `{'Mevcut' if res['has_extended'] else 'Yok'}`
                - **MD5 Hash Özet Değeri:** `{res['md5']}`
                - **SHA-256 Hash Özet Değeri:** `{res['sha256']}`
                """)
                
                st.markdown("#### TESPİT EDİLEN ZAFİYETLER VE RİSKLER")
                if res['flaws']:
                    for flaw in res['flaws']:
                        st.warning(f"[!] {flaw}")
                else:
                    st.success("[+] Bilinen kalıp tabanlı zafiyet veya ardışık dizi saptanmadı.")

            with col_det2:
                st.markdown("#### HESAPLANAN BRUTE-FORCE KIRILMA SÜRELERİ")
                
                def format_time(seconds):
                    if seconds < 0.01: return "Anında (< 0.01 sn)"
                    elif seconds < 60: return f"{int(seconds)} Saniye"
                    elif seconds < 3600: return f"{int(seconds/60)} Dakika"
                    elif seconds < 86400: return f"{int(seconds/3600)} Saat"
                    elif seconds < 31536000: return f"{int(seconds/86400)} Gün"
                    elif seconds < 31536000 * 1000: return f"{int(seconds/31536000)} Yıl"
                    else: return "Minyarlarca Yıl (Pratikte İmkansız)"

                st.markdown(f"""
                - **Online Kısıtlı Saldırı (100 req/s):** `{format_time(res['sec_online'])}`
                - **Tekil Standart CPU (10M/s):** `{format_time(res['sec_cpu'])}`
                - **Tekli Tüketici GPU (RTX 4090):** `{format_time(res['sec_gpu'])}`
                - **Kurumsal GPU Havuzu (10T h/s):** `{format_time(res['sec_cluster'])}`
                - **Özel Donanım ASIC Rig (1P h/s):** `{format_time(res['sec_asic'])}`
                """)
                
                st.markdown("#### UYUMLULUK VE İYİLEŞTİRME ÖNERİLERİ")
                if res['score'] < 75:
                    st.markdown("""
                    1. **Kompleksite Artırımı:** Karakter havuzunu tüm setleri kapsayacak şekilde genişletin.
                    2. **Uzunluk Optimizasyonu:** Minimum 16 ila 24 karakter uzunluğunu hedefleyin.
                    3. **Kalıp Temizliği:** Sözlük kelimeleri veya ardışık sayı dizgilerini tamamen kaldırın.
                    """)
                else:
                    st.success("[+] Parola yapısı kurumsal ve ulusal güvenlik standartlarına (NIST SP 800-63B) uygundur.")

# ==========================================
# SEKME 2: GELİŞMİŞ ŞİFRE ÜRETİCİSİ
# ==========================================
with tab_generator:
    st.markdown("### KRİPTOGRAFİK ANAHTAR VE PAROLA ÜRETİM MOTORU")
    
    synth_mode = st.selectbox(
        "Sentez Modu Seçimi:", 
        [
            "Standart Karakter Havuzu Sentezleyicisi", 
            "Diceware / Okunabilir Passphrase Üreteci", 
            "Özel Kalıp ve Anahtar Kelime Enjeksiyon Motoru",
            "Kriptografik Token ve Salt Üreteci (Hex / Base64)"
        ]
    )
    st.markdown("---")

    if synth_mode == "Standart Karakter Havuzu Sentezleyicisi":
        c1, c2, c3 = st.columns(3)
        with c1:
            gen_len = st.slider("Anahtar Uzunluğu (Karakter)", min_value=8, max_value=128, value=24, step=1)
            batch_qty = st.selectbox("Toplu Üretim Adedi", [1, 5, 10, 25], index=1)
        with c2:
            inc_u = st.checkbox("Büyük Harf Dahil [A-Z]", value=True)
            inc_l = st.checkbox("Küçük Harf Dahil [a-z]", value=True)
            inc_d = st.checkbox("Sayısal Rakam Dahil [0-9]", value=True)
        with c3:
            inc_s = st.checkbox("Özel Karakter Dahil [!@#$]", value=True)
            exc_ambig = st.checkbox("Belirsiz Karakterleri Ayıkla (l, I, O, 0)", value=True)
            enforce_types = st.checkbox("Her Seçilen Setten En Az 1 Adet Zorunlu Tut", value=True)

        if st.button("STANDART ANAHTARLARI SENTEZLE", type="primary"):
            pool_chars = ""
            if inc_l: pool_chars += string.ascii_lowercase
            if inc_u: pool_chars += string.ascii_uppercase
            if inc_d: pool_chars += string.digits
            if inc_s: pool_chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            if exc_ambig:
                for char in "lIO01":
                    pool_chars = pool_chars.replace(char, "")
                    
            if not pool_chars:
                st.error("[HATA] Karakter havuzu boş bırakılamaz. En az bir set seçmelisiniz.")
            else:
                st.markdown("#### SENTEZLENEN ÇIKTI AKIŞI")
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

    elif synth_mode == "Diceware / Okunabilir Passphrase Üreteci":
        p1, p2, p3 = st.columns(3)
        with p1:
            w_count = st.slider("Kelime Sayısı", min_value=3, max_value=10, value=5)
        with p2:
            w_sep = st.selectbox("Kelime Ayracı", ["-", "_", ".", "/", "+", "Boşluk"])
        with p3:
            add_num_sfx = st.checkbox("Son Ek Sayı Ekle", value=True)
            cap_init = st.checkbox("Kelime Baş Harflerini Büyük Yap", value=True)

        lexicon = [
            "cyber", "nexus", "quantum", "matrix", "vertex", "vector", "binary", 
            "protocol", "firewall", "cipher", "packet", "kernel", "router", 
            "daemon", "proxy", "shield", "crypt", "node", "entropy", "syntax",
            "subnet", "gateway", "payload", "buffer", "token", "hash", "cluster"
        ]

        if st.button("PASSPHRASE SENTEZLE", type="primary"):
            chosen_words = random.choices(lexicon, k=w_count)
            if cap_init:
                chosen_words = [w.capitalize() for w in chosen_words]
            
            separator = " " if w_sep == "Boşluk" else w_sep
            passphrase = separator.join(chosen_words)
            if add_num_sfx:
                passphrase += f"{separator}{random.randint(100, 999)}"
                
            st.markdown("#### SENTEZLENEN PASSPHRASE")
            st.code(passphrase, language="")
            st.info(f"Karakter Uzunluğu: {len(passphrase)} | Okunabilirlik ve Hafıza İndeksi: Yüksek")

    elif synth_mode == "Özel Kalıp ve Anahtar Kelime Enjeksiyon Motoru":
        k1, k2 = st.columns(2)
        with k1:
            user_keyword = st.text_input("Zorunlu Anahtar Kelime / İsim Girişi", placeholder="Örn: projectAlpha")
            total_target_len = st.slider("Hedef Toplam Uzunluk", min_value=12, max_value=64, value=20)
        with k2:
            key_pos = st.selectbox("Kelime Yerleşimi", ["Başa Ekle", "Sona Ekle", "Rastgele Karıştır"])
            wrap_sym = st.checkbox("Özel Sembollerle Çevrele", value=True)

        if st.button("ÖZEL KALIBI SENTEZLE", type="primary"):
            if not user_keyword:
                st.warning("[UYARI] Enjekte edilecek bir anahtar kelime girmelisiniz.")
            else:
                rem_len = max(4, total_target_len - len(user_keyword))
                random_string = "".join(random.choices(string.ascii_letters + string.digits + "!@#$*", k=rem_len))
                
                if key_pos == "Başa Ekle":
                    final_key = user_keyword + ("#" if wrap_sym else "") + random_string
                elif key_pos == "Sona Ekle":
                    final_key = random_string + ("#" if wrap_sym else "") + user_keyword
                else:
                    mixed_list = list(user_keyword + random_string)
                    random.shuffle(mixed_list)
                    final_key = "".join(mixed_list)[:total_target_len]
                    
                st.markdown("#### ÖZEL ENJEKSİYON ÇIKTISI")
                st.code(final_key, language="")

    else: # Kriptografik Token ve Salt Üreteci
        t1, t2 = st.columns(2)
        with t1:
            token_format = st.selectbox("Format Tipi", ["Hexadecimal (Hex)", "Base64", "URL-Safe Token", "Pure Numeric PIN"])
            token_bytes = st.slider("Bayt / Uzunluk Değeri", min_value=8, max_value=128, value=32, step=4)
        with t2:
            st.markdown("**Açıklama:** Bu mod, veritabanı tuzlama (salting), API anahtarları veya güvenli oturum tokenleri üretmek için optimize edilmiştir.")

        if st.button("TOKEN / SALT ÜRET", type="primary"):
            if token_format == "Hexadecimal (Hex)":
                raw_token = os.urandom(token_bytes).hex()
            elif token_format == "Base64":
                raw_token = base64.b64encode(os.urandom(token_bytes)).decode('utf-8')
            elif token_format == "URL-Safe Token":
                raw_token = secrets.token_urlsafe(token_bytes)
            else:
                raw_token = "".join(random.choices(string.digits, k=token_bytes))

            st.markdown("#### KRİPTOGRAFİK TOKEN ÇIKTISI")
            st.code(raw_token, language="")

# ==========================================
# SEKME 3: ALGORİTMA VE UYUMLULUK MATRİSİ
# ==========================================
with tab_matrix:
    st.markdown("### KRİPTOGRAFİK ALGORİTMA VE DONANIM DİRENCİ MATRİSİ")
    st.markdown("Güncel hash fonksiyonlarının ve anahtar türetme mekanizmalarının başarım karşılaştırma tablosu.")

    matrix_data = pd.DataFrame({
        "Algoritma / Fonksiyon": [
            "MD5 (Legacy Hash)", 
            "SHA-256 (Secure Hash Standard)", 
            "Bcrypt (Adaptive Cost 12)", 
            "Argon2id (Memory-Hard Function)", 
            "PBKDF2-HMAC-SHA256"
        ],
        "Saniyedeki İşlem Kapasitesi (GPU)": [
            "~100 Milyar Hashes/sec", 
            "~10 Milyar Hashes/sec", 
            "~50,000 Hashes/sec", 
            "~1,000 Hashes/sec (Bellek Kısıtlı)", 
            "~20,000 Hashes/sec"
        ],
        "ASIC / GPU Donanım Direnci": [
            "Çok Düşük (Kırılabilir)", 
            "Düşük (GPU Hızlandırmasına Açık)", 
            "Yüksek (Bellek Maliyetli)", 
            "Maksimum (Side-channel Dirençli)", 
            "Orta Düzey (CPU/GPU Dengeli)"
        ],
        "Önerilen Kurumsal Kullanım Alanı": [
            "Kullanımdan Kaldırıldı (Checksum Hariç)", 
            "Bütünlük Doğrulama / Dijital İmza", 
            "Geleneksel Parola Hashleme", 
            "Modern Enterprise Kriptografi Standardı", 
            "Key Derivation Functions (KDF)"
        ]
    })

    st.dataframe(matrix_data, use_container_width=True)
    
    st.markdown("### STANDARTLAR VE MATEMATİKSEL FORMÜLASYONLAR")
    st.markdown("""
    - **Shannon Entropi Denklemi:** $H = L \\times \\log_2(R)$ (Burada $L$ uzunluk, $R$ karakter havuzu büyüklüğünü ifade eder).
    - **NIST SP 800-63B Uyumluluğu:** Kurumsal sistemlerde parola politikalarının ezber dayatması yerine uzunluğa (minimum 15-20 karakter) ve entropi değerine odaklanması gerektiğini savunur.
    - **Salt ve Pepper Entegrasyonu:** Rainbow table saldırılarını tamamen etkisiz kılmak için her hash girdisine rastgele bit dizileri (salt) eklenmesi zorunludur.
    """)

st.markdown("---")
st.markdown("Cryptic Core Enterprise Security Intelligence Suite • Local Sandbox Execution Environment • v5.2.0")
