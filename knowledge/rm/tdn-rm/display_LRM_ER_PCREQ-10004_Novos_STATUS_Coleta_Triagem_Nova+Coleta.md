---
content_hash: 7db6acbd7eba77880fcde48db7e78ddbdb613de15931b40e4e11e73a3900e676
fetched_at: '2026-06-29T00:08:04.601197+00:00'
page_id: '235575351'
product: rm
source: tdn-rm
title: ER_PCREQ-10004_Novos_STATUS_Coleta_Triagem_Nova Coleta
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10004_Novos_STATUS_Coleta_Triagem_Nova+Coleta
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM SAÚDE |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-9999](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9999 "PCREQ-9999") |
| **Requisito** | * [PCREQ-10004](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10004 "PCREQ-10004") | **Subtarefa** | * [SAU\_DEV-4248](http://jira.totvs.com.br/browse/SAU_DEV-4248) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    Esta especificação tem como objetivo detalhar a melhoria à ser implementada na funcionalidade de Controle de Pedidos de Exames, onde serão implementados 3 novos Status: Coleta, Triagem e Nova Coleta.

## Definição da Regra de Negócio

**RN001 -**Será criado um novo parâmetro, no cadastro de unidade de atendimento, que determinará se a unidade utiliza o fluxo "**Triagem, Coleta e Nova Coleta**". Caso o parâmetro esteja marcado, o comportamento será o descrito na **RN002,**caso contrário, o comportamento não deve ser alterado. 

**RN002 -**Serão adicionados aos Status já existentes, no Controle de Pedidos de Exames, 4 novos Status: Triagem - Envio, Triagem - Recebimento, Coleta e Nova Coleta. Os Status serão utilizados nas seguintes situações:

   **Em Coleta:** Logo após ao Status Inicial. Quando o pedido passar para **"Em Coleta",** o sistema dará ao usuário a possibilidade de imprimir as etiquetas, que serão anexadas às coletas. A ação de impressão das etiquetas deve avançar o Status  de "Em Coleta" para "Triagem - Envio";

   **Triagem - Envio:** Logo após o Status **"Em coleta",**este status indica que as amostras já estão etiquetadas e já foram enviadas para a coleta;

   **Triagem - Recebimento:**Ao receber a amostra, o sistema deverá ser sinalizado que o recebimento ocorreu (através da leitura das etiquetas), avançando o pedido para o status **"**Triagem - Recebimento**". Apenas neste Status será permitido ao usuário realizar a exportação das amostras para o arquivo Matrix;**

**Nova Coleta:**Este Status precede o Status Inicial e serve para reiniciar o fluxo. Ele pode ser acionado a qualquer momento, sempre que uma nova amostra necessite ser coletada. Ao mudar para este Status, o sistema deverá exigir do usuário a justificativa para a mudança, que será incluída no log de alteração de status.

**Considerações Adicionais:**

* **O sistema deve permitir que o usuário encerre o pedido à qualquer momento, pois por diversos motivos o fluxo pode ser interrompido.**
* **O sistema só poderá permitir a digitação após o Status "Triagem - Recebimento".**
* **A digitação também deve ser permitida após a exportação.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Unidade de Atendimento | Alteração | Cadastros > Uso Geral > Unidades de Atendimento | **RN001** |
| Controle de Pedidos de exames | Alteração | Unidades Diagnóstico > Controle de Pedidos de exames | **RN002** |

**Exemplo de Aplicação:**

1. Acesse o menu **"Cadastro > Uso Geral > unidades de Atendimento";**
2. Marque a opção **"Utiliza Fluxo - Coleta, Triagem, Nova Coleta";**
3. Realize um novo pedido de exame;
4. Acesse o Controle de Pedidos de Exames;
5. Avance e Retorne o Fluxo, verificando se todas as situações descritas nas **Regras de Negócio**, foram contempladas.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
