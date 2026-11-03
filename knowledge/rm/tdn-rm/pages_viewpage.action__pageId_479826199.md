---
content_hash: 43122487d17b2774c02776cbb939e0ab0453974990b6bdbef48aa052ba72d1bd
fetched_at: '2026-06-29T00:10:18.325399+00:00'
page_id: '479826199'
product: rm
source: tdn-rm
title: 5338378 FISCAL01-8349 DT Escrituração Fiscal - Período de apuração do tributo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=479826199
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Escrituração Fiscal |
| Ticket: | [5338378](https://totvssuporte.zendesk.com/agent/tickets/5338378 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8349 |

**02. SITUAÇÃO/REQUISITO**

Ao escriturar o movimento, onde a data de emissão está diferente da data de lançamento, o sistema está consistindo a data da Emissão do movimento para validar se existe período de apuração aberto, porém de acordo com o Wagner Henrique do suporte fiscal, para o tributo ICMS o sistema deve considerar a data de lançamento do movimento.

**03. SOLUÇÃO**

Para sanar estes e outros casos realizamos as seguintes alterações alterações:

- Utilizar a data do ISS somente se o Movimento\Itens possuir o Tributo ISS;  
- Buscar os períodos de apuração não tomando como base somente as datas dos Movimentos que estão sendo escriturados pois temos muitas variações de periodicidade nos tributos. Passar a buscar TODOS os Períodos de Apuração dos tributos existentes nos Movimentos que estão sendo escriturados, que estejam ABERTOS e que possuem Data Inicial >= início do ano anterior do Movimento mais antigo e Data Final <= fim do ano posterior do Movimento mais recente. Dessa forma, conseguiremos abranger todas as periodicidades dos tributos e não acarretaremos sobrecarga no sistema, uma vez que estamos filtrando somente os períodos abertos e os tributos existentes no movimento.

**04. DEMAIS INFORMAÇÕES**

A situação estava ocorrendo devido a efeitos colaterais em que se passou a ser verificada sempre a "Data de ISS", independente de existir ISS no Movimento ou não. Por exemplo, considerando um Movimento de Entrada com as seguintes parametrizações:  
- Data de ISS parametrizada como Emissão = 30/01/2019  
- Data de Entrada / Saída = 01/02/2019  
O movimento deve ser escriturado no período de Fevereiro (que está aberto), porém, a consistência é realizada com o período de Janeiro (encerrado).

Além desta situação, identificamos também problemas em tributos com periodicidade trimestral.
