---
content_hash: c429fa8236c73ac9df712f7b26146fc8ba1aa7423e8f94a339035533b7420022
fetched_at: '2026-06-29T00:08:58.755265+00:00'
page_id: '361437166'
product: rm
source: tdn-rm
title: 2286457 FOPCALCULO01-3480 DT Cadastro de Cliente e Fornecedor
type: documentation
url: https://tdn.totvs.com/display/LRM/2286457+FOPCALCULO01-3480+DT+Cadastro+de+Cliente+e+Fornecedor
version: 7
---

# Cliente/Fornecedor

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cadastro | Cliente e Fornecedor |
| **Situação/Requisito:** | Ao realizar a inclusão de um Cliente/Fornecedor o sistema exibe a mensagem 'não foi possível executar o processo corretamente: Campo(s) obrigatório(s) não preenchido(s): Tipo de Cliente/Fornecedor". |
| **Solução/Implementação:** | Ajustado o cadastro de Clientes e Fornecedores para validar o tipo de cliente/fornecedor verificando o parâmetro 'Tipo de Cliente/Fornecedor Obrigatório' no módulo TOTVS Gestão Financeira.   1. Com o parâmetro marcado, o campo no cadastro de Clientes e Fornecedores passa ser obrigatório, retornando uma mensagem para o usuário quando o mesmo tenta salvar o cadastro sem preencher o campo: 2. Com o parâmetro desmarcado, o campo passa não ser obrigatório, permitindo que o usuário cadastre/altere um Cliente/Fornecedor sem informar o tipo de Cliente/Fornecedor. Não é retornado mensagem de erro para o usuário: |
| **Tickets relacionados:** | [2286457](https://totvssuporte.zendesk.com/agent/tickets/2286457 "Open ticket in Zendesk Support") |
