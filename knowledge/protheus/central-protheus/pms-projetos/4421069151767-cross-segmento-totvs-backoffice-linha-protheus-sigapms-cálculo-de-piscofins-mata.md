---
article_id: 4421069151767
category: PMS - Projetos
content_hash: d71b45b43662218737deacf6920cc6cca6d669866bd8f368d846c1fb7d0212fc
fetched_at: '2026-06-28T22:37:15.071111+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Cálculo de PIS/Cofins
  (MATA010 - SIGAPMS)
type: support-article
updated_at: '2022-02-01T20:49:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421069151767-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-C%C3%A1lculo-de-PIS-Cofins-MATA010-SIGAPMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como calcular o **PIS/Cofins** para produtos do Projeto?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Todas as Versões

**Solução**

O Sistema avalia as definições das alíquotas para o cálculo do PIS/COFINS, mediante a seguinte prioridade de preenchimento:

**Para Apuração do PIS/COFINS:**

1. Cadastro de Produtos - percentuais definidos nos campos **Percentual COFINS** e **Percentual PIS**;
2. Parâmetros - percentuais definidos pelos parâmetros **MV\_TXPIS** e **MV\_TXCOFIN**.

**Cadastro de Produto**

Informe os percentuais de COFINS, PIS ou CSLL, de acordo com a operação a ser realizada na nota fiscal, e se o produto calcula ou não, os impostos para retenção.

Campos: B1\_PCOFINS, B1\_PPIS, B1\_PCSLL, B1\_PIS, B1\_COFINS e B1\_CSLL  (respectivamente, Percentual COFINS, Percentual PIS, Percentual CSLL, Calcula PIS, Calcula COFINS e Calcula CSLL).

**Cadastro de TES**

Para efeito de crédito/débito do PIS/COFINS, os campos **Calcula PIS/COFINS e Credita PIS/COFINS** devem estar configurados.

É importante ressaltar que para o cálculo correto do custo de entrada, no campo Cred. PIS/COF, informe se o imposto deve ser creditado ou debitado, e no campo Atu. Estoque deve estar configurado com Sim.

**Cadastro de Naturezas**

Informe a retenção/cálculo dos tributos (PIS, COFINS e CSLL) no módulo Financeiro.

Campos: ED\_CALCCOF, ED\_CALCPIS, ED\_CALCCSL, ED\_PERCCOF, ED\_PERCPIS e ED\_PERCCSL (respectivamente, Calcula COFINS, Calcula PIS, Calcula CSLL, Percentual COFINS, Percentual PIS e Percentual CSLL).

**Saiba mais em : [Cálculo de PIS/Cofins (MATA010 - SIGAPMS)](https://tdn.totvs.com/x/IZOZH)**
