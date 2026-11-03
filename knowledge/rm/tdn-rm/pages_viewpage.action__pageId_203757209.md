---
content_hash: 5b74faf634945652bde879eca248a9453cbd9f06e043bce27bdb1b2c416f811d
fetched_at: '2026-06-29T00:06:09.782347+00:00'
page_id: '203757209'
product: rm
source: tdn-rm
title: ER_PCREQ -6537_SAÚDE_CIH_FLUIG_12.1.9_PENDÊNCIAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203757209
version: 1
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS CIH | **Módulo** | MENU LATERAL |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAÚDE\_CIH\_FLUIG\_12.1.9 | **IRM1** | * [PCREQ-6530](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-6530 "PCREQ-6530") |
| **Requisito1** | * [PCREQ-6537](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6537 "PCREQ-6537") | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

Fluxo para apresentação de pendências relacionadas ao Controle de Infecção Hospitalar.

### Definição da Regra de Negócio

O CIH executará alguns fluxos que irão gerar pendências para os perfis logados.

 

                As pendências deverão ser apresentadas e agrupadas conforme abaixo:

 

* Tarefas Pendentes: apresentar o número de prontuários que possuem informações cadastrais faltantes. Ou seja, prontuários que estão com o Status de Importação = vermelho.
* Pendências de Importação: apresentar o número de importações que não foram realizadas com sucesso. Buscar a informação do log de importação.

 

 

Observação: Inicialmente o CIH possuirá somente um perfil, então as pendências deverão ser apresentadas para todos os usuários logados.

 

### Protótipo de Tela

### Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
