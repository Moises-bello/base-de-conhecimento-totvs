---
content_hash: 6c908c1643ba803c942a220dfaacf5c271141b2f8e985ad2dc0ba32fb79c9009
fetched_at: '2026-06-29T00:10:30.295913+00:00'
page_id: '519716142'
product: rm
source: tdn-rm
title: DT - Descrição do Aviso Automático no Campo Assunto do e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519716142
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Recursos Humanos |
| Módulo: | Folha de Pagamento |
| Função: | Avisos Automáticos |
| Ticket: | 6535749 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FOPROTINAS01-9851 |

## **02. SITUAÇÃO/REQUISITO**

Até a versão 12.1.26, ao enviar um aviso automático via e-mail, o campo "assunto" do e-mail é preenchido com o tipo do aviso automático. Em situações em que há mais de um aviso cadastrado para o mesmo tipo, o destinatário pode receber vários e-mails distintos com o mesmo assunto, o que gera uma experiência ruim para este usuário.

## **03. SOLUÇÃO**

A partir da versão 12.1.27, o sistema passa a levar, além do tipo do aviso automático, a descrição cadastrada:

O e-mail enviado terá o campo "assunto" preenchido utilizando o padrão <Tipo do Aviso> - <Descrição do Aviso>, conforme exemplo:

## **04. DEMAIS INFORMAÇÕES**

**Essa funcionalidade está disponível nas versões 12.1.24, 12.1.25 e 12.1.26 mediante a marcação do parâmetro "Enviar descrição do aviso automático no assunto do e-mail", no parametrizador do módulo de folha de pagamento, na etapa "Avisos Automáticos".IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

* [Configuração Processo Aviso Automático](https://tdn.totvs.com/pages/viewpage.action?pageId=452719365)

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
