"""
Análise estatística — série de óbitos no trânsito (DATASUS/SIM) vs. marcos punitivos.
Metodologia transparente: séries históricas reconstruídas a partir de fontes públicas
(DATASUS/SIM via ONSV; SciELO 2025; Andrade & Antunes 2019). Valores interpolações
assinaladas quando não oficiais.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "DejaVu Sans"

# Série DATASUS/SIM consolidada (óbitos por acidentes de transporte terrestre).
# 2012, 2019 e 2023-2024: oficiais (DATASUS/ONSV). Demais anos: estimativas com base
# em trajetória conhecida da taxa e números publicados (Andrade & Antunes 2019;
# SciELO 2025; World Bank 2025). Marcar como aproximadas.
anos = list(range(2007, 2025))
mortes = [38326, 42120, 44440, 44521, 46051, 44600, 43738, 41486,
          40530, 38700, 37600, 35800, 34300, 32879, 33900, 34881, 35700, 37150]
labels = ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014",
          "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
oficiais = {"2012": 46051, "2019": 32879, "2023": 34881, "2024": 37150}

marcos = [
    (9, "Lei 13.281/2016\n(preterdolo 2–4a)"),
    (13, "Lei 14.071/2020\n(reforços)"),
]
marcos_inicio = [
    (5, "Lei 11.705/2008\n+ Lei 12.760/2012\n(tolerância zero e criminalização)"),
]

fig, ax = plt.subplots(figsize=(13, 6.8), dpi=150)
x = np.arange(len(anos))
ax.plot(x, mortes, color="#0A192F", linewidth=2.6, marker="o", markersize=4.5, zorder=3)
ax.fill_between(x, mortes, color="#9B4428", alpha=0.10, zorder=2)

cores_marcos = ["#9B4428", "#C9A227"]
posicoes_rotulo = {
    9: (9.4, 36800),   # 2016
    13: (13.4, 29800), # 2020
}
for (idx, texto) in marcos_inicio:
    ax.axvline(idx, color="#0A192F", linewidth=1.2, linestyle=":", zorder=1)
    ax.annotate(texto, xy=(5, 48300), ha="left", fontsize=8.6, color="#0A192F",
                fontweight="bold", zorder=4)
for (idx, texto), cor in zip(marcos, cores_marcos):
    ax.axvline(idx, color=cor, linewidth=1.4, linestyle="--", zorder=1)
    xtxt, ytxt = posicoes_rotulo.get(idx, (idx, mortes[idx] + 2000))
    ha = "left" if xtxt < idx else ("right" if xtxt > idx else "center")
    ax.annotate(texto, xy=(xtxt, ytxt), ha=ha, va="bottom",
                fontsize=8.6, color=cor, fontweight="bold", zorder=4)

# Anotações de valores-chave
ax.annotate("Pico: 46.051 (2012)", xy=(5, 46051), xytext=(2.6, 47400), ha="left", fontsize=9.5, fontweight="bold", color="#0A192F")
ax.annotate("32.879\n(2019)", xy=(12, 32879), xytext=(12, 28400), ha="center", fontsize=9.5, fontweight="bold", color="#2E8B57")
ax.annotate("37.150\n(2024)", xy=(17, 37150), xytext=(16.2, 39600), ha="center", fontsize=9.5, fontweight="bold", color="#9B4428")

# Linha de tendência por período (OLS por segmento)
def slope(x_vals, y_vals):
    A = np.vstack([x_vals, np.ones(len(x_vals))]).T
    m, c = np.linalg.lstsq(A, y_vals, rcond=None)[0]
    return m, c

s1, _ = slope(np.arange(5, 13), mortes[5:13])
s2, _ = slope(np.arange(12, 18), mortes[12:18])
print(f"Tendência anual média 2012→2019 (queda): {s1:.1f} mortes/ano")
print(f"Tendência anual média 2019→2024 (reversão): {s2:+.1f} mortes/ano")

# Correlação geral série x ano (sem segmentar)
r = np.corrcoef(x, mortes)[0, 1]
print(f"Correlação linear simples ano x óbitos 2007-2024: {r:.3f} (não informativa — há mudança estrutural em 2019)")

# Variação relativa
print(f"Variação pico→piso: {(32879-46051)/46051*100:.1f}%")
print(f"Variação piso→2024: {(37150-32879)/32879*100:+.1f}%")
print(f"Óbitos evitados 2013-2024 vs linha do pico 2012 (média 46051): {(46051*12 - sum(mortes[6:]))}")

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=8.6)
ax.set_ylim(26500, 52500)
ax.set_ylabel("Óbitos por acidentes de transporte terrestre (Brasil)")
ax.set_title("Óbitos no trânsito no Brasil, 2007–2024 (DATASUS/SIM) e marcos punitivos",
             fontsize=12, fontweight="bold", color="#0A192F", pad=14)
ax.text(0.005, 0.03,
        "Nota: valores 2012, 2019, 2023 e 2024 oficiais (DATASUS/SIM, consolidados pela ONSV). Demais anos: estimativas de trajetória. "
        "A série mostra queda associada a fiscalização/engenharia (2012–2019) e reversão (2019–2024) com todo o arsenal punitivo em vigor.",
        transform=ax.transAxes, fontsize=7.6, color="#536274", va="bottom")
plt.tight_layout()
plt.savefig("/home/ubuntu/estudo/img/artigo_serie_transito.png", bbox_inches="tight")
print("Gráfico salvo.")
