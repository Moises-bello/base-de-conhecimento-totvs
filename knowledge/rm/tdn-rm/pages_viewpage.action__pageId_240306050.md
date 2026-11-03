---
content_hash: b90ffa531d7bb69e7134a1a61b4b909523be4b4b34dcc0160d9ccd8c15c6f71a
fetched_at: '2026-06-29T00:08:10.571572+00:00'
page_id: '240306050'
product: rm
source: tdn-rm
title: TVBL85_DT_Data_Competência_Lançamento_Alterada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240306050
version: 113
---

# INCLUSÃO/EXCLUSÃO DE BOLSA RETROATIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Inclusão/Exclusão de bolsa retroativa* |
| **Situação/Requisito:** | Ao inserir bolsa retroativa para um lançamento com status Baixado, o sistema estava alterando a data de contabilização de inclusão e o campo “Mês/Ano de competência” do lançamento. Somente ocorria se estivesse configurado para utilizar data de contabilização igual à “Data da competência”. |
| **Solução/Implementação:** | Criado o parâmetro Educacional | Integração | Financeiro | “Não alterar a data de competência do lançamento, no processo de inclusão/exclusão de bolsa retroativa.  Caso a data de contabilização de inclusão esteja configurada para utilizar “Data da competência”, este parâmetro “desmarcado” significa que será alterada a data de contabilização de inclusão ao inserir bolsa retroativa para um lançamento baixado. |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | TUKUMM |
| **Requisito (ISSUE):** | *N/A.* |

divs
