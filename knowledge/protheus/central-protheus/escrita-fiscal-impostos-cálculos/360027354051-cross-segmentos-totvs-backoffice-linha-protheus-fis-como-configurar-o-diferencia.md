---
article_id: 360027354051
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 84a248d5841eda13006c47f261615db5575441a002bd879167ffb5c037c839f7
fetched_at: '2026-06-28T22:39:30.639576+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS-  Como configurar o
  diferencial de alíquotas (ICMS ST) com soma no total da Nota Fiscal Entrada?
type: support-article
updated_at: '2024-06-20T14:13:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027354051-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-diferencial-de-al%C3%ADquotas-ICMS-ST-com-soma-no-total-da-Nota-Fiscal-Entrada
---

**Dúvida**

Como configurar o diferencial de alíquotas (ICMS ST) com soma no total da Nota Fiscal Entrada?

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Informe no **Cadastro do Produto** ou da **Exceção Fiscal** o percentual de **ICMS-ST (MVA)** estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial:

TES

Calcula ICMS (F4\_ICM) = SIM

L. FISC. ICMS (F4\_LFICM) = TRIBUTADO

DIF. ALIQ. (F4\_COMPL) = NÃO

MATL CONSUMO (F4\_CONSUMO) = SIM

AGREGA SOLID. (F4\_INCSOL) = SIM

MARG. SOLID. (F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)

O FORNECEDOR deve ser de um Estado diferente do emitente (MV\_ESTADO) e preencha a Inscrição Estadual no SIGAMAT.EMP.

Note que o sistema irá demonstrar a alíquota Interna do Estado, no entanto o cálculo será realizado pelo diferencial.

**Exemplo:**

ICMS Próprio

Base de Cálculo = R$1000,00

Alíquota interestadual 12%

Valor do ICMS Próprio - R$120,00

Diferencial de alíquota:

Base de Cálculo = R$1000,00

Alíquota Interna 18%

Valor do ICMS complementar - R$60,00

Para tratar Base Dupla deverá configurar o parâmetro **MV\_UFBDST**com o estado da sua empresa.
