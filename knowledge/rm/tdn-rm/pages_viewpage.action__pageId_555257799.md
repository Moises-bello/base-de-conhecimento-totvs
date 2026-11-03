---
content_hash: 28cce4a11be84aee7038174041ead09978b7751ffd36c8e5cb56b1152569dddf
fetched_at: '2026-06-29T00:10:46.588326+00:00'
page_id: '555257799'
product: rm
source: tdn-rm
title: 8791873 FISCAL01-13233 DT - NFS-e - Maringá/PR - Geração da tag IncentivoFiscal
  por serviço.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555257799
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e - Municipal |
| Ticket: | 8791873 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13233 |

## **02. SITUAÇÃO/REQUISITO**

O cliente nos informa que para a Prefeitura de Maringá/PR há um incentivo fiscal somente para os serviços de graduação. Atualmente no ERP RM, a tag em questão é gerada a partir da marcação da flag  
'INCENTIVOCULTURAL' no cadastro da filial. Portanto, o cliente necessita de uma adequação do ERP para seja possível gerar a flag a partir de algum parâmetro no cadastro do serviço. Seguem os dados do cliente e da  
legislação em questão.

Legislação:  
<https://leismunicipais.com.br/a/pr/m/maringa/lei-ordinaria/2006/736/7359/lei-ordinaria-n-7359-2006-institui>[-o-programa-municipal-de-bolsas-de-estudo-promube](https://leismunicipais.com.br/a/pr/m/maringa/lei-ordinaria/2006/736/7359/lei-ordinaria-n-7359-2006-institui-o-programa-municipal-de-bolsas-de-estudo-promube)

## **03. SOLUÇÃO**

● Criação de uma flag “Possui Incentivo” no cadastro do produto | Anexo | Tributos do Produto por  
Município.

● Adicionado a regra para o sistema considerar no envio da NFS-e se a flag “Possui Incentivo” está  
marcada, caso sim será gerado a tag “incentcult”. Caso estiver desmarcada o sistema irá verificar a flag  
“Incentivo Cultural” no cadastro da Filial no envio da NFS-e, caso nenhuma das flags estiver marcada, a  
tag não será gerada.

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
