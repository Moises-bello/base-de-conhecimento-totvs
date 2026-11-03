---
content_hash: f1577377cd5b94ebd1f5e19b667d7c5a8ed54cfa5055c9d171de3d9ba751ed5a
fetched_at: '2026-06-29T00:06:25.138568+00:00'
page_id: '224132745'
product: rm
source: tdn-rm
title: TTRHOS_DT_REpasse_Bolsa_Opcionais_Por_Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224132745
version: 124
---

# GERAR CONTABILIZAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Educacional |
| **Função:** | Repasse de bolsa |
| **Situação/Requisito:** | No processo de Repasse de Bolsa, ao preencher a tabela Opcional, o sistema desconsidera a Tabela preenchida e não preenche no Lançamento Financeiro criado. O parâmetro Educacional "Origem da tabela opcional" está marcado com "Serviço". |
| **Solução/Implementação:** | Otimizado o processo de Repasse de Bolsa, quando marcado o parâmetro Educacional "Origem da tabela opcional" igual a "Serviço", o sistema não permitirá digitar uma tabela opcional na tela do processo.     Obs.: Quando o parâmetro Educacional/Financeiro/Opcionais está marcado o item "Origem da tabela opcional" igual a "Serviço", a geração de lançamentos do repasse sempre irá fixar os códigos opcionais que estão cadastrados no Serviço. |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | *NA* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
