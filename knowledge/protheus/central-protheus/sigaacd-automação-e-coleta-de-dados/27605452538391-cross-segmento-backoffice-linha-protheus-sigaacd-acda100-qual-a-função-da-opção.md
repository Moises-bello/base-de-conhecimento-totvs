---
article_id: 27605452538391
category: SIGAACD - Automação e Coleta de Dados
content_hash: 6b9908631116fd41978a008d2c0eb7b053f870e6a96d28d7b38a06bdc386c7b9
fetched_at: '2026-06-28T22:39:11.100918+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  ACDA100 - Qual a
  função da opção "Gera Nota" na OS por Pedido de Venda?
type: support-article
updated_at: '2024-11-06T18:14:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27605452538391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-Qual-a-fun%C3%A7%C3%A3o-da-op%C3%A7%C3%A3o-Gera-Nota-na-OS-por-Pedido-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27605432149271) Tempo aproximado para leitura: **00:03:12 min**

**Dúvida**Para que serve a Ordem de Separação por Pedido de venda com a opção 'Gera Nota" = Sim?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

No F12 da rotina rotina Ordens de Separação, quando selecionada a opção Pedido de Venda, há uma opção chamada "Gera Nota".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27605452513559)

Ela serve justamente para o usuário gerar a Ordem de Separação de forma que ela só será considerada finalizada (legenda verde), quando houver a Geração da Nota de Saída pelo próprio coletor (rotina ACDV168).

Exemplo prático:

Ordem de Separação 000053, o produto já foi separado no coletor (ACDV166) mas ela fica com legenda amarela (em andamento):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27605452514455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27605452515991)

Para efetuar a geração da Nota via Coletor, acesse ao menu:

Atualizações -> Expedição -> Geração de Nota de Saída.

![acessando ao acdv168.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/27605432154775)

Posteriormente, basta selecionar o numero da Ordem de Separação e gerar a Nota:

![gerando a nota.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/27605452519959)

Com isso, a Ordem de Separação é finalizada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27605452520983)

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA100 - Ordem de Separação por Pedido de Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408423317399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-Ordem-de-Separa%C3%A7%C3%A3o-por-Pedido-de-Venda)*

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
