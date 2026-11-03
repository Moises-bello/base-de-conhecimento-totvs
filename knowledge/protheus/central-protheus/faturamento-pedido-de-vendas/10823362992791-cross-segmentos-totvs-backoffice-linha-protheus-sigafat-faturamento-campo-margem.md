---
article_id: 10823362992791
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 51748b831965f15b42c7a355d8ff86f54704a8e1c628357f2cfacb1dc0541191
fetched_at: '2026-06-28T22:38:42.601391+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Campo "Margem de contribuição (%)" na aba Rentabilidade da Planilha Financeira
  no Pedido de Vendas
type: support-article
updated_at: '2022-12-13T19:44:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10823362992791-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Campo-Margem-de-contribui%C3%A7%C3%A3o-na-aba-Rentabilidade-da-Planilha-Financeira-no-Pedido-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**

Qual a base da estruturação do campo "Margem de contribuição (%)" na aba Rentabilidade da Planilha Financeira no Pedido de Vendas?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Solução**

A margem de contribuição é calculada da seguinte forma:  
  
Margem de contribuição % = Lucro Bruto / Vlr. Presente \* 100  
Margem de contribuição % = 746,726412 / 909,226412 \* 100  
Margem de contribuição % =**82,127664**

**![](https://tdn.totvs.com/download/attachments/266963014/Planilha%20Margem.png?version=1&modificationDate=1475242983000&api=v2)**

Abaixo segue exemplo de utilização de produto que contém TES que valida impostos:

2ª. Fase – Cálculo de Impostos Sobre o Valor PRESENTE

**Desmembramento do cálculo**

Antes de iniciar o desmembramento do cálculo, vale ressaltar que a formula e semelhante a utilizada no documento de entrada (MATA103) para o cálculo do custo de entrada do produto, onde e amplamente utiliza as configurações da TES informada no pedido de vendas.

**Simulação de Valores:**

nVlrPres   := 197.44814307 (Valor Presente Total)

IT\_VALCMP  := 0.00 (Valor do ICMS Complementar)

IT\_VALICM  := 26.06 (Valor de ICMS)

IT\_VALIPI  := 0.00 (Valor do IPI)

SF4->F4\_IPI:= Não

Formula 1

nValTot := nVlrPres-IIf(SF4->F4\_IPI=="R",0,MaFisRet(nItem,"IT\_VALIPI"))+MaFisRet(nItem,"IT\_VALCMP")

nValTot := 197.44814307 – 0 + 0

nValTot := 197.44814307

**Algoritmo para cálculo dos impostos**

nValTot à Valor Presente

nValIcm àValor do ICMS

nValIpi à Valor do IPI

![](https://tdn.totvs.com/download/attachments/266963014/Rentabilidade.PNG?version=1&modificationDate=1496862819000&api=v2)

**Aplicando o algoritmo na TES 502**

nValTot := 197.45 (Valor Presente Total)

nValIcm := 26.06 (Valor de ICMS)

nValIpi := 0.00 (Valor do IPI)

SF4 → F4\_CREDIPI := Não

SF4 → F4\_CREDICM := Sim

Tipo Pedido = "N - Normal"

**Fórmula aplicada:**

Resultado:= nValTot – nValIcm

Resultado:= 197.44814307 – 26.06

Resultado:= 171.38814307

**Saiba Mais:**

**[FAT0139 Processo para utilização de Rentabilidade no Pedido de Vendas (MATA410)](https://tdn.totvs.com/x/RojpDw)**
