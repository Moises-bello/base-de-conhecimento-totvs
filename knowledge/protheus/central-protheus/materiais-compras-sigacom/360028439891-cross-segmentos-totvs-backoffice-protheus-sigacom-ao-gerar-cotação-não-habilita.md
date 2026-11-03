---
article_id: 360028439891
category: Materiais - Compras (SIGACOM)
content_hash: 52fa09fd700707ef26d5852236292f244c6295210306ec7a7f8e3eda00738499
fetched_at: '2026-06-28T22:41:07.435992+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao Gerar Cotação não
  habilita a inclusão de um Fornecedor (Inclusão Manual) '
type: support-article
updated_at: '2022-07-06T14:31:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028439891-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-Gerar-Cota%C3%A7%C3%A3o-n%C3%A3o-habilita-a-inclus%C3%A3o-de-um-Fornecedor-Inclus%C3%A3o-Manual
---

**Dúvida**Ao Gerar Cotação não fica habilitado a inclusão de um Fornecedor (Inclusão Manual)

**Ambiente**Protheus – Compras – A partir da versão 12.1.17

**Solução**

Ao gerar cotação não é possível inserir Fornecedor (Inclusão Manual), não habilita a Lupa e nem permite digitar manualmente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028512591/mceclip0.png)

Para alteração, seguir os procedimentos;

1. Configurador> Em Base de Dados -> Dicionário -> Base de Dados:

2. Acessar tabela SC8 ->  Editar o campo C8\_FORNECE  e -> Em Propriedade alterar o conteúdo = "2" Alterar;

 3. Acessar o campo C8\_LOJA > Editar o campo C8\_FORNECE  e -> Em Propriedade alterar o conteúdo = "2" Alterar;

![20211229_105923.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4417442090519/20211229_105923.gif)

Após alteração, salvar a configuração do Configurador ao fechar a rotina MATA131 e abrir novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028514872/mceclip4.png)

***Saiba Mais :***

* [Cotação](https://tdn.totvs.com/x/0iObEg)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Limitar número de Fornecedores na cotação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036577853)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
