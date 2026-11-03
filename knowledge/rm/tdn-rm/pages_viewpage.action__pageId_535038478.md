---
content_hash: 7af4d7a468e12533407b0a4f0cacf00d7155fcce9146dd2c6fb281befc2b02a3
fetched_at: '2026-06-29T00:10:37.085110+00:00'
page_id: '535038478'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-6619 DT Cálculo dos Valores Auxiliares para Bolsas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535038478
version: 25
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Inclusão/alteração lançamento financeiro |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUINTEGRACOES-6619](https://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-6619) |

## **02. SITUAÇÃO/REQUISITO**

Diante de alguns cenário apresentados pelos cliente surgiu a necessidade de controlar de forma paralela e especifica valores relacionados ao processamento das bolsas calculados durante geração do lançamento financeiro do aluno.

## **03. SOLUÇÃO**

Criamos o recurso de  que serão processados durante a geração do laçamento financeiro da parcela.

Para cada bolsa processada para a parcela do contrato do aluno o sistema executará as fórmulas vinculadas aos valores auxiliares cadastrados e que são aplicados a "Bolsa".

Importante

Serão processados somente os valores auxiliares ativos e inativo em que a validade seja inferior a data de vencimento da parcela.

Os valores retornadas pela fórmula previamente parametrizada no cadastro do valor auxiliar serão gravados nas tabelas:

SVALORAUXBOLSALAN

* Tem como objetivo armazenar os valores auxiliares por bolsa conforme os dados presentes na tabela **SBOLSALAN**.

Exemplo:

* A Parcela possui uma bolsa ( cód. bolsa 37)
* Dois valores auxiliares cadastrados ( Id. 4 - VAUX001 /Id. 7 - VAUX002)

Apos a geração do lançamento financeiro da parcela os dados serão gravados conforme a imagem abaixo.

SVALORAUXBOLSALANDESCPONTUAL

* Tem como objetivo armazenar os valores auxiliares executado para cada bolsa da parcela e para cada vencimento do desconto por antecipação processado para o contrato do aluno, ou seja, conforme os dados presentes na tabela **SBOLSALANDESCPONTUAL** .

Exemplo:

* A Parcela possui uma bolsa condicional ( cód. bolsa 35)
* Dois valores auxiliares cadastrados ( Id. 4 - VAUX001 /Id. 7 - VAUX002)
* Desconto por antecipação com 4 vencimentos ( conforme a imagem abaixo )

Apos a geração do lançamento financeiro os valores auxilares processados serão gravados na tabela **SVALORAUXBOLSALANDESCPONTUAL** conforme o exemplo abaixo.

Importante

1. O valor demonstrado acima será o valor retornado pela fórmula associada ao valor auxiliar, ou seja, contempla a regra pré estabelecida pelo cliente.
2. Será gravado na tabela **SVALORAUXBOLSALANDESCPONTUAL** somente bolsa condicionais que tem o seu valor impactado pelo desconto por antecipação, para maiores informações recomendamos consultar o documento
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
