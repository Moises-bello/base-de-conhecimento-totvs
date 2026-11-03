---
article_id: 1500008921942
category: Escrita Fiscal - Impostos - ICMS
content_hash: 9beb384be2129251045dcbd037db50944f963ed3875494b146be55cc65a20673
fetched_at: '2026-06-28T22:39:23.988745+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como emitir nota
  fiscal de devolução de suframa?'
type: support-article
updated_at: '2023-11-17T18:07:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008921942--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-emitir-nota-fiscal-de-devolu%C3%A7%C3%A3o-de-suframa
---

**Dúvida**Como emitir nota fiscal de devolução de suframa?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A nota fiscal de devolução deve ser o espelho da nota fiscal original.

Venda de SP para Zona Franca de Manaus:

**11º Exemplo –** Venda para Zona Franca de Manaus com Desconto de ICMS, Pis e Cofins (Pis e cofins descontado após o calculo do ICMS).

**Configurações:**

**Parâmetros**  
MV\_RPCBIUF  Preenchido  
MV\_DESCZF definido como .T.  
MV\_DESZFPC definido como .T.  
MV\_DSZFSOL definido como .T.  
MV\_UFSTZF  Preenchido  
MV\_IPIZFM definido como .T.  
MV\_SUFRAMA definido como T  
***MV\_RPCBIZF definido como F***(o desconto de ICMS será aplicado *antes* de aplicar o Desconto de PIS e Cofins)

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

PIS/COFINS (F4\_PISCOF) -  Definido como AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) – Definido como CALCULA.

Mot. Desone (F4\_MOTICM) - 7 suframa

Valor de Mercadorias: R$ 1.000,00

Alíquota de ICMS: 7%

Alíquota de PIS: 1,65%

Alíquota de Cofins: 7,6%

Base de Cálculo do Pis/Cofins: R$ 1.000,00

Valor do Pis: R$ 1.000,00 \* 1,65% = R$ 16,50

Valor do Cofins: R$ 1.000,00 \*7,6% = R$ 76,00

Base de Cálculo de ICMS: R$ 1.000,00 \* 7% = R$ 70,00

Valor de ICMS a descontar: R$ 70,00

Valor da Operação: R$ 1000,00 – R$ 70,00 - R$ 16,50 - R$ 76,00 = R$ 837,50

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013415322)

Configuração da TES de devolução

Calcula icms = sim

L fiscal icms = isento

CST = 40

Mot desone = 7

PIS/COFINS (F4\_PISCOF) -  Definido como AMBOS

CRÉD PIS/COFINS (F4\_PISCRED) – Definido como CALCULA.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013415942)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013714661)

CD2

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013416142)

Documentação  Suframa:

<https://tdn.totvs.com/pages/releaseview.action?pageId=605019302>
