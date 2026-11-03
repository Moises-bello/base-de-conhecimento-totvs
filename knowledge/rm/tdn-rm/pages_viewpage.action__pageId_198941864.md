---
content_hash: 768d753eb68e3541840b186c78f60b442690a78739a5b891aad39724e4fc46e9
fetched_at: '2026-06-29T00:06:01.933671+00:00'
page_id: '198941864'
product: rm
source: tdn-rm
title: Tolerância_no_Faturamento_BRA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198941864
version: 3
---

# Tolerância no Faturamento

O processo de Tolerância no Faturamento consiste os limites superior e inferior informados no Cadastro de Produto, impedindo que ao realizar um faturamento de movimento que utilize tolerância os mesmos não sejam realizados.

**Principais Campos e Parâmetros:**

**No Cadastro do Produto:**

Acessar o TOTVS Gestão de Estoque, Compras e Faturamento | Guia Cadastros | Produto | Editar (ou incluir novo) um produto | Guia: Preço | Preencher “Tolerância Preço” e/ou “Tolerância Quantidade”(o valor informado será considerado como %).

**Movimento de Origem:**

Acessar o TOTVS Gestão de Estoque, Compras e Faturamento| Ambiente | Parametros | Selecionar o tipo de movimento a ser parametrizado | Etapa [Mov – Outros Dados] Aprovação: Usa

**Movimento de Destino:**

1. Acessar o TOTVS Gestão de Estoque, Compras e Faturamento| Ambiente | Parâmetros | Selecionar o tipo de movimento a ser parametrizado | [Mov – Outros Dados] Tolerância: Usar Para Quantidade
2. Acessar o TOTVS Gestão de Estoque, Compras e Faturamento| Ambiente | Parâmetros | Selecionar o tipo de movimento a ser parametrizado | [Mov – Outros Dados] Tolerância: Usar Para Preço
3. Acessar o TOTVS Gestão de Estoque, Compras e Faturamento| Ambiente | Parâmetros | Selecionar o tipo de movimento a ser parametrizado | [Mov – Outros Dados] Tolerância: Usar Para Quantidade e Preço
