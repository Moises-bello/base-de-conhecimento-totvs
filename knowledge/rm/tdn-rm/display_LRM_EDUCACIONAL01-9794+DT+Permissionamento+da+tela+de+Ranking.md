---
content_hash: 270c2f2a0403faab1bdb485ebc154356f0b7a4e670bec574fc9985ba3f4a16e5
fetched_at: '2026-06-29T00:10:25.370713+00:00'
page_id: '503219226'
product: rm
source: tdn-rm
title: EDUCACIONAL01-9794 DT Permissionamento da tela de Ranking
type: documentation
url: https://tdn.totvs.com/display/LRM/EDUCACIONAL01-9794+DT+Permissionamento+da+tela+de+Ranking
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Avaliação e Pesquisa |
| Função: | Ranking |
| Ticket: | #6121385 |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-9794 |

## **02. SITUAÇÃO/REQUISITO**

A tela de Ranking, anexo da tela de Provas, do módulo de Avaliação e Pesquisa, não estava obedecendo as permissões configuradas para o perfil do usuário.

## **03. SOLUÇÃO**

Foi realizado um ajuste na tela de Ranking, para que passasse a obedecer o permissionamento configurado para o perfil do usuário.

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
