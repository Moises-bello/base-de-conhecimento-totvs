---
content_hash: 70821b16afd7868b5e80f57845b7f00a7972de60046fc5cdad1b1a8a5fcee032
fetched_at: '2026-06-29T00:08:38.373824+00:00'
page_id: '285649687'
product: rm
source: tdn-rm
title: 1039845 EDUCACIONAL01-1470 DT Importação de dados Urânia – Utiliza sala do
  ambiente Urânia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285649687
version: 102
---

# Importação de dados Urânia

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Importação de dados Urânia |
| **Situação/Requisito:** | Ao executar o processo de “Importação de dados do Urânia”, caso esteja marcado o parâmetro Educacional | Integração | Urânia | Utiliza “Ambiente” do Urânia como “Sala” do Totvs Educacional, o sistema não permitia importar registro de turma/disciplina se o arquivo importado não continha informações do ambiente (tag <AMBIENTE>). |
| **Solução/Implementação:** | Ao executar o processo de “Importação de dados do Urânia”, será permitido importar registros de turma/disciplina, quando marcado o parâmetro Educacional | Integração | Urânia | Utiliza “Ambiente” do Urânia como “Sala” do Totvs Educacional. Caso o arquivo importado não contenha dados do ambiente (tag <AMBIENTE>), será gravado um Log de Aviso e permitido prosseguir com a importação. Também foi alterado o processo “Atualização do Log das alocações das turmas/disciplinas importadas do Urânia”, onde será gerado status “Aviso” na situação citada anteriormente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
