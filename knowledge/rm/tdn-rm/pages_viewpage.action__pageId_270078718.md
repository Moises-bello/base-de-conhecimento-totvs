---
content_hash: 872117aea799a9e610f0c4f1fb96385b3bafe68a609a01749bdb2458a2666ed8
fetched_at: '2026-06-29T00:08:23.316869+00:00'
page_id: '270078718'
product: rm
source: tdn-rm
title: 249945_DT_Importação_Conceito_Lançamentos_Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270078718
version: 113
---

# Importação de Lançamento Contábil via Conceito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Importação de Lançamento Contábil via Conceito |
| **Situação/Requisito:** | Ao importar lançamentos via conceito o sistema esta carregando o valor incorreto para coligada da 'Contra Partida' porém esse campo não foi informado no arquivo que contem os lançamentos contábeis. |
| **Solução/Implementação:** | Ajuste no processo de importação para que no caso do conceito antigo que carrega o valor -99 para as coligadas das contas de Débito, Crédito e Contra Partida esse valor seja também substituído para NULL quando a conta em questão não for informada no arquivo. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
