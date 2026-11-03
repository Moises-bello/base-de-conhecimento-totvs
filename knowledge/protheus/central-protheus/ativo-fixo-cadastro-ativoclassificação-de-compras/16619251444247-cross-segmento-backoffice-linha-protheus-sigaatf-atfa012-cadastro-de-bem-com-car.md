---
article_id: 16619251444247
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: c1b0d4b495c4c69aec9415a82051663dddf94f707d16ef9b8f14d2fa17650bdc
fetched_at: '2026-06-28T22:41:48.332250+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - Cadastro de
  Bem com Caractere Especial na Descrição
type: support-article
updated_at: '2023-08-25T17:15:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16619251444247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Cadastro-de-Bem-com-Caractere-Especial-na-Descri%C3%A7%C3%A3o
---

**Problema:**

Ao tentar informar uma descrição para bem o com caractere especial é apresentado o help:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16619088046615)

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - A partir da versão 12

**Solução:**

No cadastro de ativo, foi desenvolvido uma melhoria para que não permita o cadastro de nenhum campo obrigatório utilizado como índice com caractere especial, gerando uma mensagem de alerta informando o usuário.

Pois ao cadastrar um ativo em que um ou mais campos índice é preenchido com algum caractere especial, é gerado error log ao tentar fazer consulta em banco de dados.

O caractere especial danifica a sintaxe de consulta no banco de dados, por esse motivo não é recomendado cadastro com caracteres especiais.

Por este motivo foi removia a opção de informar caracteres especiais no campo N1\_DESCRIC.

**Saiba mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=648034479>
