---
article_id: 360041823214
category: Recrutamento e Seleção de Pessoas (SIGARSP)
content_hash: ad9eb822d95c9da7f8660aa559e2d5a727191e47e9efa58f63e87c2ba3d436c9
fetched_at: '2026-06-28T22:43:00.907752+00:00'
product: protheus
section_id: 206960907
source: central-protheus
title: RH - Linha Protheus - RSP - Configuração necessária para realizar admissão
  de vaga com controle de posto
type: support-article
updated_at: '2021-04-06T19:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041823214-RH-Linha-Protheus-RSP-Configura%C3%A7%C3%A3o-necess%C3%A1ria-para-realizar-admiss%C3%A3o-de-vaga-com-controle-de-posto
---

**Dúvida**O que conferir ao tentar realizar uma admissão através do módulo Recrutamento e Seleção de Pessoal e apresentar esta mensagem "O sistema está configurado para utilizar visão organizacional e não existe nenhuma visão com essa estrutura cadastrada. Verifique o MV\_ORGCFG".  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055870474/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recrutamento e Seleção de Pessoal - Todas as versões  
  
**Solução**O sistema gera a mensagem porque o parâmetro MV\_ORGCFG está como 1. Sendo assim, quando você cadastra o funcionário, o sistema solicitará que você amarre um departamento e um posto de trabalho. O departamento que estiver neste funcionário precisará existir em alguma visão (RDK) e nesta visão deverá conter o campo "Hierarquia (RDK\_HIERAR) = 2 e o campo RDK\_TIPO = 1. Somente desta forma a mensagem não será gerada e a inclusão finalizará corretamente.  
  
Para as Vagas geradas com controle de posto precisa ter o cadastro de Visão do tipo comunicação (2).  
  
No módulo SIGAORG (70), acesse o menu Atualizações > Estrutura > Visões e ajuste o campo Hierarquia:

![](https://totvssuporte.zendesk.com/attachments/token/d0PVVuYBcqHj8xwrHR4DrL8gu/?name=inline1415372022.png)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[Central de Artigos Recrutamento e Seleção](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960907-RH-Recrutamento-e-Sele%C3%A7%C3%A3o-de-Pessoal)
