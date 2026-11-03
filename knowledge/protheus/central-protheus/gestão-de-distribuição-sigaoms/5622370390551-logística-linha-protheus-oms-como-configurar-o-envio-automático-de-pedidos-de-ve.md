---
article_id: 5622370390551
category: Gestão de Distribuição (SIGAOMS)
content_hash: eaf37b56f78a73a09fae37da0c8cab583d7cd8dbcd549e219b893b0e3d6e43d1
fetched_at: '2026-06-28T22:45:49.635912+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como configurar o Envio Automático de Pedidos
  de Venda para TOL/TRE
type: support-article
updated_at: '2022-12-01T11:03:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5622370390551-Log%C3%ADstica-Linha-Protheus-OMS-Como-configurar-o-Envio-Autom%C3%A1tico-de-Pedidos-de-Venda-para-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:18 min****Dúvida**Como configurar o **OMSXCPL6 - Envio Automático de Pedidos de Venda** para **TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Os pedidos de venda gerados no **TOTVS OMS**podem ser enviados automaticamente ao **TOL/TRE**.  
Para isso, deve ser configurada a execução automática via **Schedule** da rotina **OMSXCPL6 - Envio Automático de Pedidos de Venda.**Realize os seguintes passos para configurar o **Envio Automático de Pedidos de Venda** para **TOL/TRE:**

* No arquivo **Appserver.ini** é necessário inserir a seguinte configuração:  
    
  **[OnStart]**  
  jobs=FWSCHDMANAG,FWSCHDQUEUE  
  RefreshRate=60  
    
  **[FWSCHDMANAG]**  
  Main=FWSCHDMANAG  
  Environment=<ambiente>  
    
  **[FWSCHDQUEUE]**  
  Main=FWSCHDQUEUE  
  Environment=<ambiente>
* No **SIGACFG - Configurador/Ambiente/Schedule/Schedule/Agent:** Realizar o cadastro do **Agente**, segue exemplo:

![cadastro_agent.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/5622730840983/cadastro_agent.JPG)

* No **monitor** inicie o serviço, o *status* deverá ser atualizado para **iniciado**, conforme exemplo:

![monitor.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/5622822552855/monitor.JPG)

* Em **Agendamentos**, realize o **cadastro do agendamento para rotina OMSXCPL6-Envio de Pedidos**

****![cadastro_rotina.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5622910195351/cadastro_rotina.png)****

No exemplo acima, destacamos o botão de **Recorrência** e de **Parâmetros**, os quais deverão ser configurados de acordo com a sua necessidade.  
  
**Saiba mais**Mais informações poderão ser acessadas nos *links*:  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/viewpage.action?pageId=271167961)  
[Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS para TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011610682-Log%C3%ADstica-Linha-Protheus-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOL)  
[Integração TOTVS OMS x TOTVS Otimização Logística - Planejamento](https://tdn.totvs.com/pages/releaseview.action?pageId=268801735#Integra%C3%A7%C3%A3oTOTVSOMSxTOTVSOtimiza%C3%A7%C3%A3oLog%C3%ADstica(Planejamento)-11.1.Configura%C3%A7%C3%A3oParaEnvioAutom%C3%A1ticodePedidosdeVenda(Schedule))  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
