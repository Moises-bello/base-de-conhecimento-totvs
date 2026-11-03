---
content_hash: 85f9b93d104b12a844f32881e3c48e5973d954f37ee78f74eb1ea9eac37cc2f4
fetched_at: '2026-06-29T00:08:04.793319+00:00'
page_id: '235581902'
product: rm
source: tdn-rm
title: ER_PCREQ-10750_Dispensação_-_Modelo_Otimizado_Separação_Prévia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235581902
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM SAÚDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10749](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10749 "PCREQ-10749") |
| **Requisito** | * [PCREQ-10750](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10750 "PCREQ-10750") | **Subtarefa** | * [SAU\_DEV-4567](http://jira.totvs.com.br/browse/SAU_DEV-4567) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    Este documento tem como objetivo a especificação da funcionalidade "**Modelo Otimizado de Separação Prévia**" na tela do painel de dispensação.

## Definição da Regra de Negócio

 **RN001 -** Sistema deve criar um fluxo alternativo, na tela de "**Painel de Dispensação**", onde o usuário terá a possibilidade de montar o mapa de dispensação ainda na "**View**" do painel;

   **RN002 -** Na tela de detalhes do Painel, onde atualmente são exibidos todos os itens detalhadamente, deverá ser alterada a funcionalidade de processamento. Quando acionada, a funcionalidade vai verificar se os parâmetros "**Utiliza dispensação horária por requisição**" e "**Utiliza Modelo Otimizado de Separação Prévia**" estão marcados, caso estejam, vai gerar um pacote com base no campo "**CODPACOTE**", da tabela "**SZAPRAZAMENTO**", separando os conceitos de mapa e pacote;

 **RN003 -**Na tela de "**Recebimento pela Enfermagem**", sistema deverá se adequar à nova realidade, observando, no caso de os parâmetros estarem marcados, a coluna "**CODPACOTE**", ao invés da "**IDMAPA**".

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Mapa de Dispensação | Alteração | Estoques > Mapa de Dispensação | **RN001** |
| Mapa de Dispensação (Detalhe) | Alteração | Estoques > Mapa de Dispensação | **RN002** |
| Parâmetros | Alteração | Opções > Parâmetros > Parâmetros Gerais | **RN002** |
| Recebimento pela Enfermagem | Alteração | Estoques > Recebimento Pela Enfermagem | **RN003** |

**Exemplo de Aplicação*:***

* Acesse o menu "**Opções > Parâmetros > Parâmetros Gerais**", aba "**Estoques II**" e marque os parâmetros "**Utiliza dispensação horária por requisição**" e "**Utiliza Modelo Otimizado de Separação Prévia**".
* Selecione o relatório correspondente à etiqueta de pacote;
* Acesse o menu "**Prontuário**" e selecione um paciente que esteja internado e ocupando algum leito;
* Prescreva algum item para o paciente;
* Acesse o menu "**Estoques > Mapa de Dispensação**";
* inclua um filtro que permita visualizar a prescrição recém feita;
* Selecione a linha desejada e clique em "**Gerar Mapa**", na parte superior da tela. Sistema deverá atribuir aos itens um ID de Mapa;
* Caso esteja com o relatório de mapa corretamente configurado, clique em "**Imprimir Mapa**", na parte superior da tela. Sistema deverá imprimir todos os itens que tem aquele ID de Mapa.
* Dê um duplo clique em algum dos itens da prescrição. Na tela de detalhe, selecione os itens desejados e clique em "**Processar**". Sistema processará a requisição e gerará um "**CODPACOTE**", para cada item.
* Ao final do processo, sistema automaticamente gerará a etiqueta que corresponde aos itens do pacote;
* Acesse o menu "**Estoques > Recebimento Pela Enfermagem**".
* Nesta tela, deverá ser "bipado" o código de barras correspondente ao pacote, para que os itens sejam listados e confirmados pela enfermagem;
* Para efeito de testes, pode ser digitado o código do pacote, seguido de um "**0**", por exemplo: Pacote "**000013**", deverá ser digitado "**0000130**";
* Confirmar todos os itens.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
