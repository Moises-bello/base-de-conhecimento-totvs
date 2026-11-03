---
article_id: 360050442913
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c5a7fe5417082aa7f54d17ecf7dcfeaa383f98492d8df5ce8295ea35ecca4926
fetched_at: '2026-06-28T22:42:02.603178+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Venda para
  Zona Franca de Manaus com Desconto de ICMS, Pis e Cofins com ST Reduzido, utilizando
  a redução do ST no ICMS a deduzir do ST
type: support-article
updated_at: '2025-02-11T22:06:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050442913-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Venda-para-Zona-Franca-de-Manaus-com-Desconto-de-ICMS-Pis-e-Cofins-com-ST-Reduzido-utilizando-a-redu%C3%A7%C3%A3o-do-ST-no-ICMS-a-deduzir-do-ST
---

**Dúvida**Como fazer uma venda para Zona Franca de Manaus com Desconto de ICMS, Pis e Cofins com ST Reduzido, utilizando a redução do ST no ICMS a deduzir do ST  
   
 **Ambiente**Todas Versões Protheus  
  
**Solução**

**Parâmetros:**

MV\_UFSTZF **=** Preencher com a UF de Destino

MV\_DSZFSOL = .T.

MV\_RPCBIUF = Preencher com a UF de destino

MV\_RPCBIZF = .T.

**Clientes(Mata030)**

Tipo (A1\_TIPO) -  Definido com Solidário

Desc. P/ Suframa (A1\_CALCSUF) – Definido como SIM

Suframa (A1\_SUFRAMA) - Preenchido

Cód. Mun. ZF (A1\_CODMUN) - Preenchido

**Produtos (Mata010)**

Imp. Z. Franca (B1\_IMPZFRC) – Em branco

Solid. Saida (B1\_PICMRET) – Definido como 39%

**Tipos de Entrada e Saída (Mata080)**

Calc. ICMS (F4\_ICM) – Definido como SIM

Livro Fiscal ICMS (F4\_LFICM)  - Definido como Outros

Material de Consumo (F4\_CONSUMO) – Definido como Não

Ded.ICM.ST  (F4\_ICMSTMT) - Vazio

PIS Z.Franca (F4\_PISDSZF) e COFINS Z.F.( F4\_COFDSZF)  - Definido como 2

PIS/COFINS (F4\_PISCOF) -  Definido como AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) – Definido como CALCULA.

%Red.ICMS ST (F4\_BSICMST) – Definido como 58,33%

Red.Carg.Trb (F4\_APLIRED) – Definido como 3

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

Aplicação do MVA: R$ 843,97 \* 39% = R$ 329,15

Base de Cálculo do ICMS ST: R$ 843,97 + R$ 329,15 = R$ 1.173,12

Base Reduzida: R$ 1.173,12 \* 58,33% = R$ 684,28

Cálculo do Imposto: R$ 684,28\* 17% = R$ 116,33

Valor do ICMS a deduzir: R$ 63,53 - R$ 63,53 \* (100-58,33)/100 = R$ 37,06

Valor do ICMS ST: R$ 116,33 – R$ 37,06 = R$ 79,27

Valor total da nota: R$ 843,97 + R$ 79,27 = R$ 923,24
