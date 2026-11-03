---
article_id: 360048691173
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 6f09c073140f88eb21660ff356373a6029b6c65fa92261fb70e58e54467a287a
fetched_at: '2026-06-28T22:39:36.940575+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Descontar PIS e COFINS
  antes do ICMS para o cálculo do SUFRAMA
type: support-article
updated_at: '2021-06-22T13:13:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048691173-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Descontar-PIS-e-COFINS-antes-do-ICMS-para-o-c%C3%A1lculo-do-SUFRAMA
---

**Dúvida**Como descontar o PIS e COFINS antes do ICMS para o cálculo SUFRAMA?  
  
**Ambiente**

Todas as Versões Protheus  
  
**Solução**

**Configurações:**

**Parâmetros**:

MV\_RPCBIZF = .T.

MV\_RPCBIUF = Preenchido

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

Valor do Pis: R$ 1.000,00 \* 1,65% = R$ 16,50

Valor do Cofins: R$ 1.000,00 \*7,6% = R$ 76,00

Base de Cálculo de ICMS: R$ 1.000,00 – R$ 16,50 – R$ 76,00 = R$ 907,50

Valor de ICMS: R$ 907,50 \* 7% = R$ 63,53

Desconto de ICMS : R$ 63,53

Valor da Operação: R$ 907,50 – R$ 63,53 = R$ 843,97
