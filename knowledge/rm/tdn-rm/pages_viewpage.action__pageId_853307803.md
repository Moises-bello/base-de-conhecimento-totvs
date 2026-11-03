---
content_hash: 53badc482f9dcb8c33ebd041f1fa807edebf83c02fd86112ed08014476eb3804
fetched_at: '2026-06-29T00:11:54.473309+00:00'
page_id: '853307803'
product: rm
source: tdn-rm
title: DT - Validação da Base de Dados - Retirar validação do campo PIS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853307803
version: 7
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Validação da Base de Dados - Retirar validação do campo PIS |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10467](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10467 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.230
* 12.1.2402.175
* 12.1.2406.108 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Com a entrada do FGTS Digital, o PIS deixou de ser uma informação necessária, conforme [publicação](https://www.totvs.com/blog/fiscal-clientes/numero-do-pis-fim-de-sua-obrigatoriedade/). Diante disso, o campo PIS no cadastro do funcionário não é mais obrigatório. No entanto, o processo **Validação da Base de Dados** ainda exige o preenchimento desse campo.

## **04. SOLUÇÃO**

Realizamos a tratativa no produto para que na geração do processo **Validação da Base de Dados** não seja mais validado o preenchimento do campo PIS.

## **05. DOCUMENTAÇÃO**
