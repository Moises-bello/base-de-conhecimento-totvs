---
article_id: 21800321917079
category: SIGAACD - Automação e Coleta de Dados
content_hash: 706ae42e5c0af22cdf06e887a2d79ab78fdb1fd68b1e1fa7ed88924efdb61107
fetched_at: '2026-06-28T22:39:11.180446+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA030 Gera Mestre
  mesmo para Produto ou Endereço Bloqueado _MSBLQL =Sim '
type: support-article
updated_at: '2024-03-05T19:45:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21800321917079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA030-Gera-Mestre-mesmo-para-Produto-ou-Endere%C3%A7o-Bloqueado-MSBLQL-Sim
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21800347989527) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**

Ao incluir Mestre de Inventário por Produto ou Endereço que estejam Bloqueados, permite que seja incluido o mesmo e apresenta posteriormente o ***HELP REGBLOQ***?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21800652916375)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21800652928663)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21800652940183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21800652957591)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

No exemplo de cenário acima, é necessário avaliar os itens que estão bloqueados se há necessidade de efetuar o processo de Inventário, se positivo deve ser alterado o campo de Bloqueado para N.

Também é possível na rotina de Lançamentos do Inventário (ACDA035) excluir as linhas dos itens que estão Bloqueados para que não sejam processados ou mesmo apresente o HELP REGBLOQ. Veja o print de exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21800993102871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21800993120791)

***Fonte:***

<https://tdn.totvs.com/pages/releaseview.action?pageId=306858373>

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
