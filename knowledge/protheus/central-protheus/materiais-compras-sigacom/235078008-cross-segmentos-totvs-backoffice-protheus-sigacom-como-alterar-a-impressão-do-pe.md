---
article_id: 235078008
category: Materiais - Compras (SIGACOM)
content_hash: 1f94de0ee518a0ee229d3182676e0e3eebc70799dc95ad1c5279724fd84c8c51
fetched_at: '2026-06-28T22:41:14.436676+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como alterar a impressão
  do pedido de compra por um relatório customizado na rotina MATA121 ?
type: support-article
updated_at: '2025-08-04T18:18:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235078008-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-alterar-a-impress%C3%A3o-do-pedido-de-compra-por-um-relat%C3%B3rio-customizado-na-rotina-MATA121
---

**Dúvida**

Como alterar a impressão do pedido de compra por um relatório customizado na rotina MATA121 ?  
  
**Ambiente**

Protheus – Compras – A partir da 12.1.17

**Solução**

Na rotina pedido de compras (**MATA121**) a opção de impressão do pedido de compra disponível através do botão **Outras Ações**->**Imprimir**, por padrão o relatório impresso é o **MATR110**.

Muitos clientes questionam se é possível alterar o relatório impresso ou incluir um relatório customizado ao invés do relatório **MATR110**.

Para utilizar um novo relatório na rotina **MATA121** é possível alterando o nome do relatório através do parâmetro **MV\_PCOMPRA**.

Exemplo de configuração:

Acesse o configurador e siga os seguintes passos:

* Ambiente -> Cadastro -> Parâmetros -> Pesquisar -> MV\_PCOMPRAS

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415213087639)

**IMPORTANTE** :

* Não deve ser informado "U\_" ou  "( )" no conteúdo do parâmetro para que funcione.
* O botão "**Outras Ações->Imprimir Browse"**, é um botão da interface do **Protheus** e não pode ser alterado, pois é existente em quase todas as rotinas e tem a função de realizar a impressão das informações do Browse da rotina em questão.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Fontes de Relatórios de Compras para personalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022534771)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
