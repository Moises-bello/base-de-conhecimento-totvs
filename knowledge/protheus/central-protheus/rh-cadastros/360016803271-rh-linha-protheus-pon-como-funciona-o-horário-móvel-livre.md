---
article_id: 360016803271
category: RH - Cadastros
content_hash: 99c1c9982ae05c4e3886ff285d6e35c65029658a59855fd898f706bac2140c87
fetched_at: '2026-06-28T22:44:52.872054+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como funciona o Horário Móvel Livre
type: support-article
updated_at: '2026-02-04T17:06:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016803271-RH-Linha-Protheus-PON-Como-funciona-o-Hor%C3%A1rio-M%C3%B3vel-Livre
---

**Dúvida**  
Como funciona o Horário Móvel Livre?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O **Horário Móvel Livre é uma modalidade de horário que tem algumas particularidades**, como:  
  
1 - O sistema neste caso, não considera os horários de entradas/saídas cadastrados na Tabela de Horário Padrão, mas avalia a quantidade de horas que o funcionário deve trabalhar no dia, exemplo: 08h, 12h, etc;  
2 - O funcionário pode entrar/sair quando quiser e quantas vezes quiser, contanto que ao final do dia, cumpra a quantidade de horas trabalhadas previstas;  
3 - Nesta modalidade de horário, todos os apontamentos são feito com base na saída. Como o funcionário pode ter várias batidas e entrar em qualquer horário, no final do dia será contabilizado a quantidade de horas trabalhadas e será confrontado: quanto foi feito versus o quanto previsto no dia. Se o funcionário trabalhou menos que o previsto, será gerado evento de saída antecipada, se o funcionário trabalhou mais que o previsto, será gerado evento de hora extra. Nessa modalidade de horário nunca é gerado evento de atraso;  
4 - Não é possível cadastrar tolerância para cada uma das batidas do dia, justamente por existir a liberdade do funcionário entrar/sair quantas vezes quiser, portanto, só é possível cadastrar tolerância por período.  
  
A **parametrização** do Horário Móvel Livre deve ser feita **através** da **Regra de Apontamento**, aba de Horário Móvel, conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000028582)

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Conceito e funcionamento de horário móvel](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004195191-RH-Linha-Protheus-PON-Conceito-e-funcionamento-de-hor%C3%A1rio-m%C3%B3vel)  
[SIGAPON - Tolerância para Hora Extra e Horas Não Realizadas](https://tdn.totvs.com/pages/releaseview.action?pageId=496398394)  
[RH - Linha Protheus - PON - Como funcionam as horas extras autorizadas e não autorizadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004053911-MP-PON-Como-funcionam-as-horas-extras-autorizadas-e-n%C3%A3o-autorizadas?source=search)  
[RH - Linha Protheus - PON - Como gerar o Adicional Noturno e o Adicional Noturno sobre Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004252711-MP-PON-Como-gerar-o-Adicional-Noturno-e-Adicional-Noturno-sobre-Horas-Extras?source=search)
