---
article_id: 4409386353047
category: Gestão de Distribuição (SIGAOMS)
content_hash: 4f5d849f4b16fb05427bb28c7f5e91c46014aad25e452a68cf268fbd35c5ac8d
fetched_at: '2026-06-28T22:45:50.140579+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Reprogramar a Viagem no TOL/TRE, quando
  integrada ao TOTVS OMS
type: support-article
updated_at: '2022-12-01T11:10:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409386353047-Log%C3%ADstica-Linha-Protheus-OMS-Reprogramar-a-Viagem-no-TOL-TRE-quando-integrada-ao-TOTVS-OMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:24 min** **Dúvida**Qual  a **funcionalidade de Reprogramar a Viagem** no **TOL/TRE**, quando integrada ao **TOTVS OMS**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Quando a integração do **TOTVS OMS** x **TOL/TRE** estiver ativa, os pedidos de venda gerados no **TOTVS OMS** poderão ser **integrados ao TOL/TRE**, transformando-se em **Pedidos de Transportes**, que resultam em **Viagens**.  
  
Caso tenha necessidade de realizar **manutenções na viagem** gerada no **TOL/TRE**, poderá realizar o processo de **Reprogramar a viagem**. As viagens são elaboradas no **módulo Programação**, na **rotina Análise**, disponível no **TOL/TRE**.  
  
A ação de **Reprogramar a viagem**, pode ocorrer quando a viagem estiver com ***status* igual a Liberada**. Selecione a viagem e execute o **botão Viagem**, em seguida **botão Reprogramar**.  
  
Após a **reprogramação**, o *status* da viagem no **TOL/TRE** é atualizado para **Distribuída**. Com *status* igual a **Distribuída** poderá efetuar **manutenções na viagem**, como por exemplo **troca de itens entre viagens** ou **cancelamento**.

![reprogramada1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4409542893079/reprogramada1.jpg)

![reprogramada2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4409549679255/reprogramada2.JPG)

Para que seja possível **reprogramar** as viagens do **TOL/TRE** é necessário configurar as informações de conexão com o **DBAccess** diretamente na seção ***Environment*,** modificando o arquivo **Appserver.ini** do **TOTVS OMS**, conforme exemplo abaixo:  
  
Nome do Ambiente acessado pelo **Web Service**  
**[Environment]**  
SourcePath=C:\Totvs\Protheus\Apo  
RootPath=C:\Totvs\Protheus\Data  
StartPath=\system\  
. . . ; outras chaves  
**DBDatabase=MSSQL**  
**DBAlias=PLS101**  
**DBServer=192.168.1.20**  
**DBPort=7890**Além da configuração arquivo **Appserver.ini** do **TOTVS OMS,** no **TOL/TRE**, acesse **Configuração/Integração**, selecione **Fontes de Dados** e clique em **Inserir** ou **Alterar** caso exista. Digite o **código**, **nome** e a **descrição**.  
  
Em **Serviços para tarefas de integração**, no campo **URL**, digite: **http://<ip ou nome>:<porta>/neolog/ReprogramService.APW.**No campo **Tempo Máximo de Espera por Resposta**, informe o ***timeout* do serviço,** recomendado **30000**.  
Clique em **Salvar**.   
  
O processo de **reprogramação** de viagem gera arquivo **XML de comunicação** do **TOTVS OMS** x **TOL/TRE** na pasta **reprogramservice**. Essa pasta é criada automaticamente na **primeira reprogramação** efetuada no ambiente, caso tenha o **bloco** abaixo definido no arquivo **Appserver.ini WS** do **TOTVS OMS:**  
  
**[NEOLOG]**  
**Debug=1**  
**DebugPath=Neolog**Caso não tenha o bloco acima definido no arquivo **Appserver.ini WS**, os arquivo **XML de comunicação**  serão criados  na pasta **system/neolog da instalação do Protheus.** **Importante**No **TOTVS OMS,** no **monitor de carga - OMSXCPL7,** a viagem pode ser gerada com ***status* igual a Liberada** de forma automática, para isso o parâmetro **MV\_CPLLVA** deverá estar preenchido como **1.**  
**Quando a viagem no TOTVS OMS**, no **monitor de carga - OMSXCPL7, estiver** com *status* igual a **Reprogramada**, se desejar **desatualizar o pedido** pela rotina **envio de pedidos - OMSXCPL6**, o Sistema não permitirá, apresentando a mensagem **TripThatContainsOrderItemIsNotEditable** - A viagem contém  item do pedido não é editável. A **desatualização** poderá ocorrer quando a viagem estiver com *status* igual a **Distribuída** no **TOL/TRE**.  
  
**Saiba mais**Mais informações poderão ser acessadas nos *link's*:  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Como habilitar geração de arquivo de LOGs na integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
