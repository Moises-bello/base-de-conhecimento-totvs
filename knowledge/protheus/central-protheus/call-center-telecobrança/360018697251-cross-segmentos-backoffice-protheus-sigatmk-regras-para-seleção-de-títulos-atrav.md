---
article_id: 360018697251
category: Call Center - Telecobrança
content_hash: 29a435e44c94b38b101d34c677ed3de513d05a5d9e4b89478f9fbc1912771c2c
fetched_at: '2026-06-28T22:41:28.612819+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Regras para seleção de títulos
  através da rotina de Pré Atendimento
type: support-article
updated_at: '2024-04-25T14:16:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018697251-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Regras-para-sele%C3%A7%C3%A3o-de-t%C3%ADtulos-atrav%C3%A9s-da-rotina-de-Pr%C3%A9-Atendimento
---

**Dúvida**

Qual a regra para o sistema retornar os títulos vencidos na rotina de **Pré Atendimento** (**TMKA280**)?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

A rotina utiliza as **Regras de Seleção (TMKA160)** para filtrar os títulos que serão apresentados ao operador. Caso existam títulos vencidos que atendam regras diferentes, o sistema apresentará todos os títulos somente ao operador que possui a maior regra cadastrada.

1. Primeiramente, é necessário cadastrar as **Regras de Seleção** (**TMKA160**);

2. Com a regra criada, precisamos definir os **Grupos de Atendimento** (**TMKA040**) que utilizem essas regras;

3. Com as regras cadastradas, precisamos vinculá-las aos operadores.

Exemplo 1 - Apenas um título existente e vencido há 3 dias.

* O título será apresentado na rotina de Pré Atendimento **somente** se acessada com o usuário 000001 - .Usuário Regra 01.

Para mais exemplos e visualização de telas de cadastros, acesse a FAQ: **[Regras para seleção de títulos através da rotina de Pré Atendimento (TMKA280)](http://tdn.totvs.com/pages/viewpage.action?pageId=375226523)**
