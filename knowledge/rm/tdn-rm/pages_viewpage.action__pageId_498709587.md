---
content_hash: 0706d1809bffa587802bc9c45df18796c647b9d8a0a1fe98d8371b608f4c1899
fetched_at: '2026-06-29T00:10:22.734196+00:00'
page_id: '498709587'
product: rm
source: tdn-rm
title: FISCAL01-9579 DT EFD Contribuições - F100 (Rendimentos registrados no Extrato
  de Caixa) - Criar Grupo no Cadastro de Processos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498709587
version: 7
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Contribuições |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9579 FISCAL01-9581 |

**02. SITUAÇÃO/REQUISITO**

Cliente solicita que o F100 do EFD Contribuições seja considerado o extrato de caixa uma vez que se trata de rendimento de conta.

Empresa do Lucro Real.

Desde de 1º de abril de 2015 foi publicado o decreto nº 8.426/2015 que restabelece as alíquotas da Contribuição para o PIS/PASEP e da COFINS incidentes sobre receitas financeiras auferidas pelas pessoas jurídicas sujeitas ao regime de apuração não-cumulativa das referidas contribuições.

**03. SOLUÇÃO**

**Cadastro de Processo:**

Foi adicionada a opção "EFD Contribuições" no campo Processo e a opção  "F100" no campo Grupo do Processo do Cadastro de Processo.

Imagem

Validações:

O Grupo "Registro F100" só poderá ser selecionado para o Processo "EFD Contribuições".

**Filtro de Operações**

Foi modificado o cadastro de processo para permitir cadastrar um filtro de operação com a origem Extrato de Caixa quando o processo for referente ao F100.  
Para o F100 será possível selecionar somente origem Extrato de caixa e o Lookup para o Cadastro de Conta Caixa

Imagem

Validação:

* Se for realizado um tentativa de cadastrar uma conta caixa que já foi cadastrada em outro filtro de operação para o mesmo processo será apresentado erro de duplicidade e o cadastro não poderá ser salvo.

Imagem
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
