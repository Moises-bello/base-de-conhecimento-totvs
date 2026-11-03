---
article_id: 4409677400343
category: Gestão de Distribuição (SIGAOMS)
content_hash: 03b8c5e58815428d2c467794d19af723be73f389ad5ddeceac369ba434ee7f7e
fetched_at: '2026-06-28T22:45:49.590232+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Cancelar Viagem gerada no TOL/TRE, quando
  integrada ao TOTVS OMS
type: support-article
updated_at: '2022-10-20T14:07:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409677400343-Log%C3%ADstica-Linha-Protheus-OMS-Cancelar-Viagem-gerada-no-TOL-TRE-quando-integrada-ao-TOTVS-OMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:36 min** **Dúvida**Como realizar o **Cancelamento de uma Viagem** gerada no **TOL/TRE**, quando integrada ao **TOTVS OMS**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Quando a integração do **TOTVS OMS**  x **TOL/TRE** estiver ativa, os pedidos de venda gerados no **TOTVS OMS** poderão ser integrados ao **TOL/TRE**, transformando-se em **Pedidos de Transportes**, que resultam em **Viagens**.  
  
O **cancelamento de uma viagem** gerada no **TOL/TRE**, poderá ser realizado acessando o **módulo Programação**, na rotina **Análise**, disponível no **TOL/TRE**. Selecione a **viagem**, acione o **botão viagem**, localizado na parte inferior da tela, em seguida pressione a opção **Cancelar**. Conforme exemplo abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410717032983/mceclip2.png)

Apenas viagens em **criação, distribuídas, com oferta cancelada ou liberadas podem ser canceladas.**  
  
Para que seja possível **cancelar** as viagens do **TOL/TRE** é necessário configurar as informações de conexão com o **DBAccess** diretamente na seção **Environment,** modificando o arquivo **Appserver.ini** do **TOTVS OMS**, conforme exemplo abaixo:  
  
Nome do Ambiente acessado pelo **Web Service**  
**[Environment]**  
SourcePath=C:\Totvs\Protheus\Apo  
RootPath=C:\Totvs\Protheus\Data  
StartPath=\system\  
. . . ; outras chaves  
**DBDatabase=MSSQL**  
**DBAlias=PLS101**  
**DBServer=192.168.1.20**  
**DBPort=7890**Além da configuração arquivo **Appserver.ini** do **TOTVS OMS,** no **TOL/TRE**, realize os procedimentos abaixo:

* Acesse **Configuração/Integração**, selecione **Fontes de Dados** e clique em **Inserir** ou **Alterar** caso exista. Digite o **código**, **nome** e a **descrição**.  
  Em **Serviços para tarefas de integração**, no campo **URL**, digite:  
  **http://<ip ou nome>:<porta>/neolog/CancelService.APW.**No campo **Tempo Máximo de Espera por Resposta**, informe o ***timeout* do serviço,** recomendado **30000**.  
  Clique em **Salvar**.
* Acesse **Configuração/Integração**, selecione **Geral** e marque os seguintes itens: **Permissão:** Permitir o cancelamento de uma viagem liberada.  
  **Solicitações:** Solicitação de cancelamento de viagem ligada.

O processo de **cancelamento** **de viagem** gera arquivo **XML de comunicação** do **TOTVS OMS** x **TOL/TRE** na pasta **cancelservice**. Essa pasta é criada automaticamente, assim que ocorrer o **primeiro cancelamento** efetuado no ambiente. Para isso é necessário informar o **bloco** abaixo definido no arquivo **Appserver.ini WS** do **TOTVS OMS**:**[NEOLOG]**  
**Debug=1**  
**DebugPath=Neolog** **Parâmetros que interferem no Cancelamento:**

* **MV\_CPLESCG:** Permite estorno automático da carga ao cancelar ou reprogramar viagem?   
  Indica se será permitido efetuar o estorno automático da carga ao cancelar ou reprogramar uma viagem. Quando o usuário do **TOL/TRE** solicitar o cancelamento ou reprogramação da viagem, caso exista carga montada no **TOTVS OMS** esta será estornada.
* **MV\_CPLATVG:** Atualiza a viagem no **TOL/TRE** ao cancelar a integração do pedido?   
  Indica se será atualizada a viagem no **TOL/TRE** ao cancelar a integração no **TOTVS OMS**. Se esse parâmetro estiver definido como 1-Sim, ao cancelar um item integrado que já encontra-se em uma viagem, será solicitada a alteração da viagem no **TOL/TRE** para que reflita os ajustes sofridos no **TOTVS OMS.**

**Importante**No quadro abaixo descrevemos os principais resultados ao **Cancelar uma Viagem no TOL/TRE**:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410730416791/mceclip4.png)

**Saiba mais**Mais informações poderão ser acessadas nos *link's*:  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Parâmetros para integrar o TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402272406551-Log%C3%ADstica-Linha-Protheus-OMS-Par%C3%A2metros-para-integrar-o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Como habilitar geração de arquivo de LOGs na integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
