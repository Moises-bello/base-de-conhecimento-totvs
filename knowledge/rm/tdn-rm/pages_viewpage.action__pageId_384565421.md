---
content_hash: 7bdb4a9d74d5a34bc8a5d410d2b0db727f3867b27bfe0a34681094557d04239b
fetched_at: '2026-06-29T00:09:07.116206+00:00'
page_id: '384565421'
product: rm
source: tdn-rm
title: 3123203 FOPROTINAS01-5159 DT Duplicação do Histórico de Situação após Liberação
  de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384565421
version: 3
---

# DUPLICAÇÃO DO HISTÓRICO DE SITUAÇÃO APÓS LIBERAÇÃO DE COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Funcionário | Histórico de Situação | Liberação de Competência |
| **Situação/Requisito:** | Ao executarmos a rotina de Liberação de Competência, após finalização, o produto está “duplicando” os registros do Histórico de Situação, para aqueles funcionários que tiveram Atestado/Afastamento durante o mês. |
| **Solução/Implementação:** | Ao atualizar a situação do funcionário para início e término de afastamento implementou-se a junto base de dados a verificação se existe registro de histórico para aquele período, chapa, tipo de situação antes de inserir. Assim evita-se que dados duplicados sejam salvos. |
| **Tickets relacionados:** | 3123203 |
