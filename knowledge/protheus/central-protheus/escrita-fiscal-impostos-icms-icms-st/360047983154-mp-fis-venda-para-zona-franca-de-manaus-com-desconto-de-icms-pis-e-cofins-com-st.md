---
article_id: 360047983154
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: e1ce931fba6a1d41722b8e692972a0837b866a04d0112aaf939bddf0f5bdd301
fetched_at: '2026-06-28T22:39:20.575933+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: MP FIS - Venda para Zona Franca de Manaus com Desconto de ICMS, Pis e Cofins
  com ST Reduzido
type: support-article
updated_at: '2021-04-28T20:48:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047983154-MP-FIS-Venda-para-Zona-Franca-de-Manaus-com-Desconto-de-ICMS-Pis-e-Cofins-com-ST-Reduzido
---

**Dúvida**

Qual a configuração para Venda para Zona Franca de Manaus com Desconto de ICMS, Pis e Cofins com ST Reduzido ?

**Ambiente**

Todas as Versões

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

Solid. Saída (B1\_PICMRET) – Definido como 39%

 

**Tipos de Entrada e Saída (Mata080)**

Calc. ICMS (F4\_ICM) – Definido como SIM

Livro Fiscal ICMS (F4\_LFICM)  - Definido como Outros

Material de Consumo (F4\_CONSUMO) – Definido como Não

Ded.ICM.ST  (F4\_ICMSTMT) - Vazio

PIS Z.Franca (F4\_PISDSZF) e COFINS Z.F.( F4\_COFDSZF)  - Definido como 2

PIS/COFINS (F4\_PISCOF) -  Definido como AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) – Definido como CALCULA.

Mot. Desone (F4\_MOTICM) - 7 suframa

%Red.ICMS ST (F4\_BSICMST) – Definido como 58,33%

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

Aplicação do MVA: R$ 843,97 \* 39% = R$ 329,15

Base de Cálculo do ICMS ST: R$ 843,97 + R$ 329,15 = R$ 1.173,12

Base Reduzida: R$ 1.173,12 \* 58,33% = R$ 684,28

Cálculo do Imposto: R$ 684,28\* 17% = R$ 116,33

Valor do ICMS ST: R$ 116,33 – R$ 63,53 = R$ 52,80

Valor total da nota: R$ 843,97 + R$ 52,80 = R$ 896,77
