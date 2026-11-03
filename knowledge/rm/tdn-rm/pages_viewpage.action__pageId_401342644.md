---
content_hash: c4f715ec440bad692e710ae4ba126566744cbb39fc36c388f514bf2604f3c42f
fetched_at: '2026-06-29T00:09:10.582645+00:00'
page_id: '401342644'
product: rm
source: tdn-rm
title: 3422428 FOPCALCULO01-4484 Relatório de Escala Mensal de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=401342644
version: 1
---

# Relatório

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Relatório | Escala de Férias |
| **Situação/Requisito:** | Ao gerar o relatório 3.014 – Escala Mensal de Férias (GENERICO) na visão Delphi o campo “Limite de Concessão” está retornando uma data diferente do campo “ Limite de início de gozo” que se encontra no cadastro do período de gozo do funcionário. Atualmente na MDI .Net, o relatório Escala Mensal de Férias "não foi convertido", portanto existe somente no Delphi. No .NET existe apenas o relatório FOPREL00031 - Escala Anual de Férias, mas é diferente do Delphi e não atende o Cliente. |
| **Solução/Implementação:** | Criado o relatório FOPREL00184 - Escala Mensal de Férias.TotvsReport em .net |
| **Tickets relacionados:** | 3422428 |
