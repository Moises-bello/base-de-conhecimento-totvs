---
content_hash: 9198139c81245617c565c182cba0fd3849b999034d206f2c6f3e8c461b3cb347
fetched_at: '2026-06-29T00:10:26.902269+00:00'
page_id: '515299241'
product: rm
source: tdn-rm
title: 6472501 FISCAL01-10394 - EFD CONTRIBUIÇÕES - Não gera registro 0600
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515299241
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gerador de Saídas |
| Função: | Gerador de Saídas |
| Ticket: | 6472501 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10394 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o EFD Contribuições o registro 0600 (centro de custo) não é gerado quando a nota é de serviço de Brasília com modelo 55

## **03. SOLUÇÃO**

Foi realizada uma alteração na geração do Registro 0600, onde se aplica a seguinte regra:

* Lançamento de saída;
* Que seja modelo do documento seja 55;
* Natureza com CFPS preenchido ;
* O produto for serviço;

O lançamento será considerado serviço, gerando assim o registro.
