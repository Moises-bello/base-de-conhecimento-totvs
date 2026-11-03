---
content_hash: 5d3b50e2876346dcd7fb251eefeae07b40e69de9f17cc0de6b2528f7d918dce0
fetched_at: '2026-06-29T00:10:15.155910+00:00'
page_id: '463819599'
product: rm
source: tdn-rm
title: PORTALMOBILE01-6825 DT Parametrização Integração Rubeus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463819599
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Novo Portal do Processo Seletivo |
| Função: | Integração Rubeus |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [PORTALMOBILE01-6806](http://jiraproducao.totvs.com.br/browse/PORTALMOBILE01-6806) |

## **02. SITUAÇÃO/REQUISITO**

Para atender aos critérios da integração com a plataforma Rubeus, era necessário a criação de parâmetros de integração para permitir a configuração de alguns itens necessários ao funcionamento dessa integração.

## **03. PRÉ-REQUISITO**

Como pré-requisito é necessário que a máquina esteja utilizando a versão 1.2 do protocolo TLS, que é o protocolo utilizado para realizar a comunicação com a integração.

## **04. SOLUÇÃO**

A partir da versão 12.1.24, foi criada uma nova aba, dentro dos parâmetros do cadastro de processo seletivo, chamada "Integrações". Nessa nova aba, foi criado um parâmetro para determinar se a integração com o Rubeus estará habilitada para o processo seletivo em questão, além de informar dados como o endereço da API do Rubeus, bem como o Token de acesso que será necessário para a autenticação, e dados como código da origem e os tipos de evento do Rubeus que se relacionarão com as etapas do processo seletivo, durante a inscrição do candidato.

Foram realizados ajustes também nos processos de "Copiar processo seletivo" e "Copiar parâmetros entre processos seletivos", para que os parâmetros de integração com o Rubeus possam ser copiados caso os processos mencionados sejam executados.

Para o processo de "Copiar processo seletivo", a opção "Copiar todos os parâmetros do portal de inscrição?" deve estar marcado, conforme abaixo:

Para o processo "Copiar parâmetros entre processos seletivos", a opção "Copiar as integrações" deve estar marcada, conforme abaixo:

## **05. DEMAIS INFORMAÇÕES**

Mais informações estarão disponíveis no documento de referência da integração com o Rubeus.

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
