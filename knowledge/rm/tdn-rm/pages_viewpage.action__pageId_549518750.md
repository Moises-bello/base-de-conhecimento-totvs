---
content_hash: 3113a6eda6527ce3bd4c08aa039a39c54bc56804cdf7ff84a4b9ada161a7dc08
fetched_at: '2026-06-29T00:10:43.125035+00:00'
page_id: '549518750'
product: rm
source: tdn-rm
title: DEDUCONNECT-763 DT Erro ao incluir um cartão na carteira da bandeira ELO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549518750
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Carteira Digital Gerenciamento de Carteira Digital Pagamento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-763](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-763) |

## **02. SITUAÇÃO/REQUISITO**

Erro ao incluir um cartão na carteira da bandeira ELO.

Exemplo de iniciais do cartão: 5067 4100 ...

## **03. SOLUÇÃO**

Tratamento de imagem e cor para a bandeira ELO.  
Implementação de expressão regular para reconhecimento da imagem e cor com base no número do cartão.  
Ajuste no preenchimento to token do cartão ao efetuar um pagamento.  
Alteração do mapeamento de CardType a ser informado para o Gateway (Cybersource) para os números de cartões suportados pelo financeiro.  
Sincronização das expressões regulares de cartões com o portal.  
Ajuste do salvamento do cartão ao marcar a opção para salvar o cartão na carteira no pagamento com outro cartão.

Mais detalhes, consulte os documentos de referência: 

[11.2 - Listagem da Carteira Digital](https://tdn.totvs.com/display/LRM/11.2+-+Listagem+da+Carteira+Digital)  
[11.3 - Gerenciamento da Carteira Digital](https://tdn.totvs.com/display/LRM/11.3+-+Gerenciamento+da+Carteira+Digital)

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
