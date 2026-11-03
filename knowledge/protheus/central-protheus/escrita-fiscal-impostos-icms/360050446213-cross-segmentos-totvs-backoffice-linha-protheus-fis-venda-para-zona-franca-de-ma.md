---
article_id: 360050446213
category: Escrita Fiscal - Impostos - ICMS
content_hash: 6b3a6594d66692ca66ea539809d291712df3b291c90b042ba4d39ba97a4d8244
fetched_at: '2026-06-28T22:39:24.254745+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Venda para Zona Franca
  de Manaus apenas com desconto de ICMS
type: support-article
updated_at: '2021-07-28T02:43:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050446213-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Venda-para-Zona-Franca-de-Manaus-apenas-com-desconto-de-ICMS
---

**Dúvida**Qual a configuração para efetuar uma venda para Zona Franca de Manaus apenas com Desconto de ICMS?

**Ambiente**Protheus - Todas as Versões  
  
**Solução**

**Parâmetros:**

MV\_RPCBIZF = .T.

MV\_RPCBIUF  = Branco ou preenchido

MV\_DSZFSOL  = .F. ou .T.

MV\_UFSTZF  = Branco ou preenchido

**Clientes(Mata030)**

Tipo (A1\_TIPO) -  Definido com Revendedor

Desc. P/ Suframa (A1\_CALCSUF) – Definido como SIM

Suframa (A1\_SUFRAMA) - Preenchido

Cód. Mun. ZF (A1\_CODMUN) - Preenchido

**Produtos (Mata010)**

Imp. Z. Franca (B1\_IMPZFRC) – Em branco

**Tipos de Entrada e Saída (Mata080)**

Calc. ICMS (F4\_ICM) – Definido como SIM

Livro Fiscal ICMS (F4\_LFICM)  - Definido como Outros

Material de Consumo (F4\_CONSUMO) – Definido como Não

Ded.ICM.ST  (F4\_ICMSTMT) - Vazio

PIS Z.Franca (F4\_PISDSZF) e COFINS Z.F.( F4\_COFDSZF)  - Definido como 2

PIS/COFINS (F4\_PISCOF) -  Definido como AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) – Definido como DEBITA.

Mot. Desone (F4\_MOTICM) - 7 suframa

Valor de Mercadorias: R$ 1.000,00

Alíquota de ICMS: 7%

Alíquota de PIS: 1,65%

Alíquota de Cofins: 7,6%

Base de Cálculo do Pis/Cofins: R$ 1.000,00

 Valor do Pis: R$ 1.000,00 \* 1,65% = R$ 16,50

 Valor do Cofins: R$ 1.000,00 \*7,6% = R$ 76,00

\*\* (Valores de Pis e Cofins são calculados, mas não são descontados)

 Base de Cálculo de ICMS: R$ 1.000,00

 Valor de ICMS: R$ 1.000,00 \* 7% = R$ 70,00

 Valor da Operação: R$ 1.000,00 – R$ 70,00 = R$ 930,00
