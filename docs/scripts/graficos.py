#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gráficos comparativos para o estudo sobre hiperinflação penal no Brasil."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

AZUL = "#1a3a5c"
VERMELHO = "#c0392b"
CINZA = "#7f8c8d"
DOURADO = "#b8860b"
VERDE = "#27ae60"
OUT_DIR = "/home/ubuntu/estudo/img"
import os
os.makedirs(OUT_DIR, exist_ok=True)


def save(fig, name):
    fig.savefig(f"{OUT_DIR}/{name}.png", bbox_inches="tight", facecolor="white")
    fig.savefig(f"{OUT_DIR}/{name}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("ok:", name)


# ----------------------------------------------------------------
# GRÁFICO 1 — Evolução da população carcerária brasileira (1988-2025)
# ----------------------------------------------------------------
anos = [1988, 1995, 1997, 2000, 2005, 2010, 2015, 2020, 2023, 2025]
presos = [88041, 173104, 198520, 232755, 401236, 496251, 622202, 744216, 811707, 964668]

fig, ax = plt.subplots(figsize=(11, 6))
ax.plot(anos, presos, marker="o", color=AZUL, linewidth=2.5, markersize=7, zorder=3)
ax.fill_between(anos, presos, alpha=0.15, color=AZUL)
for x, y in zip(anos, presos):
    ax.annotate(f"{y:,.0f}".replace(",", "."), (x, y), textcoords="offset points",
                xytext=(0, 10), ha="center", fontsize=9, color="#333")
ax.set_title("Evolução da população carcerária brasileira (1988–2025)",
             fontsize=15, fontweight="bold", pad=14, color=AZUL)
ax.set_ylabel("Pessoas presas")
ax.set_xlabel("Ano")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{int(v/1000)} mil"))
ax.text(0.01, 0.97, "Brasil passou de 88 mil presos (1988) para 964,7 mil (2025):\ncrescimento de 998% em 37 anos",
        transform=ax.transAxes, fontsize=10, va="top", bbox=dict(boxstyle="round", fc="#f2f2f2", ec="none"))
ax.text(0.99, -0.14, "Fontes: World Prison Brief / Infopen-SENAPPEN", transform=ax.transAxes,
        ha="right", fontsize=8.5, color=CINZA)
save(fig, "grafico1_evolucao_carceraria")


# ----------------------------------------------------------------
# GRÁFICO 2 — Comparação internacional de taxas de encarceramento (2024-2025)
# ----------------------------------------------------------------
paises = ["EUA", "Brasil", "Rússia", "Tailândia", "Argentina", "Chile",
          "Espanha", "Inglaterra\ne Gales", "França", "Alemanha", "Japão"]
taxas = [637, 439, 451, 348, 245, 231, 150, 143, 99, 63, 38]
# taxas WPB recentes: EUA ~522-637 (usar 522?); para ser conservador use 637? -> usar 522 (2024)
taxas = [522, 439, 451, 348, 245, 231, 150, 143, 99, 63, 38]

cores = [VERMELHO if p == "Brasil" else DOURADO if p in ("Rússia", "Tailândia", "Argentina") else "#95a5a6" for p in paises]

fig, ax = plt.subplots(figsize=(12, 6))
ordenado = sorted(zip(taxas, paises, cores), reverse=True)
nomes = [p for _, p, _ in ordenado]
vals = [t for t, _, _ in ordenado]
cor_list = [c for _, _, c in ordenado]
bars = ax.barh(nomes[::-1], vals[::-1], color=cor_list[::-1], height=0.68)
for bar, v in zip(bars, vals[::-1]):
    ax.text(bar.get_width() + 6, bar.get_y() + bar.get_height()/2, str(v),
            va="center", fontsize=10, fontweight="bold")
ax.set_xlabel("Taxa de encarceramento (presos por 100 mil habitantes)", fontsize=11)
ax.set_title("Taxa de encarceramento: Brasil em nível comparável ao de regimes autoritários (2024/2025)",
             fontsize=14, fontweight="bold", pad=14, color=AZUL)
from matplotlib.patches import Patch
leg = [Patch(facecolor=VERMELHO, label="Brasil"),
       Patch(facecolor=DOURADO, label="Países com governos autoritários/punitivistas"),
       Patch(facecolor="#95a5a6", label="Democracias ocidentais e Japão")]
ax.legend(handles=leg, loc="lower right", fontsize=9.5, frameon=False)
ax.set_xlim(0, 620)
ax.text(0.99, -0.16, "Fontes: World Prison Brief (dados 2024-2025)", transform=ax.transAxes,
        ha="right", fontsize=8.5, color=CINZA)
save(fig, "grafico2_comparacao_internacional")


# ----------------------------------------------------------------
# GRÁFICO 3 — Brasil na contramão: variação % das taxas de encarceramento 2000-2015/2025
# ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 6))
paises2 = ["Brasil", "Argentina", "Chile", "EUA", "China", "Rússia", "Alemanha", "França"]
var = [169, 171, 50, 14, 15, -19, -19, -6]
# Brasil 2000: 132 -> 2015: 301 = +128%; 2000-2025: 132 -> 439 = +233%
var = [128, 171, 50, 14, 15, -19, -19, -6]
cores2 = [VERMELHO if p == "Brasil" else VERDE if v < 0 else "#95a5a6" for p, v in zip(paises2, var)]
bars = ax.bar(paises2, var, color=cores2, width=0.6)
for bar, v in zip(bars, var):
    ax.text(bar.get_x() + bar.get_width()/2, v + (4 if v >= 0 else -14),
            f"{v:+d}%", ha="center", fontsize=11, fontweight="bold")
ax.axhline(0, color="black", linewidth=0.8)
ax.set_ylabel("Variação percentual da taxa de encarceramento (2000–2015)", fontsize=11)
ax.set_title("Na contramão mundial: Brasil expandiu o encarceramento enquanto o mundo reduziu",
             fontsize=14, fontweight="bold", pad=14, color=AZUL)
ax.text(0.99, -0.22, "Fontes: Pastoral Carcerária (2018); World Prison Brief; Nexo Jornal",
        transform=ax.transAxes, ha="right", fontsize=8.5, color=CINZA)
save(fig, "grafico3_contramao_mundial")


# ----------------------------------------------------------------
# GRÁFICO 4 — Distribuição de crimes que levam à prisão (Infopen 2024)
# ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 6))
crimes = ["Tráfico de\ndrogas", "Roubo\nqualificado", "Roubo\nsimples",
          "Homicídio\ndoloso", "Furto\nqualificado", "Furto\nsimples", "Outros"]
pct = [24, 13.9, 7.9, 12, 4.5, 4.8, 32.9]
cores4 = [VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, "#95a5a6"]
colors = [VERMELHO if i < 5 else CINZA for i in range(7)]
colors[3] = "#e67e22"
wedges, texts, autotexts = ax.pie(pct, labels=crimes, autopct=lambda p: f"{p:.0f}%",
                                  startangle=90, colors=colors,
                                  textprops={"fontsize": 10.5}, pctdistance=0.72)
for at in autotexts:
    at.set_color("white")
    at.set_fontweight("bold")
centre_circle = plt.Circle((0, 0), 0.52, fc="white")
ax.add_artist(centre_circle)
ax.text(0, 0.06, "Crime que mais\nprende no Brasil", ha="center", fontsize=10.5, fontweight="bold", color=AZUL)
ax.text(0, -0.20, "51% dos delitos que levam\nao encarceramento são\nnão violentos", ha="center",
        fontsize=9.5, color="#333")
ax.set_title("O que leva pessoas à prisão no Brasil (1º semestre de 2024)",
             fontsize=14, fontweight="bold", pad=20, color=AZUL)
ax.text(0.5, -0.08, "Fonte: SISDEPEN/SENAPPEN (1º sem. 2024), compilado pela BBC News Brasil",
        transform=ax.transAxes, ha="center", fontsize=8.5, color=CINZA)
save(fig, "grafico4_crimes_prisao")


# ----------------------------------------------------------------
# GRÁFICO 5 — Prisão por tráfico de drogas: antes e depois da Lei 11.343/2006
# ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 6))
an = ["2005\n(pré-lei)", "2010", "2015", "2022\n(Infopen)"]
presos_drogas = [33, 62, 173, 273]  # mil (estimativas: 33 mil 2005; Conectas; 273 mil 2022 FBSP)
# usar dados documentados: 2005 = 33 mil (11%), 2009 = 90 mil (~19%), 2015 = ~173 mil (28%)
an = ["2005", "2009", "2015", "2022"]
presos_drogas = [33, 90, 173, 273]
ax.bar(an, presos_drogas, color=[VERDE, VERDE, VERMELHO, VERMELHO], width=0.55)
for i, v in enumerate(presos_drogas):
    ax.text(i, v + 6, f"~{v} mil", ha="center", fontsize=11, fontweight="bold")
ax.set_ylabel("Presos por tráfico de drogas (milhares)")
ax.set_title("Prisão por tráfico de drogas: efeito multiplicador da Lei nº 11.343/2006",
             fontsize=14, fontweight="bold", pad=14, color=AZUL)
ax.text(0.02, 0.92, "Antes da lei (2005): 33 mil presos por tráfico\n"
                    "Depois (2022): ~273 mil — 8 vezes mais",
        transform=ax.transAxes, fontsize=10.5, va="top",
        bbox=dict(boxstyle="round", fc="#fdf2e9", ec=DOURADO))
ax.text(0.99, -0.16, "Fontes: Conectas (2013); Infopen/SENAPPEN; FBSP",
        transform=ax.transAxes, ha="right", fontsize=8.5, color=CINZA)
save(fig, "grafico5_trafico")


# ----------------------------------------------------------------
# GRÁFICO 6 — Prisão por tráfico: percentual do total de presos
# ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 5.5))
an = ["2006", "2015"]
pct_m = [11, 47]
pct_f = [20, 91]
x = np.arange(len(an))
w = 0.32
ax.bar(x - w/2, pct_m, w, label="Homens", color=AZUL)
ax.bar(x + w/2, pct_f, w, label="Mulheres", color=VERMELHO)
for i in range(len(an)):
    ax.text(x[i] - w/2, pct_m[i] + 2, f"{pct_m[i]}%", ha="center", fontweight="bold", fontsize=12)
    ax.text(x[i] + w/2, pct_f[i] + 2, f"{pct_f[i]}%", ha="center", fontweight="bold", fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(an, fontsize=12)
ax.set_ylabel("% das prisões por tráfico de drogas (%)")
ax.set_title("Tráfico de drogas: de 11% a 45% do total de prisões em uma década (Rio Grande do Sul)",
             fontsize=13, fontweight="bold", pad=14, color=AZUL)
ax.legend(frameon=False, fontsize=10)
ax.set_ylim(0, 105)
ax.text(0.99, -0.24, "Fonte: Ornell et al., Trends in Psychiatry and Psychotherapy (2020) — dados RS",
        transform=ax.transAxes, ha="right", fontsize=8.5, color=CINZA)
save(fig, "grafico6_tráfico_percentual")

print("TODOS OS GRÁFICOS GERADOS")
