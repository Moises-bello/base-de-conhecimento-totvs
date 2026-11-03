---
article_id: 360047973474
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 3ad23224cb7a84921e40eec3a43b768ac60c060c237d6102fa6afa4e0538ae15
fetched_at: '2026-06-28T22:39:20.345673+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Calcular ICMS antes
  de deduzir Pis e Cofins - SUFRAMA
type: support-article
updated_at: '2021-07-13T18:26:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047973474-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Calcular-ICMS-antes-de-deduzir-Pis-e-Cofins-SUFRAMA
---

**Dúvida**Como  calcular ICMS antes de deduzir Pis e Cofins - SUFRAMA?  
   
 **Ambiente**

Todas Versões Protheus  
  
**Solução**

MV\_RPCBIZF = .F.

MV\_RPCBIUF = Branco ou preenchido

**Clientes(Mata030)**

Tipo (A1\_TIPO) -  Definido como Revendedor

Desc. P/ Suframa (A1\_CALCSUF) – Definido como SIM

Suframa (A1\_SUFRAMA) - Preenchido

Cód. Mun. ZF (A1\_CODMUN) - Preenchido

**Produtos (Mata010)**

Imp. Z. Franca (B1\_IMPZFRC) – Não ou Em branco

**Tipos de Entrada e Saída (Mata080)**

Calc. ICMS (F4\_ICM) – Definido como SIM

Livro Fiscal ICMS (F4\_LFICM)  - Definido como Outros

Material de Consumo (F4\_CONSUMO) – Definido como Não

Ded.ICM.ST  (F4\_ICMSTMT) - Vazio

PIS Z.Franca (F4\_PISDSZF) e COFINS Z.F.( F4\_COFDSZF)  - Definido como 2

PIS/COFINS (F4\_PISCOF) -  Definido como AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) – Definido como CALCULA.

Mot. Desone (F4\_MOTICM) - 7 suframa

Exemplo de cálculo:

Valor de Mercadorias: R$ 1.000,00

Alíquota de ICMS: 7%

Alíquota de PIS: 1,65%

Alíquota de Cofins: 7,6%

Base de Cálculo do Pis/Cofins: R$ 1.000,00

1.000,00 x 7% = 70,00

Valor do Pis: R$ 1.000,00 \* 1,65% = R$ 16,50

Valor do Cofins: R$ 1.000,00 \*7,6% = R$ 76,00

Base de Cálculo de ICMS:

Valor da Operação: R$ 1.000,00 - 70,00 - 16,50 - 76,00 = 837,50
