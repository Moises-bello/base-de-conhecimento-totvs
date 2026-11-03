---
article_id: 360037230354
category: Manutenção de Ativos (SIGAMNT)
content_hash: 56301aaed3247beab441d8baee9dbc843909d2d5fefdb161d5c1c93c64bb9720
fetched_at: '2026-06-28T22:42:32.977326+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Conceito da Distribuição da Solicitação
  de Serviço
type: support-article
updated_at: '2021-06-01T19:45:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037230354-Manufatura-Linha-Protheus-MNT-Conceito-da-Distribui%C3%A7%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:40 min****Dúvida**Qual o conceito da **Distribuição da Solicitação de Serviço - MNTA295**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**  
A rotina de **Distribuição de solicitação de serviço** **- SS** tem a finalidade de permitir o usuário distribuir as **SS** por executantes, também pode informar ou alterar qual o **Tipo de Serviço** a ser executado, alterar a descrição do serviço e definir a **Prioridade**.  
  
Após a distribuição da **SS** conforme análise, pode ser gerada uma ou várias ordens de serviço,**Corretiva** ou **Preventiva** se necessário.  
  
Durante a distribuição da **Solicitação de Serviço,** se já houver outra solicitação para o mesmo bem/localização e com o mesmo **Tipo de Serviço,** é emitida uma mensagem ao usuário alertando, onde pode desconsiderar e continuar o processo ou pode cancelar.  
  
Para gerar **Ordem de Serviço** do tipo **Preventiva** deve ser habilitado o parâmetro **MV\_NGSSPRE - Indica se a Solicitação de Serviço poderá gerar ordem de serviço do tipo Preventiva/Preditiva.**  
Só é possível gerar várias **Ordens de Serviço** para a mesma **Solicitação de Serviço** se o parâmetro **MV\_NGMULOS - Permite gerar múltiplas ordens de serviço a partir do retorno da distribuição**estiver ativo.
