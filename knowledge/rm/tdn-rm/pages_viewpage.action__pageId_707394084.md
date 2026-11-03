---
content_hash: 6d07887c49273a401632a69c6f67d419fadfab7e428c0d462d658223e4fe772d
fetched_at: '2026-06-29T00:11:23.177273+00:00'
page_id: '707394084'
product: rm
source: tdn-rm
title: DT - Férias Compulsórias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=707394084
version: 12
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Férias Compulsórias |
| País: | Brasil |
| Ticket: | S/N |
| Requisito/Story/Issue (informe o requisito relacionado) : | <https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2831>  <https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2571>  <https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2573> |

## **02. SITUAÇÃO/REQUISITO**

**Conforme descrito na central de atendimento:**

Atualmente as férias compulsórias são marcadas automaticamente através do parâmetro 'Marcar automaticamente férias em dobro ao liberar competência', disponível em **RM | RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Férias |  Férias em Dobro**, de acordo com a quantidade de dias informada no campo 'Qtd. de dias a ser considerado para marcação'.  Com este parâmetro marcado, no processo de Liberação de competência será feita a marcação de férias para todos os funcionários que possuem férias em dobro ou que tenham férias à vencer.

As férias do funcionário serão marcadas para a primeira segunda-feira da próxima competência.

Como o processo de Liberação de Competência pode ocorrer nos dias 2 ou 3 do mês e esses dias poderiam ser após a segunda-feira do próximo mês,  desta forma não teria o tempo legal para pagamento das férias (dois dias úteis antes do início do Gozo)  e/ou aviso das férias (trinta dias antes do início da férias), portanto não estava atendendo as necessidades das empresas.

## **03. SOLUÇÃO**

Para atender as necessidades dos clientes. foi implementado em  **RM | RH | Folha de Pagamento | Férias | Processos**,o módulo **Marcar Férias Compulsórias**.

## **04.****ASSUNTOS RELACIONADOS**

* [Férias Compulsórias](https://tdn.totvs.com/pages/viewpage.action?pageId=708092095)
