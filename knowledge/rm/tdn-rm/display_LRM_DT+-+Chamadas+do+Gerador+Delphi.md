---
content_hash: 352b70f408e83cbf731cc07aed328f2ea2b71585adf6dfcd223ce4fd948cdae7
fetched_at: '2026-06-29T00:11:44.688401+00:00'
page_id: '815564974'
product: rm
source: tdn-rm
title: DT - Chamadas do Gerador Delphi
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Chamadas+do+Gerador+Delphi
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
|  | Gerador Delphi |
| País: | Brasil |
| Story : | [DRHCALCRM-5580](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5580) |

## **02. SITUAÇÃO/REQUISITO**

Com a descontinuidade do Delphi será necessário tratar nos cadastros/processos/configurações do produto, retirando dos lookups e parâmetros a opção de utilizar o Gerador de Relatórios Delphi.

## **03. SOLUÇÃO**

No TOTVS Folha de Pagamento foi retirada a opção de gerar relatórios usando o gerador Delphi nos cadastros e configurações listadas abaixo:

* Funcionários | Processos | Relatórios | Relatórios de Funcionários
* Funcionários | Processos | Relatórios | Relatórios de Férias
* Funcionários | Processos | Relatórios | Relatórios de Rescisão
* Funcionários | Anexos | Movimento | Férias | Processos | Relatórios de Férias
* Funcionários | Anexos | Movimento | Rescisão| Processos | Relatórios de Rescisão
* Parametrizador | Portal | Demonstrativo de Pagamento
* Parametrizador | Portal | Férias
* Parametrizador | Portal | Informe de Rendimentos
* Configurações | Avisos automáticos
* Configurações | Envio de e-mail
