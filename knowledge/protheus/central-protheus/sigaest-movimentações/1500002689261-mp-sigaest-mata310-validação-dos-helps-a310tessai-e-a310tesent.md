---
article_id: 1500002689261
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 60df4d7ef7c517ee30603cb8e85e0e1c7ad761c888c47f1c00db3b246d1fd26b
fetched_at: '2026-06-28T22:38:58.625210+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - MATA310 - Validação dos HELPs A310TESSAI e A310TESENT
type: support-article
updated_at: '2021-04-28T15:45:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002689261-MP-SIGAEST-MATA310-Valida%C3%A7%C3%A3o-dos-HELPs-A310TESSAI-e-A310TESENT
---

**Ocorrência**

Ao tentar efetuar Transferência entre Filiais (MATA310 ou MATA310), é apresentado o HELP: A310TESSAI ou A310TESENT

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101536354/mceclip0.png)  
  
**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17

**Causa**  
Os HELP's **A310TESSAI** e **A310TESENT** são apresentados em casos onde a tabela SFM (TES inteligente) esteja em branco.

**Solução**

Se os campos de TES - "**Tes para notas de saída**" e "**Tes para notas de entrada**" estiverem preenchidos, deixe os campos "Tp Oper. Saída?" e "Tp Oper. Entrada?" em branco, conforme imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002693161/mceclip1.png)

Do contrário também funcionará (deixando os campos de TES em branco e os campos de Tp Oper preenchidos).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
