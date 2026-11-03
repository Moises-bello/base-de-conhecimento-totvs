---
article_id: 9927550638871
category: Gestão de Transportes (TMS)
content_hash: a2bdec01521a3e56b39c066d94a5beb99e341f1a218c2efe68a203a9f40bafd9
fetched_at: '2026-06-28T22:45:27.289263+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastro de nova filial para empresa que
  já utiliza o TOTVS Logística TMS
type: support-article
updated_at: '2022-11-01T13:43:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9927550638871-Log%C3%ADstica-Linha-Protheus-TMS-Cadastro-de-nova-filial-para-empresa-que-j%C3%A1-utiliza-o-TOTVS-Log%C3%ADstica-TMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:20 min** **Dúvida**Para clientes que já implantaram o **TOTVS Logística TMS** no **Protheus**, o que é necessário cadastrar novamente quando é criado uma nova filial?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Quando já foi implantado o **TOTVS Logística TMS** no **Protheus** em uma empresa e posteriormente se vê a necessidade de criar uma nova filial no Sistema, geralmente tem-se a intenção de reaproveitar os cadastros já feitos nas outras filiais, como clientes e produtos, por exemplo. Entretanto, há alguns cadastros e parâmetros que é preciso revisar e cadastrar por filial, para o correto funcionamento do Sistema:

* **Cadastros:**
  + **Atualizações/ Logística/ Estrutura de regiões - TMSA120** - Criar nova filial dentro de seu estado e definir abaixo dela o município onde está localizada fisicamente. Outros municípios do estado são opcionais estar abaixo dela.   
    No exemplo da imagem abaixo a filial de **SC - Santa Catarina** é representada pela região **FL1** e o município onde está localizada está representado pela região **O00051.**

**![](https://p23.zdusercontent.com/attachment/888110/xEfwE1tdMlyE4zKroBAF2UuPg?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..tj55SAC5S4UUb3Xll5MtyQ.MZ-kcANVi2R4g62ajbqbiThpZJBwknfSBb6MHpCl87aM5ykVEBFbc8BG_choNs-mUfZDSrL49I_mv19l8sh8b3Q960yQGjOTiRbEE4_zMIj04tQyJ9sgjjkwGzj5hVKeKLABCjYnaKUQoLsITyVv2TBlUeE6ba-HZykoVkCsTPj3VFvs7Hc03JmfPv2DA43SqPETkqlrmVk--SgyQIpAETlGcpY1D__j-cXF8AUgaUp_vK966zY2jGvH6gAu_9E73hpgBH70lARcnOyYp_3sUr8DdSaFOiPqWZzxlxcJZQs.thZiSXcNKjr3HSfs6CRcVQ)**

* + **Atualizações/ Serviços/ Tarefa x Atividade - DLGA080 -** Cadastrar atividades de chegada e saída relacionadas a nova filial;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9928948672407)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9929001454871)

* + **Atualizações/ Serviços/ Serviços x Tarefa - DLGA070 -** Cadastrar o serviço **operacional** que a filial vai utilizar em suas rotas relacionado a **tarefa x atividade** que incluiu no item anterior;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9929044621079)

* + **Atualizações/ Logística/ Rotas - OMSA100 -** Cadastrar nova rota que atenderá a operação da nova filial;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9929161476375)

* **Parâmetros**
  + **MV\_ESTADO -** Incluir um novo parâmetro exclusivo para filial indicando a **UF - Unidade Federativa** de onde está localizada;
  + **MV\_CDRORI -** Incluir um novo parâmetro exclusivo para filial indicando a região onde a filial está localizada. Seguindo o exemplo apresentado anteriormente seria **O00051**;
  + **MV\_URLQCOD -** Incluir um novo parâmetro exclusivo para filial, conforme orientado na documentação [Logística - Linha Protheus - TMS - Tag infCteSupl no CT-e versão 3.00A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035596554-Log%C3%ADstica-Linha-Protheus-TMS-Tag-infCteSupl-no-CT-e-vers%C3%A3o-3-00A)

**Saiba mais**Fluxo, cadastros e parâmetros para emissão de **CT-e - Conhecimento de Transporte Eletrônico**: [Logística - Linha Protheus - TMS - Emissão de CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025588954-Log%C3%ADstica-Linha-Protheus-TMS-Emiss%C3%A3o-de-CT-e)
