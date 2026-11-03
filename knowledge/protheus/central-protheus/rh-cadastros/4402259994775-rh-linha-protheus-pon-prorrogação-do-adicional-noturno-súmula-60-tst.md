---
article_id: 4402259994775
category: RH - Cadastros
content_hash: 1436fdc18b08d072d8823e8dc767abd05e7cb26c2317ecd817aeb4c0b9a5ad21
fetched_at: '2026-06-28T22:44:53.086464+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Prorrogação do Adicional Noturno - Súmula 60 -
  TST
type: support-article
updated_at: '2026-04-23T12:54:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402259994775-RH-Linha-Protheus-PON-Prorroga%C3%A7%C3%A3o-do-Adicional-Noturno-S%C3%BAmula-60-TST
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34205041685783)****Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como estender o adicional noturno conforme **Súmula** **60 - TST - Prorrogação do Adicional Noturno**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
**1.** Cadastre os horários na [**Tabela de Horário Padrão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o) **(Atualizações>Cadastro do Ponto>Tabela de Horário padrão)**, determinando horários em todos os dias da tabela, **inclusive nos dias não trabalhados,** conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402259860119)  
  
**2.** No cadastro de **Regra de Apontamento (Atualizações>Cadastro do Ponto>Regra de Apontamento)**, existem campos que determinam este conceito:  
- Na **aba Apontamentos,** o campo **Pror. Ad. Not** que prorroga o Adicional Noturno;  
- Na **aba Outros**, o campo **Per. Pro Ad** prorroga o adicional até o final de jornada.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402253051671)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402259909143)  
  
**3.** Cadastre ao menos os 8 primeiros [tipos de Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314) **(Atualizações>Cadastro do Ponto>Tipos Horas Extras)**, com eventos **diferentes entre eles;**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36910751431319)  
  
**4.** No [**cadastro de Eventos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450836887-RH-Linha-Protheus-PON-Como-utilizar-o-cadastro-de-evento-do-ponto-eletr%C3%B4nico) **(Atualizações>Cadastro do Ponto>Eventos),** cadastre os Eventos vinculados aos [**IDs de Ponto 028A (Adicional Noturno H.E) e 004A (Adicional Noturno);**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004252711-RH-Linha-Protheus-PON-Como-gerar-o-Adicional-Noturno-e-Adicional-Noturno-sobre-Horas-Extras)  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402253104151)  
  
**5.** Com o funcionário alocado neste turno e nesta regra, faça o **reapontamento,** onde o Sistema **prorrogará o adicional noturno até o final da jornada** conforme exemplos abaixo:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402253113111)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402259954455)  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402253133847)  
  
**\*\*\***Exemplo feito com horário fixo na regra de apontamento, por isso, a existência do evento Atraso.  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como gerar o Adicional Noturno e Adicional Noturno sobre Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004252711)
