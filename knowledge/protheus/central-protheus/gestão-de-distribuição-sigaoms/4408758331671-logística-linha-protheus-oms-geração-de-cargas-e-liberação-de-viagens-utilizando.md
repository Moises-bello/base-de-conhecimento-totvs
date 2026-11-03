---
article_id: 4408758331671
category: Gestão de Distribuição (SIGAOMS)
content_hash: 59d5b680ceae8db83826f6b085611abbea3bf4c79e9ec0cac9c9f68447947328
fetched_at: '2026-06-28T22:45:49.837946+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Geração de Cargas e Liberação de Viagens
  utilizando a integração do TOTVS OMS x TOL/TRE
type: support-article
updated_at: '2022-10-20T14:00:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408758331671-Log%C3%ADstica-Linha-Protheus-OMS-Gera%C3%A7%C3%A3o-de-Cargas-e-Libera%C3%A7%C3%A3o-de-Viagens-utilizando-a-integra%C3%A7%C3%A3o-do-TOTVS-OMS-x-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:12 min****Dúvida**Como realizar a **Geração de Cargas** e **Liberação de Viagens** utilizando a **integração** do **TOTVS** x **TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Quando a integração do **TOTVS OMS x TOL/TRE** estiver ativa, os pedidos de venda gerados no **TOTVS OMS** poderão ser integrados ao **TOL/TRE**, transformando-se em **Pedidos de Transportes,** que resultam em **Viagens,** quando recebidas pelo **TOTVS OMS**, se tornarão **Cargas**.  
  
Para a identificação do **Pedido de Transporte** no **TOL/TRE**, é utilizado o mesmo código do **Pedido de Venda** do **TOTVS OMS**, para que o usuário possa rastrear quais pedidos irão compor a **viagem**. As viagens são elaboradas no **módulo Programação**, na **rotina Análise**, disponível no **TOL/TRE.**A ação dentro do **TOL/TRE** que dispara a mensagem de **viagem publicada** para o **TOTVS OMS** é a **Liberação.**Logo, após a elaboração da viagem no **TOL/TRE**, esta deverá ser liberada para o **TOTVS OMS**, selecionando a viagem e executando o **botão Liberar**.  
  
Após a **Liberação da viagem** pelo **TOL/TRE**, a viagem se mantêm com o *status* igual a **Sincronizando**, até que o **TOTVS OMS** realize sua **Liberação**.  
  
Exemplo:

* Antes de realizar a **Liberação** e o **envio** para o **TOTVS OMS**:

![cpl01.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408760363287/cpl01.JPG)

* Após a **Liberação** e **aguardando** a resposta do **TOTVS OMS**:

![CPL02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408767292311/CPL02.png)

* Após resposta de **Liberação** **recebida** do **TOTVS OMS:**

**![cpl03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408760866583/cpl03.png)**

* **A viagem** será gerada no **Monitor de Cargas - OMSXCPL7:**

**![CPL04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408760962839/CPL04.png)**

* A **viagem** poderá ser criada de forma automática com *status* igual a **Liberada.** Posicione sobre a viagem, qual deseja gerar a carga no **TOTVS OMS**, selecione a **opção** **Gerar Carga.** Assim, o Sistema irá gerar  uma **nova carga** na rotina **Montagem de Cargas -  OMSA200.**

**Importante**  
A **Liberação de Viagem e a Geração da Carga** podem ser parametrizadas para serem geradas de forma automática no **TOTVS OMS**. Os parâmetros envolvidos são: **MV\_CPLAUT** e **MV\_CPLLVA**. Logo abaixo, em **Saiba mais**, no artigo **Logística - Linha Protheus - OMS - Parâmetros para integrar o TOTVS OMS x TOL/TRE**, estão descritos todos os parâmetros envolvidos nessa integração.

**Saiba mais**Mais informações poderão ser acessadas nos *link's*:  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Parâmetros para integrar o TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402272406551-Log%C3%ADstica-Linha-Protheus-OMS-Par%C3%A2metros-para-integrar-o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS para TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011610682-Log%C3%ADstica-Linha-Protheus-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOL)  
[Logística - Linha Protheus - OMS - Como habilitar geração de arquivo de LOGs na integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na Integração TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003568682-MP-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-Integra%C3%A7%C3%A3o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
