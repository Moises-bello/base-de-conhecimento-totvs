---
content_hash: 7b38de110e73a320a8b0b068dba34133322ee81617828ae7cfdfb682cb22c035
fetched_at: '2026-06-29T00:10:16.002323+00:00'
page_id: '466323952'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-2218 DT Execução da contabilização por competência multi contexto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=466323952
version: 16
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Contabilização por competência |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

A contabilização/estorno por competência processa apenas contratos do contexto corrente, ou seja, o contexto que o usuário está logado.

Para executar o processo de contabilização para outro contexto, o usuário necessita logar no contexto desejado e posteriormente executar o processo, este procedimento tem um alto custo para instituições que possuem muitos contextos.

## **03. SOLUÇÃO**

Implementamos no processo de contabilização/estorno a opção “Habilitar multi contexto”. Esta opção possibilita ao usuário selecionar um filtro que especifique quais os contextos deverão ser processados.

Ao marcar a opção "Habilitar multi contexto" deverá ser informado obrigatoriamente um filtro para identificar quais os contextos serão processados.

Exemplo:

Opcionalmente poderá ser informado um filtro genérico que complementara o filtro multi contexto, se não for informado nenhum filtro genérico o sistema executará a contabilização/estorno para todos os contratos carregados conforme o filtro do contexto.

Informações

* Se a opção "Habilitar multi contexto" estiver marcada, não será possível utilizar o filtro por período letivo / matriz aplicada e o filtro por consulta SQL, pois as informações processadas por estes filtros são diferentes entre os contextos.
* Será possível definir no perfil do usuário se será restringido o acesso a opção de execução do processamento multi contexto.

Em função da flexibilização dos filtros o processo poderá contabilizar e estornar uma grande quantidade de contratos, o que poderá aumentar o tempo de processamento.

Com objetivo de melhorar a performance, o sistema poderá fracionar o processamento por contexto e em pacotes com o número de contratos definidos pelo usuário gerando vários processos em paralelo.

Conheça mais o fracionamento do processo [<<clicando aqui>>](http://tdn.totvs.com/pages/viewpage.action?pageId=465385372)!

Importante

A opção "Habilitar multi contexto" só ficará visível se o processo de contabilização / estorno for chamado fora da visão de contratos e com o fracionamento de processos habilitado.

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
