---
content_hash: 21f6560e816fb7b4c511794a75258ddab30d2ce930c242bd7252cc7b67cb6c00
fetched_at: '2026-06-29T00:10:20.214169+00:00'
page_id: '489781240'
product: rm
source: tdn-rm
title: EDUCACIONAL01-8896 DT Importador - STURMADISC - Turno da Turma/Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=489781240
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Gestão Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Importador - STURMADISC |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-8896 |

## **02. SITUAÇÃO/REQUISITO**

Ao importar a turma/disciplina (STURMADISC) não é possível informar um turno que seja diferente da matriz aplicada da turma/disciplina. No cadastro da turma/disciplina é possível informar um turno que seja diferente da matriz aplicada da mesma.

## **03. SOLUÇÃO**

O importador foi alterado para que seja possível informar um turno diferente da matriz aplicada da turma/disciplina pelo campo TURNOTURMADISC. Entretanto este campo funcionará da seguinte forma, se o campo TURNOTURMADISC:

* Estiver sido informado e for válido a turma/disciplina receberá este turno em seu cadastro;
* Não estiver sido informado ou informado com valor inválido, a turma/disciplina receberá o turno da sua matriz aplicada.

Para informações de como utilizar o importador bem como os layouts de importação, segue link da documentação: <http://tdn.totvs.com/x/2MhgDQ>.

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
