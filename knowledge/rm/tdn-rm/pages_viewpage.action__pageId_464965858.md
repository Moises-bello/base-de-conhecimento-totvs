---
content_hash: af36803013c55a83fc03c9c465663b4e8953e138038463beb02a67d157885f28
fetched_at: '2026-06-29T00:10:15.384386+00:00'
page_id: '464965858'
product: rm
source: tdn-rm
title: 5013704 FISCAL01-8108 DT NFS-e - Regime Especial de Tributação como NULL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=464965858
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Fiscal |
| Função: | Envio NFS-e |
| Ticket: | 5013704; 5194905 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8108; FISCAL01-8126 |

## **02. SITUAÇÃO/REQUISITO**

No cadastro da filial foi criado o campo 'Regime Especial de Tributação - NFS-e/TSS'. Mesmo o   
campo estando em branco no sistema, na base de dados o campo REGIMEESPECIALTRIB fica com   
valor 50 (tabela DFILIAL). Ao tentar a transmissão da NFS-e para municípios que não aceitam o valor 50 ocorre a mensagem abaixo:

Não foi possivel enviar o(s) movimento(s) da Coligada 8, Filial 1,   
Tipo Movimento 2.2.01.TOTVS Service SOA TSS : [SchemaX]TSS999135436Element 'regimeesptrib':   
[facet 'pattern'] The value '50' is not accepted by the pattern '0|1|2|3|4|5|6|7|8|9|10'.  
Element 'regimeesptrib': '50' is not a valid value of the atomic type '

{tss\_nfse\_tipos\_v2.00}  
tstpregimetrib'.

## **03. SOLUÇÃO**

No cadastro da Filial foi incluída a opção "Não se Aplica" para o campo   
"Regime Especial de Tributação - NFS-e/TSS" assim quando está opção for selecionada  
no envio da NFS-e a tag "regimeesptrib" não será gerada.

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
