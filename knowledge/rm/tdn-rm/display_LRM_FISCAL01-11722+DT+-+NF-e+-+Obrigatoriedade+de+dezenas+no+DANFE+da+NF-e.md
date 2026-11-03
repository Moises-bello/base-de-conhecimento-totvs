---
content_hash: c8d4b76fcb639e8fbb142c0bb27cdb2d7f954b40caadb42e797d34084619505b
fetched_at: '2026-06-29T00:10:32.063034+00:00'
page_id: '525029932'
product: rm
source: tdn-rm
title: FISCAL01-11722 DT - NF-e - Obrigatoriedade de dezenas no DANFE da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11722+DT+-+NF-e+-+Obrigatoriedade+de+dezenas+no+DANFE+da+NF-e
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Fiscal |
| Função: | Impressão do Relatório DANFE |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11722 |

## **02. SITUAÇÃO/REQUISITO**

O Estado de Mato Grosso do Sul deverá implementar o programa da Nota MS Premiada a partir de 01/01/2020, que visa a fomentar a cidadania fiscal, estimulando o consumidor final a exigir do estabelecimento varejista a emissão de documento fiscal (no caso, Nota Fiscal de Consumidor Eletrônica – NFC-e ou Nota Fiscal Eletrônica – NF-e) durante a aquisição de mercadorias, na expectativa de receber prêmios.

A sistemática de premiação que se pretende implantar consiste na geração, no momento da autorização do documento fiscal pela SEFAZ/MS, de dezenas que darão direito ao consumidor a concorrer a prêmios.

Por essa razão, solicitamos que entre em contato com o desenvolvedor do sistema de emissão de NF-e e de NFC-e do seu estabelecimento para que ele adeque esse software para imprimir as referidas dezenas no DANFE da NF-e e da NFC-e, conforme especificado a seguir, até 31/12/2019.

Para que essa implantação tenha pleno êxito, no momento da autorização pela SEFAZ/MS, o software emissor de NFC-e ou de NF-e deverá:

1) Capturar a informação das dezenas geradas pela SEFAZ/MS, que estarão disponíveis no arquivo XML de retorno do protocolo de autorização, tanto da NF-e quanto da NFC-e, na tag xMsg para cMsg = 200: 100 Autorizado o uso da NF-e 200 Dezenas: ( 06 11 19 38 45 50 54 )

2) Fazer constar essa informação das dezenas no DANFE da NF-e, que deverá ser impressa na área “Reservado ao Fisco”.

## **03. SOLUÇÃO**

Foi modificado o provider e o Relatório DANFE 4.0 da NF-e para imprimir a mensagem retornada pela SEFAZ através da TAG xMsg do grupo protNFe no quadro "Reservado ao Fisco", conforme definido na solicitação

## **04. DEMAIS INFORMAÇÕES**

Os campos xMsg e cMsg foram incluídos na NF-e através da NT.2018.005 sem restrição de UF e sem definição de quais serão as possíveis mensagens retornadas. Desta forma entendemos que todas as mensagens retornadas devem ser impressa no DANFE no quadro "Reservado ao Fisco" e por este motivo não foram adicionados restrições de UF nem de código da mensagem (cMsg) para a impressão do conteúdo da TAG xMsg, ou seja, sempre que a SEFAZ retornar este campo preenchido o mesmo será impresso no DANFE.

**Será necessário atualizar o TSS e importar a versão mais recente do DANFEIMPORTANTE!**

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
