---
article_id: 360035556074
category: RH - Schedule (PONSCHEDULE)
content_hash: 05d2c2e9e7936071750cbbee69a01b8f6527fb5ff3fa1447114d974ea82d5aa3
fetched_at: '2026-06-28T22:44:42.708843+00:00'
product: protheus
section_id: 32419396129943
source: central-protheus
title: RH - Linha Protheus - PON - PONM070 - Como configurar o Schedule para rotina
  de Cálculo Mensal
type: support-article
updated_at: '2026-05-25T17:43:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035556074-RH-Linha-Protheus-PON-PONM070-Como-configurar-o-Schedule-para-rotina-de-C%C3%A1lculo-Mensal
---

**Dúvida**  
Como configurar o *Schedule* para automação do Cálculo Mensal (PONM070)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Existe a possibilidade de configurar a **execução** da rotina de **Cálculo Mensal** de forma **automática** e **agendada**, via ***Schedule***. Para isto, siga com as instruções abaixo:  
  
**1.** Configurar os **serviços** no **Appserver.ini** conforme exemplo abaixo:  
  
**[OnStart]**  
jobs=FWSCHDMANAG,FWSCHDQUEUE    
RefreshRate=180

**[FWSCHDMANAG]**  
Main=FWSCHDMANAG  
Environment=P1225

**[FWSCHDQUEUE]**  
Main=FWSCHDQUEUE  
Environment=P1225  
  
**2.** De primeiro momento é necessário **configurar** os processadores de **Agendamento/*****Agents***. Para isso, siga os passos abaixo:  
- Acessar o **Configurador** na rotina **Ambiente>*****Schedule>Schedule***;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464059541271)  
- No menu superior, em**Outras Ações>Adicionar agentes padrão** e/ou caso queira criar um agent interno, clicar em **Novo.**  
\*\*Estes ***agents*** serão os **responsáveis por executar** os **processos agendados**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464053395607)  
  
- Após isso, reiniciar os Agentes Criados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464053399063)  
  
**3.** Após isso, será necessário configurar o **agendamento e sua recorrência.** Siga os passos abaixo:  
- No menu lateral esquerdo, na opção **Agend.:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464059559063)**  
  
- Clicar em novo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464059562647)  
  
- Para a **execução do** ***Schedule,*** basta preencher no campo **"Rotina"** o conteúdo **PONM070:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464059564567)**  
  
- Preencher a recorrência:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464059572631)**  
  
- Informar a empresa, filial e módulo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464059575703)  
  
- Caso necessário, preencher/Editar os parâmetros, porém, a **data inicial e final** serão **desprezadas,** pois o sistema irá executar o **Cálculo Mensal** do **período aberto (atual),** de acordo com o conteúdo do parâmetro **MV\_PONMES**.  
  
A execução será limitada à 2 períodos, o atual e o seguinte, ou seja, o cálculo será realizado apenas para o período subsequente ao que estiver aberto.  
  
Seguindo o exemplo abaixo o MV\_PONMES=01/09/2025 À 30/09/2025, o schedule de Cálculo Mensal validará e se o momento de processamento do agendamento estiver ocorrendo no dia 20/10/2025, por exemplo, será executado o Cálculo Mensal de 01/09 à 30/09 e também o período de 10/2025.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464059579031)  
  
**EXEMPLO DE UTILIZAÇÃO**  
  
**Período de Apontamento:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464053422103)**  
  
**Lançamentos>Resultados:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464053427607)**  
  
  
Os **eventos** do ponto estão configurados para o [**Folha de pagamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532), por este motivo o resultado dos eventos estão presentes em **Resultados**. Caso os **eventos** do ponto estivessem configurados para ir para o **Banco de Horas**, eles estariam presentes em **Lançamentos>Banco de Horas**, conforme o print abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464053431191)  
  
**Saiba mais:**  
[Scheduler Cálculo Mensal em 2 Períodos Abertos](https://tdn.totvs.com/pages/releaseview.action?pageId=1005430922)  
[Automação do Cálculo Mensal](https://tdn.totvs.com/pages/releaseview.action?pageId=667911298)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
