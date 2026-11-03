---
article_id: 360024400711
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 0ab61fa6a1fba7823d766a18afd79c641bcc3864cadbe1611dbdc1cefe03f1b9
fetched_at: '2026-06-28T22:39:36.897398+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o
  cálculo do PIS, COFINS e CSLL retido?
type: support-article
updated_at: '2021-07-22T18:27:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024400711-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-c%C3%A1lculo-do-PIS-COFINS-e-CSLL-retido
---

**Dúvida**

Como configurar o calculo do PIS, COFINS e CSLL retido?

**Ambiente**

Protheus - Faturamento - Compras - A partir da versão 11.80  
  
  
**Solução**

Configuração necessária para gerar a nota:

NATUREZA

**Calcula PIS** (ED\_CALCPIS) = **Sim**

**Percentual de PIS**(ED\_PERCPIS) = **Informe a alíquota**

**Calcula COFINS**(ED\_CALCCOF) = **Sim**

**Percentual de COFINS**(ED\_PERCCOF) = **Informe a alíquota**

**Calcula CSLL**(ED\_CALCCSL) = **Sim**

**Percentual de CSLL** (ED\_PERCCSL) = **Informe a alíquota**

TES

**PIS/ COFINS**(F4\_PISCOF) = **Ambos**

**Créd. PIS/COF** (F4\_PISCRED) = **Não calcula**

**Gera Duplicata**(F4\_DUPLIC) =**Sim**

PRODUTO

**Retém PIS** (B1\_PIS) = **Sim**

**Retém COFINS**(B1\_COFINS) = **Sim**

**Retém CSLL**(B1\_CSLL) = **Sim**

**Ret. Operação**(B1\_RETOPER) = **Não**- Considera valor mínimo de retenção / **Sim** - Não considera valor mínimo de retenção

FORNECEDOR

**Rec. PIS** (A2\_RECPIS) = **Não**

**Rec. COFINS** (A2\_RECCOFI) = **Não**

**Rec. CSLL**(A2\_RECCSLL) = **Não**

CLIENTE

**Rec. PIS** (A1\_RECPIS) = **Sim**

**Rec. COFINS** (A1\_RECCOFI) = **Si****m**

**Rec. CSLL**(A1\_RECCSLL) = **Sim**

**Modo de abatimento do imposto** (A1\_ABATIMP) = **Cálculo do sistema**

**Parâmetros referentes à retenção PIS/COFINS/CSLL - Lei 10.925**

**MV\_RF10925:**Data de referência inicial, para que os novos procedimentos quanto à retenção de PIS/COFINS/CSLL sejam aplicados) **= 26/07/04**

**MV\_VL10925:**Valor máximo de pagamentos no período para dispensa da retenção de PIS/COFINS/CSLL **= 5000**

**MV\_RT10925:**Modo padrão de operação do Sistema quanto à retenção de PIS/COFINS/CSLL. (1=Calculado p/sistema, 2=Efetua Retenção sempre - 3=Não efetua retenção) **= 1**

**MV\_AC10925:**Controle de permissão para que o usuário altere o modo de retenção na janela cálculo de retenção - 1=Permite alteração - 2= Não permite alteração**= 1**

**MV\_AB10925:**Modo de retenção do PIS,COFINS e CSLL p/ C.Receber 1=Verif.retenção pelo valor da nota emitida - 2=Verif.retenção p/soma notas emitidas no período **= 2**

**MV\_MT10925:**Verifica base de retenção pelo total ou apenas pelos títulos que retiveram impostos.1=Todos 2=Somente os que retiveram PIS etc **= 1**

**MV\_BX10925 (Entrada):**Define o momento do tratamento da retenção dos impostos PIS COFINS e CSLL. **1= Na Baixa OU 2 = Na Emissão**

**MV\_BR10925 (Saída):**Define o momento do tratamento da retenção dos impostos PIS COFINS e CSLL. **1= Na Baixa OU 2 = Na Emissão**

**MV\_BS10925:**Indica se o cálculo da retenção será sobre a base do PIS/COFINS/CSLL ou pelo valor total da duplicata. 1=Valor da base; 2=Valor total **= 2**

**MV\_LJ10925:**Considerar para verificação de valores de retenção os valores de todas as lojas do cliente. Opções: 1 = Loja atual ou 2 = Todas as lojas **= 2**

**MV\_VRETPIS:**Valor mínimo para dispensa de retenção de PIS **= 0.00**

**MV\_VRETCOF:**Valor mínimo para dispensa de retenção de COFINS **= 0.00**

**MV\_VRETCSL:**Valor mínimo para dispensa de retenção de CSLL **= 0.00**

**MV\_RATPIS:**Rateio do imposto na entrada - **T. (Default) para ratear os impostos OU .F. para NÃO ratear.**

**MV\_RATCOF:**Rateio do imposto na entrada - **.T. (Default) para ratear os impostos OU .F. para NÃO ratear.**

**MV\_RATCSLL:**Rateio do imposto na entrada - **.T. (Default) para ratear os impostos OU .F. para NÃO ratear.**

**MV\_PISNAT:** Natureza para titulos referentes ao PIS :**"PIS"**

**MV\_COFINS:**Natureza para titulos referentes a COFINS : **"COFINS"**

**MV\_CSLL:**Natureza de Titulos de Pagamento de CSLL : **"CSLL"**

**MV\_AG10925:** Indica se os impostos do PCC serão aglutinados em um titulo apenas quando ocorrerem os três impostos num mesmo titulo.**1=Aglutina OU2=Não Aglutina 2**

Parâmetros referentes à retenção PIS/COFINS/CSLL - Lei 13.137

Adequação do Protheus para atender as alterações de regras de cálculo do Pis, Cofins e Csll de acordo com a Lei 13137/15 | Lei nº 13.137, de 19 de junho de 2015 vigente a partir do dia **22/06/2015.**

**MV\_VL13137:** Define o valor mínimo para retenção do Pis/Cofins/Csll de acordo com a Lei 13.137**= 10.00**

**MV\_VCPCCP:**Qual a data que sera considerada para a cumulatividade do PCC na Emissao. 1=Emissao, 2=Venc.Real, 3=Dt Contab.

**MV\_VCPCCR:**Qual a data que sera considerada para a cumulatividade do PCC na Emissao. 1=Emissao, 2=Venc.Real, 3=Dt Contab.
