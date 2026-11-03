---
content_hash: 86ed6d647c85d492f3547c9c8d2f6910317da625e43a19b0558f6319810c8a1d
fetched_at: '2026-06-29T00:10:22.713272+00:00'
page_id: '498705909'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-4716 DT Período de competência para emissão de NF-e definido
  na turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498705909
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Geração de movimento por competência |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

No Educacional existe duas possibilidades de cadastro de competência para geração de NF-e, no período letivo e na parametrização por curso, porém o cliente tem em um mesmo curso, matriz e oferta turmas começando em datas diferentes e portanto precisaria definir a competência na turma.

## **03. SOLUÇÃO**

Realizamos uma melhoria no Educacional para que seja possível no cadastro da turma definir o período de competência para a geração de NF-e.

O período de competência informado no cadastro da turma terá prioridade sobre os demais locais de parametrização, por exemplo, se o Educacional estiver parametrizado para considerar a competência no período letivo e ao executar o processo de geração de movimento por competência se o período de competência da turma matriculada para o contrato estiver preenchido, será considerado a competência informada na turma, caso contrário será considerada a competência da parametrização principal.

* A aba "Movimento ( configurações para geração de NF-e )" ficará habilitada somente se o sistema estiver parametrizado para utilizar a geração de movimento por competência.
* Este recurso estará disponível para todos os cliente a partir da versão 12.1.26, porem poderá ser habilitado apos a execução do script "CN.2019.06\_03" que poderá ser solicitado ao suporte.
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
