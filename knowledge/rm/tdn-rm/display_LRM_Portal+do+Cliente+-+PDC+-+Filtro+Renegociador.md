---
content_hash: c4cadc79ff80b96b975af5629ebf4e661cec6772100dd17fa4c2c7abd2d4c69a
fetched_at: '2026-06-29T00:10:30.065308+00:00'
page_id: '519180665'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Filtro Renegociador
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Filtro+Renegociador
version: 1
---

É possível realizar um filtro na tabela **XVENDAPARCELA** que será aplicado a visão de **Renegociação** no **Portal do Cliente**.Este filtro tem o mesmo comportamento de um filtro por usuário ou por perfil, mas será aplicado apenas na visão de **Renegociação**.

Importante:

* O filtro será aplicado para todos os usuários.

Para realizar a parametrização é necessário acessar os parâmetros do sistema, através da aba Ambiente em seguida é necessário ir ao menu Parâmetros>>Totvs Incorporação>>Portal do Cliente>>Relatórios. Nesta etapa de parâmetros será apresentado a opção '**Utilizar SQL para filtrar parcelas da tabela XVENDAPARCELA a serem exibidas no Renegociador**'.

**Exemplo:**Antes de parametrizar o filtro ao acessar a visão Renegociação, estava sendo apresentado 10 lançamentos pertinentes a venda ID 41.

Foi acessado os parâmetros do sistema, através da aba Ambiente em seguida é necessário ir ao menu Parâmetros>>Totvs Incorporação>>Portal do Cliente>>Relatórios. Na criação do filtro foi informado que apenas a parcela 2 deve ser visualizada.

Apos aplicar o filtro e acessar novamente a visão de Renegociação foi apresentado apenas 1 registro, respeitando o filtro imposto.
