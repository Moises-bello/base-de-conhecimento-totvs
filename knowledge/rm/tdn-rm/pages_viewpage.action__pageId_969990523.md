---
content_hash: 69f1cb6d024d7fe4b895166a550da881e0d125c32c065e021ef73c503a635299
fetched_at: '2026-06-29T00:12:14.674758+00:00'
page_id: '969990523'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Processo "Alterar Data Início do Afastamento"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969990523
version: 6
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Integração RM X Ahgora - Processo "Alterar Data Início do Afastamento" |
| País: | Brasil |
| Épico | [DRHROTRM-11876](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11876) |

## **02. VERSÃO**

* 12.1.2410.275
* 12.1.2502.179
* 12.1.2506.121 e superiores.

## **03. S****ITUAÇÃO/REQUISITO**

Tratar para que, a integração entre o sistema de Folha de Pagamento e o Ponto Web (Ahgora) seja atualizada, quando o processo "Alterar Data de Início do Afastamento", disponível no Histórico de Afastamento, for executado.

## **04. SOLUÇÃO**

Implementado para que ao executar o processo "Alterar Data Início do Afastamento" existente em Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico de Afastamento, o sistema gere uma exclusão e uma inclusão para o Ponto Web (Ahgora). 

Exemplo:

* + Envio original do afastamento:  
    Funcionário afastado de **05/10/2024 a 09/10/2024**.

* + Alteração realizada:  
    Nova data de início alterada para **02/10/2024**.

* + Resultado esperado na integração:

    - Exclusão do afastamento original (**05/10/2024 a 09/10/2024**);

* + - Inclusão do afastamento com o novo período (**02/10/2024 a 09/10/2024**).

IMPORTANTE:

Casonão seja utilizado o agendamento da integração, o envio deverá respeitar a ordem de processamento, sendo primeiro a exclusão e, em seguida, a inclusão.

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Ponto Web (Ahgora)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=877866931)
