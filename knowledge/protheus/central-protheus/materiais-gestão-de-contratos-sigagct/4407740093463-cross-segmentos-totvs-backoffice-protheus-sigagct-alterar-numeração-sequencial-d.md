---
article_id: 4407740093463
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 89618bcd3a8791a7095cfbd3636444e26553b556b6b1308c1d30c633e007623c
fetched_at: '2026-06-28T22:37:20.349360+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alterar numeração sequencial
  dos títulos provisórios
type: support-article
updated_at: '2025-04-16T17:55:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407740093463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Alterar-numera%C3%A7%C3%A3o-sequencial-dos-t%C3%ADtulos-provis%C3%B3rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24988929769495) Tempo aproximado para leitura: **: 00:01:00 min** **Dúvida**

Existe possibilidade de alterar a sequência da numeração de títulos provisórios gerados na inclusão do contrato   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**

A possibilidade existente de se alterar a sequência da numeração dos titulo provisórios do SIGAGCT é reiniciando a numeração com um novo prefixo de titulo a ser utilizado para esses títulos provisórios

Para reiniciar a sequência da numeração dos títulos provisórios ao incluir um contrato com cronograma financeiro e refletir no contas à **PAGAR**, altere o parâmetro: "**MV\_CNPREF**" -  Prefixo usado pelos títulos gerados pelo módulo gestão de contrato.

Caso o parâmetro esteja em branco, inclua um prefixo, como exemplo: CTR

Para reiniciar a sequência da numeração dos títulos provisórios ao incluir um contrato e refletir no contas à **RECEBER**, altere o parâmetro: "**MV\_CNPRECL**" - Prefixo usado pelos títulos gerados pelo módulo gestão de contrato.

Caso o parâmetro esteja em branco, inclua um prefixo, como exemplo: CTR

Para incluir uma numeração específica dos títulos provisórios, a possibilidade existente é somente através de customização, com os Pontos de Entradas citados abaixo:

Contas à Pagar    : [**CNTPRSE2 - Geração de títulos**](https://tdn.totvs.com/pages/releaseview.action?pageId=6089601)

Contas à Receber: **[CNTPRSE1 - Geração de títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=6089600)**

***Saiba Mais:***

[CNTPRSE2 - Geração de títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=6089601)

[CNTPRSE1 - Geração de títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=6089600)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
