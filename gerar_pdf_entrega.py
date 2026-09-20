"""
Script gerador do PDF oficial de entrega da atividade de Sistematização.
Gera o arquivo: SISTEMATIZACAO_MEC_Sistematizacao-MMC.pdf
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY


def gerar_pdf(nome_arquivo="SISTEMATIZACAO_MEC_Sistematizacao-MMC.pdf"):
    caminho_saida = os.path.abspath(nome_arquivo)
    
    # Margens de 1.5 cm para garantir encaixe perfeito e legível
    doc = SimpleDocTemplate(
        caminho_saida,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Estilos customizados
    titulo_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1A365D")
    )

    subtitulo_style = ParagraphStyle(
        "DocSubTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#2B6CB0")
    )

    secao_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#1A365D"),
        spaceBefore=6,
        spaceAfter=3
    )

    subsecao_style = ParagraphStyle(
        "SubSectionHeading",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor("#2C5282"),
        spaceBefore=4,
        spaceAfter=2
    )

    texto_style = ParagraphStyle(
        "BodyJustified",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#2D3748")
    )

    item_style = ParagraphStyle(
        "ListItem",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#2D3748"),
        leftIndent=10
    )

    tabela_texto = ParagraphStyle(
        "TableText",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=10,
        textColor=colors.HexColor("#1A202C")
    )

    tabela_cabecalho = ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=10,
        textColor=colors.white
    )

    elementos = []

    # Cabeçalho Principal
    elementos.append(Paragraph("SISTEMATIZACAO - MATEMATICA E ESTATISTICA PARA COMPUTACAO", titulo_style))
    elementos.append(Spacer(1, 2))
    elementos.append(Paragraph("<b>Professor:</b> Romes | <b>Grupo:</b> Sistematizacao-MMC", subtitulo_style))
    elementos.append(Spacer(1, 4))
    elementos.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2B6CB0"), spaceAfter=6))

    # 1. Identificação dos Componentes
    elementos.append(Paragraph("1 - Identificacao dos Componentes da Equipe", secao_style))
    
    dados_equipe = [
        [Paragraph("<b>Nome Completo</b>", tabela_cabecalho), Paragraph("<b>Matricula</b>", tabela_cabecalho), Paragraph("<b>GitHub</b>", tabela_cabecalho)],
        [Paragraph("Rafael R. Leite", tabela_texto), Paragraph("72501342", tabela_texto), Paragraph("@RafaelRLeite", tabela_texto)],
        [Paragraph("Matheus Brito", tabela_texto), Paragraph("<i>72650414</i>", tabela_texto), Paragraph("@matheusbrito090108", tabela_texto)],
        [Paragraph("Fernando Luca", tabela_texto), Paragraph("72650534", tabela_texto), Paragraph("@fernandoluca015", tabela_texto)],
        [Paragraph("Italo da Silva Ferraz", tabela_texto), Paragraph("<i>72650588</i>", tabela_texto), Paragraph("@Italo-917", tabela_texto)],
    ]
    tabela = Table(dados_equipe, colWidths=[200, 150, 190])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.HexColor("#EDF2F7")]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    elementos.append(tabela)
    elementos.append(Spacer(1, 5))

    # 2. Links Obrigatórios
    elementos.append(Paragraph("2 - Links do Projeto e Acessos", secao_style))
    dados_links = [
        [Paragraph("<b>Item</b>", tabela_cabecalho), Paragraph("<b>Descricao e URL</b>", tabela_cabecalho)],
        [Paragraph("<b>Dados Crus (Dataset)</b>", tabela_texto), Paragraph('<font color="#2B6CB0"><u>https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj</u></font>', tabela_texto)],
        [Paragraph("<b>Repositorio da Solucao</b>", tabela_texto), Paragraph('<font color="#2B6CB0"><u>https://github.com/Sistematizacao-MMC/laboratorio-estatistico-interativo</u></font>', tabela_texto)],
        [Paragraph("<b>Video de Demonstracao</b>", tabela_texto), Paragraph('<font color="#2B6CB0"><u>https://drive.google.com/file/d/1x0gclwBwPL2EEWiOrFqr05dJ6aO1dxGR/view?usp=sharing</u></font>', tabela_texto)]
    ]
    tabela_l = Table(dados_links, colWidths=[150, 390])
    tabela_l.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.HexColor("#EDF2F7")]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    elementos.append(tabela_l)
    elementos.append(Spacer(1, 5))

    # 3. Resumo Executivo
    elementos.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E0"), spaceAfter=5))
    elementos.append(Paragraph("3 - Resumo Executivo da Solucao", secao_style))

    elementos.append(Paragraph("<b>A. Dataset Escolhido e Justificativa:</b>", subsecao_style))
    elementos.append(Paragraph(
        "Foi selecionada a base de dados abertos do <b>Cadastro Nacional da Pessoa Juridica (CNPJ)</b> da Receita Federal do Brasil. "
        "Com mais de 49 milhoes de registros cadastrais, este conjunto fornece um ambiente realista para explorar distribuicoes financeiras complexas com alta assimetria e caudas pesadas (<i>heavy-tailed</i>), permitindo investigar o impacto de valores atipicos em tomadas de decisao estatistica.",
        texto_style
    ))
    elementos.append(Spacer(1, 3))

    elementos.append(Paragraph("<b>B. Arquitetura e Modulos Implementados (Nucleo Autoral 'na unha'):</b>", subsecao_style))
    elementos.append(Paragraph(
        "A aplicacao foi estruturada em Python desacoplando a interface grafica (<b>Streamlit</b>) do nucleo estatistico autoral (<b><code>src/core/pystatistics.py</code></b>). Todas as funcoes matematicas foram codificadas manualmente e validadas contra <i>NumPy</i> e <i>SciPy</i> via suite de 19 testes automatizados com <i>pytest</i>.",
        texto_style
    ))
    
    elementos.append(Paragraph("- <b>Modulo 0 (Carga e Pre-processamento):</b> Suporte a upload de CSV, leitura de arquivos locais e dataset de demonstracao integrado com 1.000 empresas simuladas.", item_style))
    elementos.append(Paragraph("- <b>Modulo 2 (Estatistica Descritiva Interativa):</b> Tendencia central, dispersao, separatrizes, boxplot interativo, tabela de frequencia e deteccao de outliers pelo metodo IQR (Tukey).", item_style))
    elementos.append(Paragraph("- <b>Modulo 3 (Probabilidade e Monte Carlo):</b> Simulacoes interativas da Lei dos Grandes Numeros (LGN) e do Teorema Central do Limite (TCL) com controle de parametros.", item_style))
    elementos.append(Paragraph("- <b>Modulo 4 (Distribuicoes Teoricas):</b> Ajuste e sobreposicao de curvas de densidade teoricas (Normal, Exponencial e Uniforme) sobre os histogramas reais.", item_style))
    elementos.append(Paragraph("- <b>Modulo 5 (Correlacao e Regressao Linear Simples):</b> Coeficiente de Pearson, reta por Minimos Quadrados Ordinarios (MQO), equacoes em LaTeX, R2, predicao interativa e alerta de causalidade.", item_style))
    elementos.append(Paragraph("- <b>Modulo 6 (Relatorio de Descobertas):</b> Apresentacao analitica detalhada dos resultados diretamente na interface.", item_style))
    elementos.append(Spacer(1, 4))

    elementos.append(Paragraph("<b>C. As 3 Principais Descobertas Estatisticas:</b>", subsecao_style))
    elementos.append(Paragraph(
        "- <b>1. Assimetria Extrema em Variaveis Financeiras:</b> As variaveis de <i>Capital Social</i> e <i>Faturamento</i> apresentam media expressivamente superior a mediana (Media >> Mediana) e Coeficiente de Variacao (CV) superior a 150%. Os dados aderem com muito maior precisao a Distribuicao Exponencial/Pareto do que a Normal, demonstrando que menos de 2% das empresas concentram a maior parte do volume de capital (outliers severos). A mediana e o IQR comprovam ser medidas muito mais confiaveis que a media aritmetica.",
        item_style
    ))
    elementos.append(Spacer(1, 2))
    elementos.append(Paragraph(
        "- <b>2. Validacao Experimental do Teorema Central do Limite (TCL):</b> Mesmo partindo de populacoes com distribuicoes extremamente assimetricas ou multimodais, a distribuicao amostral das medias (X_barra) convergiu rigorosamente para uma Distribuicao Normal quando o tamanho amostral atingiu n >= 30, com erro padrao convergindo para sigma/sqrt(n). Isso legitima a aplicacao de intervalos de confianca e inferencia parametrica na base.",
        item_style
    ))
    elementos.append(Spacer(1, 2))
    elementos.append(Paragraph(
        "- <b>3. Relacao Linear por MQO e Alerta de Causalidade:</b> O modelo bivariado entre Capital Social e Faturamento indicou correlacao linear positiva moderada a forte (r > 0.60) e R2 explicativo. Contudo, reforcou-se o postulado fundamental de que <i>correlacao nao implica causalidade</i>: variaveis ocultas de confusao (setor de atividade, maturidade de mercado e localizacao) exercem papel determinante sobre o desempenho economico.",
        item_style
    ))

    try:
        doc.build(elementos)
        print(f"PDF gerado com sucesso em: {caminho_saida}")
    except PermissionError:
        caminho_alt = os.path.abspath("SISTEMATIZACAO_MEC_Sistematizacao-MMC_novo.pdf")
        doc = SimpleDocTemplate(
            caminho_alt,
            pagesize=letter,
            leftMargin=36,
            rightMargin=36,
            topMargin=36,
            bottomMargin=36
        )
        doc.build(elementos)
        print(f"O arquivo original estava aberto. PDF gerado com sucesso em: {caminho_alt}")


if __name__ == "__main__":
    gerar_pdf()
