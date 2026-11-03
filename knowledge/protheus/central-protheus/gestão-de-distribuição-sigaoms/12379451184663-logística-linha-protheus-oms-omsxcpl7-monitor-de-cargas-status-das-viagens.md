---
article_id: 12379451184663
category: Gestão de Distribuição (SIGAOMS)
content_hash: 59be3e3ddf5fdecab82e409803f50f2030c3cbe6171f8e76dfd34d2794f9e6e6
fetched_at: '2026-06-28T22:45:49.939635+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - OMSXCPL7 - Monitor de cargas, Status das
  Viagens
type: support-article
updated_at: '2026-05-19T12:54:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12379451184663-Log%C3%ADstica-Linha-Protheus-OMS-OMSXCPL7-Monitor-de-cargas-Status-das-Viagens
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como são definidos os ***Status* de uma Viagem** na rotina de **OMSXCPL7 - Monitor de cargas**, na **integração** do **TOTVS**x**TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**O **TOL/TRE** envia as viagens geradas para o **TOTVS OMS**, para a formação das cargas, sendo que o envio é realizado pela chamada do **Web Service ReleaseTripPublishRequestService**.  
Para visualizar as **Viagens** no **TOTVS OMS**, foi disponibilizada a rotina **OMSXCPL7 - Monitor de Cargas**, que será responsável pelo gerenciamento das cargas em questão.  
  
Ao receber uma viagem com o campo **Placa - DK0\_PLACA** preenchido é realizada uma busca pela placa no cadastro de veículos, **tabela DA3**.  
  
Se encontrado algum registro, o veículo será associado a carga. Para que isso ocorra é essencial que a placa recebida do **TOL/TRE** seja idêntica a placa cadastrada no **Protheus**.  
  
Ao receber a viagem no **TOTVS OMS** serão gravadas as **tabelas DK0 - Viagem CPL** e **DK1 - Itens da Viagem CPL** com suas respectivas quantidades recebidas do **TOL/TRE**. Além disso, é registrado o código da viagem na tabela auxiliar de **Sequência de Integração TOL/TRE - DK3**, quando esta existir, mais especificamente no campo **DK3\_VIAGID**.  
  
Abaixo seguem os ***Status*** de uma **Viagem** na rotina **OMSXCPL7 - Monitor de Cargas:**

* **Viagem não gerada**: quando a viagem não é gerada, a mesma não é demonstrada no **OMSXCPL7**. Esse cenário pode ocorrer quando a **URL** de publicação de viagem apresentar algum tipo de inconsistencia. Consulte os **Logs de Integração do TOTVS  OMS** e **TOL/TRE**, também o arquivo **XML** criados na pasta **PublishReleasedTrip**. Sugerimos a revisão das configurações  dessa integração, conforme o artigo citado em **Saiba Mais**.
* **Viagem Recebida**: esse *status* é demonstrado em casos onde o **processamento da integração apresenta lentidão/delay-atraso** na comunicação.
* **Viagem Aguardando Liberação**: ao utilizar o parametro **MV\_CPLLVA** igual a 2-Nao, após gerar a viagem no **TOL/TRE**, a viagem será criada no **TOTVS OMS** com esse *status*. Sendo necessário, selecionar a **viagem** e acionar o botão **Liberar a Viagem.**
* **Viagem Liberada:** esse *status* poderá ser atualizado de forma **automatica** ou **manual**, conforme o parametro **MV\_CPLLVA**. A **viagem** liberada no **TOTVS OMS**, indica que o processo de integração do TOL/TRE e TOTVS OMS ocorreu com sucesso.
* **Viagem com Falha de Liberação: a Falha de Liberação** poderá ocorrer quando o **TOTVS OMS** ou **TOL/TRE** não conseguem responder a **integração da viagem**. Possiveis erros poderão ser consultados nos **Log's de Integração**.
* **Viagem Reprogramada**: a ação de **Reprogramar a viagem**, pode ocorrer quando a **viagem** estiver com *status* igual a **Liberada** no **TOL/TRE**. Selecione a **viagem** e execute o **botão Viagem**, em seguida **botão Reprogramar**.Após a **reprogramação**, o status da **viagem** no **TOL/TRE** é atualizado para **Distribuída**. Com *status* igual a **Distribuída** poderá efetuar manutenções na **viagem**, como por exemplo troca de itens entre viagens, enviar itens de uma viagem para outra viagem, etc.
* **Viagem Cancelada:** uma **viagem** pode ser **cancelada** pelo **TOL/TRE**, com isso no **TOTVS OMS** receberá esse *status*. Outra possibilidade seria **Desatualizar o pedido de Venda no OMSXCPL6**, para isso o pedido de venda deverá estar vinculado ao uma **Viagem.** Após desatualizar pedido, a **viagem** terá o seu *status* alterado para **Cancelada.** Para esse cenario o Sistema valida o parametro MV\_CPLATVG.
* **Viagem Rejeitada**: *status* criado para utilizar no processo de **integração do TOL/TRE** para **TOTVS OMS**, para rejeições do **TOL/TRE**.

![monitor1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/12390188189591)

Abaixo destacamos os possiveis conteudos do campo **DK0\_SITINT - Situação Integração de uma Viagem**:

* 0=Recebida
* 1=Aguardando liberação
* 2=Liberada
* 3=Falha liberação
* 4=Reprogramada
* 5=Cancelada
* 6=Rejeitada

**Importante**Temos disponiveis os **Log's de Integração** do **TOTVS OMS** e **TOL/TRE**:  
1.[Logística - Linha Protheus - OMS - Como habilitar o LOG de integração do TOTVS OMS e TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-Log%C3%ADstica-Linha-Protheus-OMS-Como-habilitar-o-LOG-de-integra%C3%A7%C3%A3o-do-TOTVS-OMS-e-TOL-TRE)  
2.No **TOL/TRE**, acesse **Interface/Configuração/Monitor de Integração/Monitor de MONITORING-INTEGRATION/Log navigation/Root/CTRL+F, procure por WS/Esse é o log de integração do TOL/TRE: monitoring-integration-publihing-ws.log****Saiba mais**Mais informações poderão ser acessadas nos *link's*:  
[Monitor de Cargas - OMSXCPL7](https://tdn.totvs.com/pages/viewpage.action?pageId=549493564)   
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Parâmetros para integrar o TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402272406551-Log%C3%ADstica-Linha-Protheus-OMS-Par%C3%A2metros-para-integrar-o-TOTVS-OMS-x-TOL-TRE)  
[Logística - Linha Protheus - OMS - Como habilitar geração de arquivo de LOGs na integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
  
**Glossário**  
**TOL**- TOTVS Otimização Logística  
**TRE**- TOTVS Roteirização e Entrega  
**TOTVS OMS**- Order Management System
