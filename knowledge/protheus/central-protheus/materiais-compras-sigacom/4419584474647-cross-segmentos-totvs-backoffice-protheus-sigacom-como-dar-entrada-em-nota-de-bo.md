---
article_id: 4419584474647
category: Materiais - Compras (SIGACOM)
content_hash: 08ae059bc17ed8a0daebe9b2540983e7c6061a799451823417276d314eb343f0
fetched_at: '2026-06-28T22:41:14.555424+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como dar Entrada em
  Nota de Bonificação que atualiza somente quantidade sem atualizar custo ?
type: support-article
updated_at: '2022-05-16T22:53:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419584474647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-dar-Entrada-em-Nota-de-Bonifica%C3%A7%C3%A3o-que-atualiza-somente-quantidade-sem-atualizar-custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como dar Entrada em uma Nota de Bonificação que atualiza somente quantidade sem atualizar custo ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**

Foi desenvolvida a funcionalidade de registro de notas fiscais de compra em caráter de bonificação, ou seja, a entrada do material **não afetará o seu custo em estoque.**

Com essa nova funcionalidade será possível registrar em uma mesma nota de entrada os itens referentes à bonificação recebida do fornecedor juntamente com itens normais de compra.

Desse modo o estoque do material será atualizado e todas as demais integrações (fiscal, contábil, etc.) serão realizadas normalmente de acordo com o TES, porém o custo do material não será afetado quando for utilizado o conceito de “bonificação”.

Para que o item não tenha o custo de entrada calculado será necessário configurar o novo campo “F4\_BONIF” no cadastro de TES. Ao realizar uma entrada utilizando o TES configurado para “bonificação”, o **sistema não atualizará o custo do item na tabela SD1** (Itens de notas fiscais de entrada), permanecendo zerado.

Segue exemplo:

1° Configuração de TES:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419588816151/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419584426135/mceclip1.png)

2° Fazer um Documento de Entrada utilizando a TES correspondente:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419584430871/mceclip2.png)

***Obs.1:***

Caso o campo F4\_BONIF estiver com conteúdo "Não", será custeado o custo do produto da nota fiscal:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419584439319/mceclip3.png)

***Obs.2:***

Dúvidas referente a Custos da NF, podem ser verificadas junto ao suporte ao módulo de Estoque/Custos.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
