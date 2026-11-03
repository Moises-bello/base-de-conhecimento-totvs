---
article_id: 360052503033
category: RH - Ponto Eletrônico
content_hash: fc393c4047800b2c476e2fac7c9bcc3db74415eddb4169ca40bfa36c99df82d4
fetched_at: '2026-06-28T22:44:58.337966+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Validação de tolerância quando ocorre jornada fora
  do previsto na Tabela de Horário Padrão com horário fixo
type: support-article
updated_at: '2022-07-19T18:58:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052503033-RH-Linha-Protheus-PON-Valida%C3%A7%C3%A3o-de-toler%C3%A2ncia-quando-ocorre-jornada-fora-do-previsto-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-com-hor%C3%A1rio-fixo
---

**Ocorrência**Quando ocorre jornada feita em horário totalmente fora do previsto na Tabela de Horário Padrão, o sistema parece não acatar as tolerâncias cadastradas na Regra de Apontamento  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**No exemplo abaixo, a tabela de horário padrão tem este horário previsto:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083320733/mceclip0.png)  
  
O cadastro de tolerâncias da Regra de Apontamento está desta forma:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082198814/mceclip1.png)  
  
E o tipo do horário é fixo.  
  
Em um dia, o funcionário realizou as seguintes marcações e o sistema não gerou hora extra para a saída:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082223774/mceclip0.png)  
  
Neste dia, o sistema gerou hora extra e o adicional noturno sobre hora extra:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082223814/mceclip1.png)  
  
**Solução**Neste caso, como a jornada ocorreu **fora do horário previsto na Tabela de Horário Padrão**, o Sistema vai utilizar como base a **tolerância para a 4ª batida do dia**, que no exemplo utilizado é de 29 minutos tanto para **hora extra quanto para o adicional noturno sobre hora extra**.  
  
No primeiro exemplo, se realizarmos a **valorização** dos **25 minutos em hora noturna, teremos 29 minutos** gerados, portanto, não foram ultrapassadas as tolerâncias previstas, já no segundo exemplo, se realizarmos a **valorização dos 26 minutos em hora noturna, teremos 30 minutos gerados**, o que já ultrapassa as tolerâncias previstas, por este motivo, **o evento de hora extra noturna e adicional noturno sobre hora extra são gerados.  
  
Informações complementares**Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
