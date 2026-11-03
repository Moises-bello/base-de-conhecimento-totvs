---
content_hash: 72bc8e9cc64591b4ff968e6035dcd615bca1d53063216e1687820c2fbfae423b
fetched_at: '2026-06-29T00:10:38.033061+00:00'
page_id: '543076894'
product: rm
source: tdn-rm
title: FISCAL01-11030 DT Transmissão/Consulta dos eventos periódicos através do R5011
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543076894
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Transmissão e Consulta de Evento Reinf |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11030 |

## **02. SITUAÇÃO/REQUISITO**

Criar um processo de transmissão e consulta dos eventos periódicos pelo 5011 para que o usuário não precise enviar evento a evento.

## **03. SOLUÇÃO**

* A transmissão pelo R-5011 selecionará todos os eventos R-20XX filhos dele, com status não transmitido, inconsistente ou rejeitado e transmitirá estes eventos.
* A consulta pelo R-5011 selecionará todos os eventos pendentes ou pendente exclusão, filhos dele, incluindo aí registros R-20XX com status pendente, R20XX com status pendente exclusão (que possuem R-9000), e eventos R-2099 e R-2098 pendentes.
* Também é possível selecionar mais de um registro R-5011 ou não selecionar registros e executar para todos
* Além disso, se o registro 5011 não tiver filhos aptos a transmissão, o sistema vai emitir um alerta.
