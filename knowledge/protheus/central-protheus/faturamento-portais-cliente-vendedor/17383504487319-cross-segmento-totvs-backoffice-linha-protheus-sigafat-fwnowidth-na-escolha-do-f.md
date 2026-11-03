---
article_id: 17383504487319
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 3684ce6158c4c219e22cee9fbf941d095cf25845b4d1cedf36932be4a622a1e8
fetched_at: '2026-06-28T22:38:23.882141+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -FWNOWIDTH na
  escolha do Fornecedor do usuário do portal
type: support-article
updated_at: '2023-09-08T19:24:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17383504487319-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-FWNOWIDTH-na-escolha-do-Fornecedor-do-usu%C3%A1rio-do-portal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17383520373911) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Ao incluir um fornecedor no cadastro de usuário de portal (fata220), gera o help: FWNOWIDTH

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17383112632727)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

A mensagem ocorre por que o tamanho do campo **A2\_NOME** é maior do que o campo **AI5\_NOMFOR do cadastro do portal, aba fornecedor**, com isso ao tentar incluir, o sistema verá que o tamanho de campo é maior e não conseguirá incluir.

Por padrão do sistema, o campo A2\_NOME vem com tamanho 40 e o campo AI5\_NOMFOR vem com tamanho 30.

![A2_Nome.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/17383517791639)

![AI5_NOMFOR.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/17383487831447)

Para que o help não ocorra, ajuste o tamanho do campo AI5\_NOMFOR para o mesmo tamanho do campo A2\_nome, com isso, o help não ocorrerá e permitirá a inclusão da informação no cadastro de usuário do portal:

![AI5_NOMFOR_alterado.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/17383504459287)

![portal aba fornecedor - inclusão de fornecedor.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/17383517799959)

![inclusão do fornecedor com sucesso.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/17383487835799)
