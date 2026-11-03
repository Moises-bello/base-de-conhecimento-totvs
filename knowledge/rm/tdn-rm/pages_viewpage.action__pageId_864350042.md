---
content_hash: ef3565adab86a9fd11584ff71b86d898b1159c7a1b70be4c77d6ef212a59965e
fetched_at: '2026-06-29T00:11:55.870323+00:00'
page_id: '864350042'
product: rm
source: tdn-rm
title: DT - Processo Trabalhista - S-2500 NT04/2024
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864350042
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Processos Trabalhistas |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue: | [DRHHCM-13073](https://jiraproducao.totvs.com.br/browse/DRHHCM-13073) / [DRHHCM-12788](https://jiraproducao.totvs.com.br/browse/DRHHCM-12788) |

## **02. SITUAÇÃO/REQUISITO**

Adequações referentes à nota técnica 04/2024 da mensagem S-2500 - Processo Trabalhista.

* Grupo **{ideResp}** – alterada condição para aceitar informação do responsável direto no caso de **{tpContr} = [6,8];**
* Campo **{tpContr}** do grupo **{infoContr}** – alterada validação para aceitar informação do responsável direto no caso de **{tpContr} = [6,8];**

Atenção

**Regras do grupo ideResp:**

* **Obrigatório se {tpContr} = [8];**
* **Obrigatório na Ocorrência se {tpContr} = [6];**
* **Não informar nos demais casos;**

**ideResp** equivale aos campos **Tipo inscrição e Número inscrição** na aba **Identificação do processo:**

**tpContr**equivale ao campo **Tipo**na edição de registro na aba **Contrato de trabalho:**

Valores 6 e 8 informados nas regras:

**6 - Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício**

**8 - Responsabilidade indireta**

## **03. SOLUÇÃO**

Realizado ajustes informando o usuário qual campo deve ser preenchido caso não obedeça as regras acima.

## **04. DEMAIS INFORMAÇÕES**

          Não se aplica.

## **05. ASSUNTOS RELACIONADOS**

<https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-no-042024-revisada-28-06-2024.pdf>

<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html>

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
