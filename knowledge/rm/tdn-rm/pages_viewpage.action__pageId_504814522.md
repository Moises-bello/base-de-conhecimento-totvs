---
content_hash: b2ca0d7e2e2f0db934df1a067e6295d82818702415c55a9810e1b7992ba57b14
fetched_at: '2026-06-29T00:10:25.413140+00:00'
page_id: '504814522'
product: rm
source: tdn-rm
title: 6375471 MATESTCNTFTOF01-5995 DT Transferência entre Locais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=504814522
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Manutenção |
| Função: | Transferência entre Locais |
| Ticket: | 6375471 |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-5995 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a movimentação de um patrimônio através de criação de movimentos, quando o patrimônio possui vínculo com objeto de manutenção é executado a rotina de transferência de objeto de manutenção. Como os movimentos são criados na mesma data, a data de movimentação considerada é a data do movimento sem o horário, e com isso o serviço do manutenção apresenta uma exceção de que já existe uma transferência na data informada, pois na rotina do manutenção ele valida data e hora.

## **03. SOLUÇÃO**

Implementado uma melhoria no método de transferência de objeto de manutenção consumido pelo Patrimônio, para que a transferência seja realizada somente quando o centro de custo, localização ou filial do objeto de manutenção for diferente do enviado pela transferência de controle. As consistências de data de transferência passa a considerar apenas Data, ignorando Hora, minutos e segundos.

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

**Disponível a partir da Biblioteca RM versão 12.1.23.222 ou superior.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**


div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
