---
article_id: 360026609853
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 600a672980829d3944be059ef47adb2c9ac32f519aad4178e949064056ae0642
fetched_at: '2026-06-28T22:42:44.724456+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Parametrização para produção excedente
  como ganho de produção
type: support-article
updated_at: '2021-05-11T12:04:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026609853-Manufatura-Linha-Protheus-SIGAPCP-Parametriza%C3%A7%C3%A3o-para-produ%C3%A7%C3%A3o-excedente-como-ganho-de-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura**: 00:00:55 min**  
 **Dúvida**Ao apontar uma produção maior do que a prevista na abertura da **OP - Ordem de Produção**, é possível fazer com que o Sistema sempre entenda a produção excedente como ganho de produção, sem questionar o usuário?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**É possível fazer com que o Sistema entenda que o excedente é sempre ganho de produção, para isso altere o parâmetro **MV\_GANHOPR** **- Utilizado para verificar se permite o conceito de Ganho de Produção na inclusão do apontamento de produção** para **.T.** e **MV\_PERCPRM - Percentual da quantidade das ordens de produção qual será permitido apontado a maior** para **0**, dessa forma o Sistema não questionará o usuário e assumirá automaticamente que a quantidade excedente trata-se de ganho de produção.
