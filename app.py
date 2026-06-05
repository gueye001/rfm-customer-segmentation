import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(
    page_title="RFM Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .block-container { padding-top: 1.5rem; }
    .kpi-card {
        background: linear-gradient(135deg, #1e2130, #262d3d);
        border-radius: 12px;
        padding: 20px 24px;
        border-left: 4px solid;
        margin-bottom: 8px;
    }
    .kpi-label {
        font-size: 13px;
        color: #8b92a5;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 6px;
    }
    .kpi-value {
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
    }
    .kpi-delta {
        font-size: 12px;
        margin-top: 4px;
        color: #8b92a5;
    }
    .section-title {
        font-size: 18px;
        font-weight: 600;
        color: #ffffff;
        margin: 24px 0 16px 0;
        padding-bottom: 8px;
        border-bottom: 1px solid #2d3447;
    }
    [data-testid="stSidebar"] {
        background-color: #131720;
        border-right: 1px solid #2d3447;
    }
    .stDataFrame { border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

COLORS = {
    'Champions':            '#2ecc71',
    'Perdus':               '#e74c3c',
    'A risque':             '#f39c12',
    'Nouveaux prometteurs': '#3498db'
}
BG_COLOR   = '#0e1117'
CARD_COLOR = '#1e2130'
TEXT_COLOR = '#ffffff'
GRID_COLOR = '#2d3447'

matplotlib.rcParams.update({
    'figure.facecolor': BG_COLOR,
    'axes.facecolor':   CARD_COLOR,
    'axes.edgecolor':   GRID_COLOR,
    'axes.labelcolor':  TEXT_COLOR,
    'xtick.color':      TEXT_COLOR,
    'ytick.color':      TEXT_COLOR,
    'text.color':       TEXT_COLOR,
    'grid.color':       GRID_COLOR,
    'grid.linewidth':   0.5,
})

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

rfm = load_data('data/rfm_final.csv')

# Sidebar
with st.sidebar:
    st.markdown(
        "<h2 style='color:#ffffff;font-size:20px;"
        "font-weight:700;margin-bottom:4px'>📊 RFM Dashboard</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='color:#8b92a5;font-size:12px;"
        "margin-bottom:16px'>Online Retail UCI</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown(
        "<p style='color:#8b92a5;font-size:12px;"
        "text-transform:uppercase;letter-spacing:1px;"
        "margin-bottom:8px'>Segment client</p>",
        unsafe_allow_html=True
    )
    segment_choisi = st.radio(
        label="",
        options=['Tous', 'Champions', 'Perdus',
                 'A risque', 'Nouveaux prometteurs'],
        index=0
    )
    st.markdown("---")
    st.markdown(
        "<p style='color:#8b92a5;font-size:12px;"
        "text-transform:uppercase;letter-spacing:1px'>À propos</p>",
        unsafe_allow_html=True
    )
    st.markdown("""
    <div style='color:#c8cdd8;font-size:13px;line-height:1.6'>
    Segmentation de <b style='color:#ffffff'>5 878 clients</b><br>
    basée sur 3 dimensions :
    <br><br>
    🕐 <b>Récence</b> — dernier achat<br>
    🔁 <b>Fréquence</b> — nb de commandes<br>
    💰 <b>Montant</b> — CA généré
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "<p style='color:#8b92a5;font-size:12px;"
        "text-transform:uppercase;letter-spacing:1px'>Légende</p>",
        unsafe_allow_html=True
    )
    for seg, color in COLORS.items():
        st.markdown(
            f"<p style='color:{color};font-size:13px;"
            f"margin:4px 0'>● {seg}</p>",
            unsafe_allow_html=True
        )

# Filtre
rfm_filtre = rfm[rfm['Segment'] == segment_choisi] \
    if segment_choisi != 'Tous' else rfm

# Header
accent = COLORS.get(segment_choisi, '#7c83fd')
st.markdown(
    "<h1 style='color:#ffffff;font-size:32px;font-weight:700;"
    "margin-bottom:4px'>📊 Segmentation Clients RFM</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='color:#8b92a5;font-size:14px;margin-bottom:24px'>"
    "Online Retail UCI · 805 549 transactions · "
    "Décembre 2009 — Décembre 2011</p>",
    unsafe_allow_html=True
)

# KPIs
col1, col2, col3, col4 = st.columns(4)
kpis = [
    (col1, "👥 Clients",
     f"{len(rfm_filtre):,}",
     f"{len(rfm_filtre)/len(rfm)*100:.1f}% de la base"),
    (col2, "💰 Montant moyen",
     f"{rfm_filtre['Montant'].mean():,.0f} €",
     f"Max : {rfm_filtre['Montant'].max():,.0f} €"),
    (col3, "🔁 Fréquence moy.",
     f"{rfm_filtre['Frequence'].mean():.1f}",
     f"Max : {rfm_filtre['Frequence'].max()} commandes"),
    (col4, "🕐 Récence moyenne",
     f"{rfm_filtre['Recence'].mean():.0f} jours",
     f"Min : {rfm_filtre['Recence'].min()} jours"),
]
for col, label, value, delta in kpis:
    with col:
        st.markdown(f"""
        <div class="kpi-card" style="border-left-color:{accent}">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-delta">{delta}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Répartition
st.markdown("<div class='section-title'>Répartition des segments</div>",
            unsafe_allow_html=True)
col1, col2 = st.columns(2)
tailles = rfm.groupby('Segment').size()
seg_colors = [COLORS[s] for s in tailles.index]

with col1:
    fig, ax = plt.subplots(figsize=(6, 5))
    wedges, texts, autotexts = ax.pie(
        tailles, labels=tailles.index,
        autopct='%1.1f%%', colors=seg_colors,
        startangle=90, pctdistance=0.8,
        wedgeprops=dict(width=0.6)
    )
    for t in texts:
        t.set_color(TEXT_COLOR)
        t.set_fontsize(11)
    for at in autotexts:
        at.set_color(TEXT_COLOR)
        at.set_fontsize(10)
        at.set_fontweight('bold')
    ax.set_title('Parts de chaque segment', color=TEXT_COLOR,
                 fontsize=13, fontweight='bold', pad=15)
    st.pyplot(fig)
    plt.close()

with col2:
    fig, ax = plt.subplots(figsize=(6, 5))
    bars = ax.bar(tailles.index, tailles.values,
                  color=seg_colors, alpha=0.9,
                  edgecolor=GRID_COLOR, linewidth=0.5)
    for bar, val in zip(bars, tailles.values):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 15,
                f'{val:,}', ha='center',
                fontweight='bold', fontsize=11)
    ax.set_xticks(range(len(tailles)))
    ax.set_xticklabels(tailles.index, fontsize=9,
                       rotation=20, ha='right')
    fig.subplots_adjust(bottom=0.2)
    ax.set_ylabel('Nombre de clients')
    ax.set_title('Clients par segment', color=TEXT_COLOR,
                 fontsize=13, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, tailles.max() * 1.15)
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# Profil
st.markdown("<div class='section-title'>Profil des segments</div>",
            unsafe_allow_html=True)
profil = rfm.groupby('Segment').agg(
    Recence_moy   =('Recence',   'mean'),
    Frequence_moy =('Frequence', 'mean'),
    Montant_moy   =('Montant',   'mean')
).round(1)

heatmap_norm = pd.DataFrame(
    MinMaxScaler().fit_transform(profil),
    index=profil.index, columns=profil.columns
)
heatmap_correct = heatmap_norm.copy()
heatmap_correct['Recence_moy'] = 1 - heatmap_norm['Recence_moy']

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.heatmap(
        heatmap_correct, annot=profil, fmt='',
        cmap='RdYlGn', linewidths=1,
        linecolor=BG_COLOR, ax=ax,
        vmin=0, vmax=1,
        annot_kws={'size': 10, 'weight': 'bold'}
    )
    ax.set_title('Profil RFM (vert = bon, rouge = mauvais)',
                 color=TEXT_COLOR, fontsize=12, fontweight='bold')
    ax.tick_params(colors=TEXT_COLOR)
    st.pyplot(fig)
    plt.close()

with col2:
    segs = profil.index.tolist()
    x = np.arange(len(segs))
    width = 0.25
    recence_inv = [1 - v for v in heatmap_norm['Recence_moy']]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(x - width, recence_inv,
           width, label='Récence',   color='#e74c3c', alpha=0.9)
    ax.bar(x, heatmap_norm['Frequence_moy'],
           width, label='Fréquence', color='#3498db', alpha=0.9)
    ax.bar(x + width, heatmap_norm['Montant_moy'],
           width, label='Montant',   color='#2ecc71', alpha=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(segs, fontsize=9, rotation=20, ha='right')
    fig.subplots_adjust(bottom=0.2)
    ax.set_ylabel('Score normalisé (0-1)')
    ax.set_title('Comparaison des profils',
                 color=TEXT_COLOR, fontsize=12, fontweight='bold')
    ax.legend(facecolor=CARD_COLOR, edgecolor=GRID_COLOR)
    ax.grid(axis='y', alpha=0.3)
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# Tableau
st.markdown("<div class='section-title'>Explorer les clients</div>",
            unsafe_allow_html=True)
st.dataframe(
    rfm_filtre[['Customer ID', 'Segment', 'Recence',
                'Frequence', 'Montant']]
    .sort_values('Montant', ascending=False)
    .rename(columns={
        'Customer ID': 'Client',
        'Recence':     'Récence (j)',
        'Frequence':   'Fréquence',
        'Montant':     'Montant (€)'
    })
    .reset_index(drop=True),
    use_container_width=True,
    height=400
)

st.markdown(
    "<p style='text-align:center;color:#8b92a5;"
    "font-size:12px;margin-top:40px'>"
    "Dashboard RFM · Online Retail UCI · "
    "github.com/gueye001</p>",
    unsafe_allow_html=True
)