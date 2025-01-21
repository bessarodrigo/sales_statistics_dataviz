import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

def composicao_histograma_boxplot(dataframe, coluna, intervalos="auto", titulo="Título do Gráfico", nome_arquivo="distribuicao.png", salvar=False):
    pasta_imagens = os.path.join(os.getcwd(), "images")
    if salvar and not os.path.exists(pasta_imagens):
        os.makedirs(pasta_imagens)
    
    fig, (ax1, ax2) = plt.subplots(
        nrows=2, 
        ncols=1, 
        sharex=True,
        gridspec_kw={
            "height_ratios": (0.15, 0.85), # proporção (tamanho) dos gráficos
            "hspace": 0.02 # espaço entre os gráficos
        }
    )

    sns.boxplot(
        data=dataframe, 
        x=coluna, 
        showmeans=True,  
        meanline=True, # traço da média no boxplot
        meanprops={"color": "C1", "linewidth": 1.5, "linestyle": "--"}, # propriedades do traço da média no boxplot
        medianprops={"color": "C2", "linewidth": 1.5, "linestyle": "-"}, # propriedades do traço da mediana no boxplot
        ax=ax1,
    )

    sns.histplot(data=dataframe, x=coluna, kde=True, bins=intervalos, ax=ax2)

    for ax in (ax1, ax2):
        ax.grid(True, linestyle="--", color="gray", alpha=0.5)
        ax.set_axisbelow(True)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xlabel("")
        ax.set_ylabel("")

    ax2.axvline(dataframe[coluna].mean(), color="C1", linestyle="--", label="Média")
    ax2.axvline(dataframe[coluna].median(), color="C2", linestyle="--", label="Mediana")
    ax2.axvline(dataframe[coluna].mode()[0], color="C3", linestyle="--", label="Moda") # A moda pede o índice

    ax2.legend()
    
    fig.suptitle(titulo, fontsize=14, fontweight="bold", color="Gray")
    
    if salvar:
        caminho_arquivo = os.path.join(pasta_imagens, nome_arquivo)
        plt.savefig(caminho_arquivo, dpi=300, bbox_inches="tight")
        print(f"Gráfico salvo em: {caminho_arquivo}")

    plt.show()