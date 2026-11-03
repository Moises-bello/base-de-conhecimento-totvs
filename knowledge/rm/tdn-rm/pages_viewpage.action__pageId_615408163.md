---
content_hash: fc7ba6f276e6a58467f8751d1e6f6c775185a0d1cb76d351b5323eef61045f0a
fetched_at: '2026-06-29T00:10:59.751105+00:00'
page_id: '615408163'
product: rm
source: tdn-rm
title: Alterações nos processos de edição da AAFDT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=615408163
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Automação de Ponto |
| Função: | Processos da AAFDT |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | PONTO01-11583 |

## **02. SITUAÇÃO/REQUISITO**

Separar os processos de **Edição individual de batidas** e **Exclusão de batidas do espelho**, que antes eram usados também para os processos de exclusão.

## **03. SOLUÇÃO**

Foram criados mais dois processos, um para **Exclusão individual de batidas** e outro para **Exclusão de batidas do espelho**. Desta forma, ao consultar na tabela AAFDT as informações das batidas coletadas, será possível identificar quais foram excluídas através das telas de edição do Automação de Ponto.

Com a inclusão dos novos processos, o mapa ficará da seguinte forma:

0 → Importação manual  
**1 → Edição individual de batidas**  
2 → Lançamento global de horários  
3 → Inclusão manual  
4 → Lançamento global de batidas  
**5 → Edição de várias batidas do espelho**  
6 → Aprovação de batidas  
7 → Gerada pelo conversor  
8 → Cancelar movimento  
9 → Desaprovar batidas  
10 → Importação XML  
11 → Customizações  
12 → Desconsideração de batidas fora do perímetro  
**13 → Exclusão individual de batidas**  
**14 → Exclusão de várias batidas do espelho**

Portanto, as exclusões que antes eram utilizadas com os processos 1 e 5, agora passam a ser definidas pelos processos 13 e 14. As edições continuarão sendo identificadas pelos processos 1 e 5.

## **04. DEMAIS INFORMAÇÕES**

**As batidas que tiveram alterações antes desta implementação, permanecerão com os processos 1 e 5. Somente batidas alteradas após esta implementação ficarão com os códigos dos novos processos.IMPORTANTE!**

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
