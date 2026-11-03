---
article_id: 19205394846231
category: RH - Schedule (PONSCHEDULE)
content_hash: 48ba1ec04a0b37093a201dc2db72b61cc9d5173e5ab2594d247b20f2bdb08de8
fetched_at: '2026-06-28T22:44:42.677882+00:00'
product: protheus
section_id: 32419396129943
source: central-protheus
title: RH - Linha Protheus - PON - Como configurar o Schedule da Rotina de requisição
  da API CAROL(PONAPI01)
type: support-article
updated_at: '2025-10-20T20:13:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19205394846231-RH-Linha-Protheus-PON-Como-configurar-o-Schedule-da-Rotina-de-requisi%C3%A7%C3%A3o-da-API-CAROL-PONAPI01
---

**Dúvida**Como configurar o *Schedule* da Rotina de requisição da API CAROL(PONAPI01)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para essa configuração é necessário seguir o processo abaixo:  
  
**1.** Configurar os**serviços** no **Appserver.ini** conforme exemplo abaixo:  
**[OnStart]**  
jobs=FWSCHDMANAG,FWSCHDQUEUE    
RefreshRate=180

**[FWSCHDMANAG]**Main=FWSCHDMANAG  
Environment=P1225(inserir o nome do seu ambiente)

**[FWSCHDQUEUE]**Main=FWSCHDQUEUE  
Environment=P1225(inserir o nome do seu ambiente)  
  
**2.** De primeiro momento é necessário **configurar** os processadores de **Agendamento/*Agents***. Para isso, siga os passos abaixo:  
- Acessar o **Configurador** na rotina **Ambiente>*Schedule>**Schedule***;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19205437682711)  
  
- Acesse na aba lateral esquerda a opção***Agentes:***![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762155788311)  
  
- No menu superior, em**Outras Ações>****Adicionar agentes padrão** e/ou caso queira criar um agent interno, clicar em **Novo.**  
\*\*Estes ***agents*** serão os **responsáveis por executar** os **processos agendados**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762155793303)  
  
- Após isso, reiniciar os Agentes Criados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762155795479)  
  
**3.** Após isso, será necessário configurar o **agendamento e sua recorrência.** Siga os passos abaixo:  
- No menu lateral esquerdo, na opção **Agend.:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762155797015)  
  
- Clicar em novo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762155797783)  
  
- Para a execução do *Schedule,* basta preencher no campo "Rotina" o conteúdo PONAPI01:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762094455959)**  
- Preencher a recorrência: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762155800215)**- Informar a empresa, filial e módulo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762094462871)  
  
- Será necessário, selecionar a opção desejada nos parâmetros:  
**1.** Padrão (Apartir da última NSR lida).  
**2.** Por Período (Mês atual mais mês anteiror e futuro).  
**3.** Por Data (Selecione as datas para definir o período da busca).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762094464023)  
  
- Após configuração clique em avançar, concluir e confirmar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762094465687)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19205437705495)  
  
-Ficará conforme exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35762155805463)  
  
Ao executar o agendamento/schedule da rotina API CAROL(**PONAPI01**), após processar o agendamento o sistema gravará as marcações vindas no Clockin na tabela RR1 que ficarão prontas e aguardando o processamento da leitura/apontamento doreto no Protheus, para que essas marcações sejam gravadas e apontadas.  
  
**Saiba Mais:**  
[Schedule - Leitura/Apontamento](https://tdn.totvs.com/pages/releaseview.action?pageId=631321258)  
[Integração Protheus x Carol Clock In](https://tdn.totvs.com/pages/releaseview.action?pageId=515294516)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
