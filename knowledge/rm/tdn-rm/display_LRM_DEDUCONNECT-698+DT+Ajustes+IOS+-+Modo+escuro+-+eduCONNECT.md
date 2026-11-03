---
content_hash: 3f96bbb73005c17acddbeae5f0047a06662e0e47273c23a63d65c3f92feaf7d7
fetched_at: '2026-06-29T00:10:42.237228+00:00'
page_id: '546699663'
product: rm
source: tdn-rm
title: DEDUCONNECT-698 DT Ajustes IOS - Modo escuro - eduCONNECT
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUCONNECT-698+DT+Ajustes+IOS+-+Modo+escuro+-+eduCONNECT
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Negociação inteligente Extrato Financeiro Carteira Digital Gerenciamento de Carteira Digital Gerenciamento de Pagamento Recorrente |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-698](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-698) |

## **02. SITUAÇÃO/REQUISITO**

Ajustar sombras nos frames que estavam prejudicando a visualização dos componentes na tela.  
Tratar modo escuro no IOS que fazia com que alguns componentes não exibissem a informação corretamente para o usuário (Ex.: componentes de texto exibiam o fundo preto e texto preto não possibilitando a leitura do texto).

## **03. SOLUÇÃO**

Desabilitação do modo escuro do Iphone nas páginas do eduConnect.  
Exclusão da sombra nos frames para o IOS. Foram tratadas as páginas:  
    -Extrato Financeiro  
    -Carteira digital  
    -Gerenciamento da carteira digital  
    -Gerenciamento da recorrência  
    -Valores de negociação  
    -Termo de negociação

Mais detalhes, consulte os documentos de referência: 

[11.1 Extrato Financeiro](https://tdn.totvs.com/display/LRM/11.1++Extrato+Financeiro)  
[11.2 - Listagem da Carteira Digital](https://tdn.totvs.com/display/LRM/11.2+-+Listagem+da+Carteira+Digital)  
[11.3 - Gerenciamento da Carteira Digital](https://tdn.totvs.com/display/LRM/11.3+-+Gerenciamento+da+Carteira+Digital)  
[11.6 - Gestão do pagamento recorrente - Visualização e Cancelamento](https://tdn.totvs.com/pages/viewpage.action?pageId=527384249)  
[11.7 - Negociação inteligente](https://tdn.totvs.com/pages/viewpage.action?pageId=527832872)

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
