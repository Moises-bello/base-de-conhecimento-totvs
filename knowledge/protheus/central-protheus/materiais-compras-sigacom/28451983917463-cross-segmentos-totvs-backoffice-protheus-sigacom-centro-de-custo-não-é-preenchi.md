---
article_id: 28451983917463
category: Materiais - Compras (SIGACOM)
content_hash: bb3cb4607e6eccf442c51906d6e6f3bff6398df03ac4b4cca7faf1d2fd3b8858
fetched_at: '2026-06-28T22:41:14.405210+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Centro de Custo não
  é preenchido no financeiro ao incluir Nota Fiscal
type: support-article
updated_at: '2024-12-11T18:06:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28451983917463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Centro-de-Custo-n%C3%A3o-%C3%A9-preenchido-no-financeiro-ao-incluir-Nota-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28451983894807) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como levar o centro de custo para os titulos no financeiro quando origem for Documento de Entrada?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

Na digitação do documento de entrada, é possível informar o centro de custo e uma conta contábil diferente para cada linha da tabela SD1 (itens da NF). Por exemplo, em uma nota fiscal com 100 linhas, podem ser registrados 100 centros de custo e 100 contas contábeis distintos.

O documento de entrada grava informações de entidades contábeis na tabela SEZ (Distribuição de Naturezas em CC) apenas quando é utilizado o rateio por centro de custo e a geração de rateio financeiro está habilitada (parâmetro MV\_MULNATS). Nesse caso, é necessário preencher a natureza na aba de Duplicatas.

Como alternativa, pode-se utilizar o ponto de entrada MT100GE2, que permite complementar a gravação dos títulos no contas a pagar.

Os campos no módulo Financeiro para digitação do Centro de Custo e Conta Contábil são destinados à inserção manual, quando um título é incluído diretamente pelo módulo Financeiro. Não há integração com o módulo Compras para preencher esses campos com valores padrão, como acontece com a "Natureza"."

**Pontos de Entrada :**

[**MT100GE2 - Complementa a Gravação dos Títulos Financeiros a Pagar**](https://tdn.totvs.com/pages/releaseview.action?pageId=6085781)  
[**MTA103OK - Altera o resultado da validação padrão para inclusão e alteração**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087790)  
[**MT103LOK - Validação do rateio para os itens do documento de entrada por centro de custo**](https://tdn.totvs.com/display/public/PROT/MT103LOK)

***Saiba Mais :***

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747-MP-SIGACOM-Pontos-de-Entrada-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
