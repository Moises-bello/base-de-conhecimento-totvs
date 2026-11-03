---
article_id: 1500002097622
category: SIGAEST - SALDOS
content_hash: 4c6f97af74f58599e903337709dca2a382c2b27cc6b296457fa3af3402e3d56b
fetched_at: '2026-06-28T22:39:14.966356+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: MP - SIGAEST - MATC050 - Não estão trazendo os dados
type: support-article
updated_at: '2021-04-28T15:09:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002097622-MP-SIGAEST-MATC050-N%C3%A3o-est%C3%A3o-trazendo-os-dados
---

**Dúvida**Ao gerar a Consulta Geral ao Produto (MATC050) não aparecem os dados. Como ajustar este problema?  
  
**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17

**Solução**Em muito dos casos este problema é resolvido pelo botão "Outras Opções". Vejamos um exemplo à seguir.

Temos nosso produto 712 chamado "Ordem de Produção", vamos fazer uma Consulta Geral dele:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001909082/mceclip0.png)

Por padrão, a consulta já abre flegando a seção "Dados Cadastrais", com várias informações do Cadastro de Produto - SB1:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102967413/mceclip1.png)

Neste exemplo, o produto 712 possui Ordem de Produção em aberto, porém vejamos que mesmo ao clicar nesta seção ele não está aparecendo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100803974/mceclip2.png)

Então, clicaremos em "Outras Ações" -> "Expande":

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100804034/mceclip3.png)

Com isso, trouxeram as informações normalmente:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102967513/mceclip4.png)

**Fiz o processo acima e mesmo assim persiste sem aparecer Dados de uma/algumas seções. Como resolver?**

É importante avaliar se de fato existem informações para a seção em que gostaria de visualizar dados. No exemplo citado acima, se nosso produto tivesse OP somente com status "Fechada" não apareceria.

Outro cenário bastante comum em que não trazem dados é quando existem gatilhos (triggers) ou funções de usuários em campos da tabela SB1. Ou mesmo P.E/Customizações envolvendo SB1/Cadastro de Produtos. É importante fazer essa avaliação previamente para checar se realmente estaria ocorrendo uma não conformidade no Protheus.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033462-SIGAEST-SALDOS)*
