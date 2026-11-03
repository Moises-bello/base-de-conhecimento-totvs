---
content_hash: be32c71011e0320e8e483ea0636b57f6b38f4768edb32219c1b49555a8a155ca
fetched_at: '2026-06-29T00:06:06.370476+00:00'
page_id: '201730632'
product: rm
source: tdn-rm
title: ER_Importação_Exportação_Pesquisa_Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201730632
version: 6
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO DE PESSOAS | **Módulo** | RHU |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | [PDR\_RHU\_RHU007-61 Req5 - Importação de pesquisas salariais](http://jira.totvs.com.br/browse/PDR_RHU_RHU007-61 "Req5 - Importação de pesquisas salariais") | **IRM1** | [PCREQ-6303](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-6303 "PCREQ-6303") |
| **Requisito1** | [PCREQ-6307](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6307 "PCREQ-6307") | **Subtarefa1** | [PDR\_RHU\_RHU007-66](http://jira.totvs.com.br/browse/PDR_RHU_RHU007-66) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### 

## Objetivo

Será incluído no produto a funcionalidade para importação/exportação de Pesquisas Salariais e suas respectivas Medidas Estatísticas.

### 

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Valorização | Criação | Configurações -> Importação -> Pesquisas Salariais | - |
| Valorização | Criação | Configurações -> Exportação -> Pesquisas Salariais | - |

**1 - Importar Pesquisas Salariais.**

* Será adicionado um botão chamado "Configurações -> Importação -> Pesquisas Salariais" no menu da MDI, e ao ser clicado, será disparado o processo de importação.
* Na execução do processo ,o usuário deverá fornecer um arquivo xml de importação, este arquivo deverá estar formatado conforme o anexo schema.xml.
* Após executar o processo, os registros importados deverão estar disponíveis nos cadastros de "Pesquisa Salarial" e no anexo "Medidas Estatísticas".

**2 - Exportar Pesquisas Salariais**.

* Será também adicionado um botão chamado "Configurações -> Exportação -> Pesquisas Salariais" no menu da MDI, que ao ser clicado, será disparado o processo de exportação.
* Ao executar o processo, o usuário poderá informar um filtro de "Pesquisa Salarial" e obrigatoriamente deverá informar um diretório de destino
* Ao ser finalizado o processo, irá ser gerado um arquivo com o nome no formato de VPESQUISASALARIALYYYYMMDDHHMMSS.xml contendo os dados dos registros exportados no diretório informado pelo usuário.
* O formato do arquivo será o mesmo utilizado no processo de importação.

### Opcional

## Protótipo de Tela

**Protótipo 01 - Processo de importação**

**Protótipo 02 - Processo de exportação**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
