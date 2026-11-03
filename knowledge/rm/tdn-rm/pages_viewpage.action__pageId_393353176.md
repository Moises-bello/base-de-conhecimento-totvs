---
content_hash: 109e7300950f619149faaf06c204b790c6553ebc3ec96db89e84a4788df3527a
fetched_at: '2026-06-29T00:09:09.219921+00:00'
page_id: '393353176'
product: rm
source: tdn-rm
title: DT Portal TOP - Criação do Menu
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393353176
version: 2
---

# CRIAÇÃO DO MENU DO PORTAL DO TOP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Obras e Projetos. |
| **Função:** | Portal TOTVS Obras e Projetos. |
| **Situação/Requisito:** | Deverá ser criado uma opção de criação do Menu do Portal.  Este Menu precisa seguir as regras de segurança do Perfil de Usuário.  Deve ter a opção de tradução, para mercados internacionais. |
| **Solução/Implementação:** | Foi criado um serviço REST para obter os menus que serão utilizados no portal do TOP.  Serão retornados os menus que o usuário possui permissão no perfil de usuário do RM.  Os menus possuem devem utilizar Resources para garantir a tradução dos mesmos para o mercado internacional. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | [CPAPP01-234](http://jiraproducao.totvs.com.br/browse/CPAPP01-234) |
| **Requisito:** | [CPAPP01-181](http://jiraproducao.totvs.com.br/browse/CPAPP01-181) |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
