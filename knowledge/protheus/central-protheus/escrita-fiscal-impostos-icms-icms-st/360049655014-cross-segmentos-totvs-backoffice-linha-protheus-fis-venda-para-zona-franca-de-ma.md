---
article_id: 360049655014
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 476c4fed45baf357f1c9c89d5a183e91250d2b8239a9123b05e9f1bbe1420022
fetched_at: '2026-06-28T22:39:20.534017+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Venda para Zona Franca
  de Manaus apenas com Desconto de ICMS com ST Reduzido
type: support-article
updated_at: '2021-07-13T17:31:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049655014-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Venda-para-Zona-Franca-de-Manaus-apenas-com-Desconto-de-ICMS-com-ST-Reduzido
---

**Dúvida**Qual a configuração para Venda para Zona Franca de Manaus apenas com Desconto de ICMS com ST Reduzido ?  
   
 **Ambiente**Protheus - Todas as Versões

**Solução**

**Parâmetros:**

MV\_RPCBIZF = .T.

MV\_RPCBIUF  = Branco ou preenchido

MV\_DSZFSOL = .T.

MV\_UFSTZF = Branco ou Preenchido

**Clientes(Mata030)**

Tipo (A1\_TIPO) -  Definido com Solidário

Desc. P/ Suframa (A1\_CALCSUF) – Definido como SIM

Suframa (A1\_SUFRAMA) - Preenchido

Cód. Mun. ZF (A1\_CODMUN) - Preenchido

**Produtos (Mata010)**

Imp. Z. Franca (B1\_IMPZFRC) – Em branco

Solid. Saída (B1\_PICMRET) – Definido como 39%

**Tipos de Entrada e Saída (Mata080)**

Calc. ICMS (F4\_ICM) – Definido como SIM

Livro Fiscal ICMS (F4\_LFICM)  - Definido como Outros

Material de Consumo (F4\_CONSUMO) – Definido como Não

Ded.ICM.ST  (F4\_ICMSTMT) - Vazio

PIS Z.Franca (F4\_PISDSZF) e COFINS Z.F.( F4\_COFDSZF)  - Definido como 2

PIS/COFINS (F4\_PISCOF) -  Definido como AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) – Definido como DEBITA.

%Red.ICMS ST (F4\_BSICMST) – Definido como 58,33%

Mot. Desone (F4\_MOTICM) - 7 suframa

Red.Carg.Trb (F4\_APLIRED) – Não

**Exemplo de cálculo:**

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

 Desconto de ICMS : R$ 70,00

 Valor da Operação: R$ 1.000,00 – R$ 70,00 = R$ 930,00

Aplicação do MVA: R$ 930,00 \* 39% = R$ 362,70

Base de Cálculo do ICMS ST: R$ 930,00 + R$ 362,70= R$ 1.292,70

Base Reduzida: R$ 1.292,70\* 58,33% = R$ 754,03

Cálculo do Imposto: R$ 754,03\* 17% = R$ 128,18

Valor do ICMS ST: R$ 128,18 – R$ 70,00 = R$ 58,18

Valor total da nota: R$ 930 + R$ 58,18 = R$ 988,18
