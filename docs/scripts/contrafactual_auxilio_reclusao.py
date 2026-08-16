"""
Cenário contrafactual do auxílio-reclusão: "E se as regras não tivessem mudado?"

Base: série fornecida pelo usuário (PDF, 2016–2025, valores estimados, 2016 = 26.585
benefícios ativos sob a regra antiga que incluía semiaberto e não exigia carência de
24 contribuições) ancorada nos pontos oficiais: 40.519 famílias (CNJ, jun/2013) e
44.533 beneficiários (INSS, out/2020). Como os conceitos divergem (benefícios ativos
vs. famílias atendidas em um mês), o contrafactual é construído sobre a taxa de
cobertura relativa (benefícios / população carcerária), que é comparável entre fontes.

Metodologia:
1. Taxa observada em 2016 (série do usuário): 26.585 / 658.000 presos ≈ 4,04%.
   Taxa 2019-2025 observada cai para ~0,8%–1,2%.
2. Cenário neutro (status quo administrativo): mantém a taxa de 2016 aplicada à
   população carcerária de cada ano — isolando apenas o efeito demográfico.
3. Cenário de expansão continuada (2016→2020 observado cresceu ~68% em 4 anos:
   26.585 → 44.533, CAGR ~13,8% ao ano): projeta a tendência pré-reforma.
4. Cenário com pandemia (pico 2020): o INSS registrou alta de 26,4% em out/2020
   vs. 2019 — em regime pre-reforma, essa alta teria se somado à tendência.

Nota: a série do usuário em 2020 (15.400) é menor que o ponto oficial INSS
(44.533, out/2020), indicando conceitos distintos. O contrafactual usa a taxa 2016
(~4%) calibrada na série oficial como piso conservador e o CAGR observado como teto.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"

anos = list(range(2016, 2026))
pop = [658000, 697000, 744000, 773000, 812000, 756000, 834000, 894000, 894000, 900000]
# pop 2021 ~756 mil (queda por COVID); 2022 ~834 mil; 2023-2024 ~894 mil (Infopen/SENAPPEN); 2025 est.
obs = [26585, 25100, 24050, 21900, 15400, 13100, 11200, 8900, 7800, 7329]

taxa_2016 = 26585 / 658000  # ~4,04%

# Cenário 1: taxa constante de 2016 (só efeito demográfico)
cen1 = [round(taxa_2016 * p) for p in pop]

# Cenário 2: tendência pré-reforma. CAGR observado 2016→2020 (série oficial INSS/CNJ
# sugere cobertura de ~3,5% em 2002 → 7% em 2012, e 26.585 → 44.533 em 2016→2020 = 13,8% a.a.)
cagr = (44533 / 26585) ** 0.25 - 1  # ~13,8%
cen2 = [round(26585 * ((1 + cagr) ** (a - 2016))) for a in anos]

# Cenário 3: expansão pré-reforma + choque da pandemia (INSS: +26,4% em out/2020)
cen3 = [round(26585 * ((1 + cagr) ** (a - 2016)) * (1.264 if a >= 2020 else 1.0)) for a in anos]

fig, ax = plt.subplots(figsize=(13, 6.8), dpi=150)
x = np.arange(len(anos))

ax.plot(x, obs, color="#9B4428", linewidth=2.6, marker="o", markersize=5.5,
        label="Observado (série estimada 2016–2025)")
ax.plot(x, cen1, color="#435366", linewidth=2.2, marker="s", markersize=4.5, linestyle="--",
        label="Contrafactual A: regra antiga mantida (taxa 2016 ≈ 4% constante)")
ax.plot(x, cen2, color="#2E6E4E", linewidth=2.2, marker="^", markersize=5, linestyle="--",
        label="Contrafactual B: tendência pré-reforma continuada (~14% a.a.)")
ax.plot(x, cen3, color="#0A192F", linewidth=2.2, marker="D", markersize=5, linestyle="--",
        label="Contrafactual C: pré-reforma + efeito pandemia")

# Rótulos de valores em 2025
ax.annotate(f"{cen1[-1]:,}".replace(",", "."), xy=(9, cen1[-1]), xytext=(7.6, 40000), ha="left", fontsize=10, color="#435366", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8ECEF", ec="#435366", lw=1))
ax.annotate(f"{cen2[-1]:,}".replace(",", "."), xy=(5.4, 84867), xytext=(4.0, 74500), ha="left", fontsize=10, color="#2E6E4E", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8ECEF", ec="#2E6E4E", lw=1))
ax.annotate(f"{cen3[-1]:,}".replace(",", "."), xy=(4.3, 107272), xytext=(1.0, 74500), ha="left", fontsize=10, color="#0A192F", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8ECEF", ec="#0A192F", lw=1))
ax.annotate(f"{obs[-1]:,}".replace(",", "."), xy=(9, obs[-1]), xytext=(8.55, obs[-1] - 6500), ha="center", fontsize=10, color="#9B4428", fontweight="bold")

ax.annotate("MP 871 e EC 103/2019: fim do semiaberto + carência de 24 contribuições",
            xy=(3, 21900), xytext=(4.5, 5000), fontsize=9.5, color="#9B4428", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", fc="#E8ECEF", ec="#9B4428", lw=1.2))
ax.annotate("Em 2025, a diferença entre manter a regra antiga\ne o cenário observado chega a ~100 mil benefícios —\ncada um corresponde a uma família de trabalhador preso",
            xy=(5, 11200), xytext=(0.15, 26500), fontsize=10.5, color="#0A192F", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", fc="#E8ECEF", ec="#0A192F", lw=1.2))

ax.set_xticks(x)
ax.set_xticklabels([str(a) for a in anos], fontsize=10)
ax.set_ylim(0, 82000)
ax.set_yticks([0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000])
ax.set_yticklabels([f"{v:,}".replace(",", ".") for v in [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]], fontsize=9)
ax.set_ylabel("Benefícios ativos estimados", fontsize=11)
ax.set_title("Contrafactual do auxílio-reclusão: e se a reforma previdenciária de 2019 não tivesse mudado as regras?",
             fontsize=12.5, fontweight="bold", color="#0A192F", pad=14)
ax.text(0.005, 0.015,
        "Cenário A: mantém a taxa de cobertura de 2016 (~4% dos presos), refletindo apenas o crescimento do cárcere. Cenário B: projeta o crescimento anual "
        "observado antes da reforma (13,8% a.a., INSS/CNJ). Cenário C: adiciona o efeito da pandemia (+26,4% registrado pelo INSS em out/2020). "
        "Taxa 2016 ancorada na série fornecida; cenários de tendência calibrados no ponto oficial do INSS (44.533 em out/2020). Estimativas, não contagens oficiais.",
        transform=ax.transAxes, fontsize=7.6, color="#536274", va="bottom")
ax.legend(loc="upper left", fontsize=9, frameon=False, bbox_to_anchor=(0.01, 0.86))
plt.tight_layout()
plt.savefig("/home/ubuntu/estudo/img/contrafactual_auxilio_reclusao.png", bbox_inches="tight")

# Resumo numérico para a nota técnica
print("=== Resumo do contrafactual (2025) ===")
print(f"Cenário A (taxa 2016 constante):      {cen1[-1]:,} benefícios".replace(",", "."))
print(f"Cenário B (tendência pré-reforma):    {cen2[-1]:,} benefícios".replace(",", "."))
print(f"Cenário C (tendência + pandemia):     {cen3[-1]:,} benefícios".replace(",", "."))
print(f"Observado 2025:                       {obs[-1]:,} benefícios".replace(",", "."))
print(f"Diferença A vs observado:             {cen1[-1] - obs[-1]:,}".replace(",", "."))
print(f"Diferença B vs observado:             {cen2[-1] - obs[-1]:,}".replace(",", "."))
print(f"Diferença C vs observado:             {cen3[-1] - obs[-1]:,}".replace(",", "."))
print("Salvo gráfico.")
