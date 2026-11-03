---
content_hash: 39148f304d74b34447dc17b5f8657da9a4daded555e55c3a24766257a0b51a26
fetched_at: '2026-06-29T00:10:31.727515+00:00'
page_id: '522002358'
product: rm
source: tdn-rm
title: FISCAL01-10379 DT R-9000 Exclusão de Eventos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522002358
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Reinf R-9000 Exclusão de Eventos Periódicos |
| Ticket: | FISCAL01-10379 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Reinf R-9000 Exclusão de Eventos Periódicos |

## **02. SITUAÇÃO/REQUISITO**

Implementar a Transmissão e Consulta conforme definido na especificação

Especificação <https://tdn.totvs.com/display/LRM/FISCAL01-9797+ER+-+EFD-REINF+-+R-9000>

## **03. SOLUÇÃO**

**Funcionalidade: R-9000 Exclusão de eventos**

**Cenário I: Transmissão da exclusão de eventos**  
Dado que um evento pertence a um dos tipos: R-2010, R-2020, R-2030, R-2040, R-2050, R-2060 ou R-2070  
E o status do evento é Autorizado  
Ao executar o processo "R-9000 Exclusão de eventos",   
Se executado com sucesso, o status deve ser alterado para "Pendente Exclusão"

**Cenário II: Consulta da exclusão de eventos**  
Dado que um evento pertence a um dos tipos: R-2010, R-2020, R-2030, R-2040, R-2050, R-2060 ou R-2070  
E o status do evento é "Pendente Exclusão"  
Ao executar o processo "Consultar eventos",   
Se executado com sucesso, o status deve ser alterado para "Excluído"  
E as origens do evento devem ser apagadas  
Se executado com rejeição, o status deve ser alterado para "Autorizado"

**Cenário III: Nova Gerarão de eventos periódicos**  
Dado que um evento ou mais eventos dos tipos: R-2010, R-2020, R-2030, R-2040, R-2050, R-2060 ou R-2070  
foram excluídos pelo R-9000 Exclusão de eventos  
Ao executar o processo "Gerar eventos",   
Novos eventos correspondentes devem ser gerados com o status "Não transmitido".
