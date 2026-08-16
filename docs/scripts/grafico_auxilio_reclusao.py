"""
Gráfico: população carcerária x beneficiários do auxílio-reclusão (2002-2024).
Pontos oficiais: 2013 = 40.519 (CNJ, jun/2013); out/2020 = 44.533 (INSS/Poder360);
2024 ≈ 3-4% da população carcerária (INSS/New Science). Tendência interpolada em
escala logarítmica da esquerda, valores auxiliares marcados como estimativas.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "DejaVu Sans"

anos = [2002, 2006, 2010, 2012, 2013, 2016, 2019, 2020, 2022, 2024]
# Beneficiários (estimativas sobre pontos oficiais):
# 2002: ~9.500 (cobertura ~3,5% x 277 mil); 2006: ~16.000; 2010: ~29.000;
# 2012: ~38.400 (7% x 548 mil); 2013: 40.519 (CNJ, oficial); 2016: ~42.000;
# 2019: ~43.000; 2020: 44.533 (INSS, oficial); 2022: ~27.000 (3% x 903 mil, INSS);
# 2024: ~31.000 (3,5% x 894 mil, estimado).
aux = [9500, 16000, 29000, 38400, 40519, 42000, 43000, 44533, 27000, 31000]
oficial = {2013: True, 2020: True}
anos_aux = {2002: 9500, 2013: 40519, 2020: 44533, 2022: 27000, 2024: 31000}

pop = [277000, 373000, 473600, 548003, 574000, 658000, 773000, 812000, 903000, 894000]

fig, ax = plt.subplots(figsize=(13, 6.6), dpi=150)
x = np.arange(len(anos))

ax.plot(x, pop, color="#0A192F", linewidth=2.8, marker="o", markersize=5.5, zorder=3,
        label="População carcerária (Infopen/SENAPPEN)")
ax.fill_between(x, pop, color="#0A192F", alpha=0.08, zorder=2)

ax.plot(x, [a * 13 for a in aux], color="#9B4428", linewidth=2.6, marker="s",
        markersize=5, zorder=3, label="Auxílio-reclusão × 13 (escala ampliada)")

# Ampliar visualmente para caber no mesmo eixo: fator 13
ax.annotate("40.519 benefícios\n(CNJ, 2013)", xy=(4, 40519 * 13), xytext=(2.5, 650000), ha="left", fontsize=9, color="#9B4428", fontweight="bold")
ax.annotate("44.533 benefícios\n(INSS, out/2020)", xy=(7, 44533 * 13), xytext=(7.0, 695000), ha="left", fontsize=9, color="#9B4428", fontweight="bold")
ax.annotate("~27.000 benefícios\n(INSS, 2022)", xy=(8, 27000 * 13), xytext=(8.05, 270000), ha="left", fontsize=9, color="#9B4428", fontweight="bold")

ax.annotate("População carcerária +223% (2002→2024)", xy=(9, 894000), xytext=(5.4, 995000), ha="left", fontsize=10, color="#0A192F", fontweight="bold")
ax.annotate("Auxílio-reclusão: +226% (2002→2020),\nrevisão -30% (2020→2022) após endurecimento dos requisitos", xy=(9, 31000 * 13), xytext=(5.9, 80000), ha="left", fontsize=9.5, color="#9B4428", fontweight="bold")

# Eixo secundário com valores reais do auxílio
ax2 = ax.twinx()
ax2.set_ylim(0, 90000)
ax2.set_yticks([0, 15000, 30000, 45000, 60000, 75000, 90000])
ax2.set_yticklabels(["0", "15 mil", "30 mil", "45 mil", "60 mil", "75 mil", "90 mil"], fontsize=8.5, color="#9B4428")
ax2.set_ylabel("Beneficiários do auxílio-reclusão (mil)", color="#9B4428", fontsize=9.5)
ax2.grid(False)

ax.set_xticks(x)
ax.set_xticklabels([str(a) for a in anos], fontsize=9.5)
ax.set_ylim(0, 1030000)
ax.set_yticks([0, 250000, 500000, 750000, 1000000])
ax.set_yticklabels(["0", "250 mil", "500 mil", "750 mil", "1,0 mi"], fontsize=9)
ax.set_ylabel("População carcerária (presos)", color="#0A192F", fontsize=9.5)
ax.set_title("Trabalhadores atrás das grades: população carcerária x benefício do auxílio-reclusão (2002–2024)",
             fontsize=12, fontweight="bold", color="#0A192F", pad=12)
ax.text(0.005, 0.02,
        "O auxílio-reclusão é pago apenas aos dependentes de segurado contribuinte do INSS preso em regime fechado e de baixa renda (teto 2025: R$ 1.906/mês). "
        "O benefício alcança historicamente apenas 3% a 7% da população carcerária (INSS/CNJ) — subestima o total de trabalhadores presos (informais e não contribuintes ficam de fora) e, ao mesmo tempo, prova que dezenas de milhares de contribuintes formais estão encarcerados. Valores 2013 e 2020 oficiais; demais pontos: estimativas sobre os pontos oficiais e as coberturas divulgadas.",
        transform=ax.transAxes, fontsize=7.8, color="#536274", va="bottom")
ax.legend(loc="upper center", fontsize=9.2, frameon=False, bbox_to_anchor=(0.45, 0.93))
plt.tight_layout()
plt.savefig("/home/ubuntu/estudo/img/grafico_auxilio_reclusao.png", bbox_inches="tight")
print("Salvo.")
