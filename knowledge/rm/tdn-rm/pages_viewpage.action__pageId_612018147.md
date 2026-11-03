---
content_hash: 59e4137ed4b33b506326b1d45af14cb728b808b3b2e7f547b2595ac8e0ee87c5
fetched_at: '2026-06-29T00:10:59.181405+00:00'
page_id: '612018147'
product: rm
source: tdn-rm
title: Importa batidas fora do perímetro - Integração RM x Carol Clock-In
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=612018147
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Automação de Ponto |
| Função: | Controle de importação de batidas |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | PONTO01-11446 |

## **02. SITUAÇÃO/REQUISITO**

Controlar a importação de batidas fora do perímetro que são importadas pela integração com a Carol Clock-In.

## **03. SOLUÇÃO**

Criação de parâmetro para controle das batidas fora do perímetro. Quando marcado, as batidas fora do perímetro serão importadas normalmente para todas as tabelas, e quando desmarcado, as batidas fora do perímetro não serão importadas para o espelho do funcionário, porém permanecerão no sistema para geração do relatório AFDT das Portarias 1510/2009 e 373/2011.

Passo 01passo1yespasso1

1. No módulo de Automação de Ponto, acesse a aba **Configurações** e selecione o menu **Parametrizador**. Neste menu, selecione a opção **Iniciais** e avance até a etapa **Integração**. O parâmetro **Importa batidas fora do perímetro** ficará visível caso o parâmetro **Considera integração com as batidas da Carol** esteja **marcado**.

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

**Este processo é irreversível, portanto se a opção for desmarcada, não será possível reconsiderar estas batidas.IMPORTANTE!**

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
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
