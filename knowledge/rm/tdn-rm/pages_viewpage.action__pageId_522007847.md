---
content_hash: 67e0e0a1268f7bdea73e5163e37be402916d802fb086d44d54a26e2e9769ead3
fetched_at: '2026-06-29T00:10:31.757405+00:00'
page_id: '522007847'
product: rm
source: tdn-rm
title: FISCAL01-11534 DT EFD REINF Validar período de apuração na geração do XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522007847
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Validação dos Eventos Periódicos (R-2010, R-2020, R-2030, R-2040, R-2050, R-2060) |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11534 |

## **02. SITUAÇÃO/REQUISITO**

No Processo EFD-Reinf - Gerar Eventos → Permitir a geração do xml dos eventos 2010, 2020, 2030, 2040, 2050 e 2060 somente se os períodos de apurações correspondentes estiverem encerrados.

## **03. SOLUÇÃO**

Implementação da Validação de Período Encerrado para os Eventos Abaixo:

INSS - R-2010, R-2020, R-2030 e R-2040  
FUNRURAL - R-2050  
CPRB - R-2060

Comportamento: Na geração dos eventos periódicos se houver período de apuração com status **Aberto** pertinentes aos eventos. O processo ira emitir uma mensagem sinalizando quais períodos devem ser encerrados.

Documentação de Referência:
