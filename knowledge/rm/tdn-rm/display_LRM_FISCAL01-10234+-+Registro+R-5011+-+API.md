---
content_hash: 2bb46035947679970ed613f5a20720ed2a70546c8cfdc4e3e50eb2741067be28
fetched_at: '2026-06-29T00:10:26.091469+00:00'
page_id: '512426534'
product: rm
source: tdn-rm
title: FISCAL01-10234 - Registro R-5011 - API
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-10234+-+Registro+R-5011+-+API
version: 2
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de Eventos Periódicos - EFD Reinf |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10234 |

**02. SITUAÇÃO/REQUISITO**

De acordo com o manual da EFD-REINF o Evento R-5011 é o totalizador do período. Após o encerramento do período no ambiente da RFB este evento pode ser consultado para retornar os totalizadores calculados no ambiente da RFB com base nos Eventos transmitidos.

No TOTVS Gestão Fiscal iremos inverter a relação dos Eventos periódicos com o totalizador tornando o Evento R-5011 "pai" dos Eventos periódicos conforme abaixo.

Com esta mudança o R-5011 passa a ser utilizado como "Período dos Eventos Periódicos" e seus filhos serão os Eventos Periódicos.

Detalhes dos campos do R-5011:

* **Id. Evento Pai** deverá ser exibido um lookup para cadastro do Evento R-1000, mas não poderá ser editado;
* **Tipo:** será preenchido com o código do evento R-5011 e não deve ser editável+;+
* **Status:** deverá apresentar as opções abaixo e não ser editável.
  + Aberto: os Eventos Periódicos ainda podem ser inseridos
  + Encerrado: os Eventos Periódicos não podem ser inseridos

## Regras

* O Evento deverá ser mensal;
* Não podem existir mais de um Eventos por período;
* Ao ser cadastrado o Evento assumirá o status de "Aberto";
* O Cadastro poderá ser excluído somente se não existirem Eventos filhos com status diferente de "Não Transmitido", "Inconsistente" ou "Rejeitado".

Especificação:

[FISCAL01-9796 ER - EFD-REINF - Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=501473448)

**03. SOLUÇÃO**

Implementação das regras de validação do R-5011 conforme as regras:

* O Evento deverá ser mensal;
* Não podem existir mais de um Eventos por período;
* Ao ser cadastrado o Evento assumirá o status de "Aberto";
* O Cadastro poderá ser excluído somente se não existirem Eventos filhos com status diferente de "Não Transmitido", "Inconsistente" ou "Rejeitado".

**04. DEMAIS INFORMAÇÕES**

Url's para acesso ao serviço de Geração de Eventos Periódicos:

HEAD [http://localhost:8051/api/fiscal/v1/reinfserver/gerarevento/1|1](http://localhost:8051/api/fiscal/v1/reinfserver/gerarevento/1%7C1)

GET [http://localhost:8051/api/fiscal/v1/eventoreinf/origens/1|1](http://localhost:8051/api/fiscal/v1/eventoreinf/origens/1%7C1)

GET [http://localhost:8051/api/fiscal/v1/eventoreinf/eventosfilhos/1|1](http://localhost:8051/api/fiscal/v1/eventoreinf/eventosfilhos/1%7C1)

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
