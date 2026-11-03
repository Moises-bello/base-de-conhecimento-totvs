---
content_hash: 4e719105951eece027b80fbd98e6fafaf3e8a1f4ce9d23a2e0c37e8428e9769e
fetched_at: '2026-06-29T00:10:25.174404+00:00'
page_id: '501476755'
product: rm
source: tdn-rm
title: EDUCACIONAL01-10160 DT Sugestão de disciplinas exibindo quantidade de vagas
  de turma livre incorretamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501476755
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Sugestão de Disciplinas |
| Função: | Número de Vagas - Turma Livre |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-10160 |

## **02. SITUAÇÃO/REQUISITO**

Foi identificado que a tela de sugestão de disciplinas estava exibindo incorretamente a quantidade de vagas de Turmas Livres. O correto é que para esses casos, a quantidade de vagas seja retirado do cadastro de turma/disciplina e não do cadastro de turma, como estava acontecendo.

## **03. SOLUÇÃO**

Foi realizado um ajuste no sistema, para que na tela de sugestão de disciplinas, o número de vagas exibidos seja sempre o valor do cadastro da turma/disciplina, para o caso de Turmas Livres.

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
