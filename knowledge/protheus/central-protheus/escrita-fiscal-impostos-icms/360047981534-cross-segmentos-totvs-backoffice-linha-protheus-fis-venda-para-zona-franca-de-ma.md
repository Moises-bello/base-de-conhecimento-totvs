---
article_id: 360047981534
category: Escrita Fiscal - Impostos - ICMS
content_hash: 5bb952fd63e5d6aaccbcbd5f880bf493a16b5dd16f173bb07278dc67bc6f1996
fetched_at: '2026-06-28T22:39:24.268902+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Venda para Zona Franca
  de Manaus com Desconto de ICMS, PIS e COFINS com ST - SUFRAMA
type: support-article
updated_at: '2021-07-28T03:12:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047981534-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Venda-para-Zona-Franca-de-Manaus-com-Desconto-de-ICMS-PIS-e-COFINS-com-ST-SUFRAMA
---

**Dúvida**

Qual a configuração para  emitir nota fiscal com desconto ICMS, Pis, Cofins com ICMS-ST - SUFRAMA?  
  
**Ambiente**

Todas as Versões do Protheus  
  
**Solução**

Configurações:

MV\_RPCBIZF = .T.

MV\_RPCBIUF = Branco ou preenchido

MV\_DSZFSOL  = .T.

MV\_UFSTZF  = Preenchido

**Clientes(Mata030)**

Tipo (A1\_TIPO) -  Definido como Solidário

Desc. P/ Suframa (A1\_CALCSUF) – Definido como SIM

Suframa (A1\_SUFRAMA) - Preenchido

Cód. Mun. ZF (A1\_CODMUN) - Preenchido

**Produtos (Mata010)**

Imp. Z. Franca (B1\_IMPZFRC) – Não ou Em branco

Solid. Saída (B1\_PICMRET) – Definido como 30%

 

**Tipos de Entrada e Saída (Mata080)**

Calc. ICMS (F4\_ICM) – Definido como SIM

Livro Fiscal ICMS (F4\_LFICM)  - Definido como Outros

Material de Consumo (F4\_CONSUMO) – Definido como Não

Ded.ICM.ST  (F4\_ICMSTMT) - Vazio

PIS Z.Franca (F4\_PISDSZF) e COFINS Z.F.( F4\_COFDSZF)  - Definido como 2

PIS/COFINS (F4\_PISCOF) -  Definido como AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) – Definido como CALCULA.

Mot. Desone (F4\_MOTICM) - 7 suframa

**Exemplo de cálculo:**

Valor de Mercadorias: R$ 1.000,00

Alíquota de ICMS: 7%

Alíquota de PIS: 1,65%

Alíquota de Cofins: 7,6%

Base de Cálculo do Pis/Cofins: R$ 1.000,00

Valor do Pis: R$ 1.000,00 \* 1,65% = R$ 16,50

Valor do Cofins: R$ 1.000,00 \*7,6% = R$ 76,00

Base de Cálculo de ICMS: R$ 1.000,00 – R$ 16,50 – R$ 76,00 = R$ 907,50

Valor de ICMS: R$ 907,50 \* 7% = R$ 63,53

Desconto de ICMS : R$ 63,53

Valor da Operação: R$ 907,50 – R$ 63,53 = R$ 843,97

Aplicação do MVA: R$ 843,97 \* 30% = R$ 253,19

Base de Cálculo do ICMS ST: R$ 843,97 + R$ 253,19 = R$ 1.097,16

Cálculo do Imposto: R$ 1.097,16 \* 17% = R$ 186,52

Valor do ICMS ST: R$ 186,52 – R$ 63,53 = R$ 122,99

Valor total da nota: R$ 843,97 + R$ 122,99 = R$ 966,96
