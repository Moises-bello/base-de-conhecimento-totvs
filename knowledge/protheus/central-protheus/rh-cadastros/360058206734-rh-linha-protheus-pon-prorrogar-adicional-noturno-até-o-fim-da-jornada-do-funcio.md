---
article_id: 360058206734
category: RH - Cadastros
content_hash: b7fb01fda8233b3f92be1e351073250de7924e4ef4dc195929d6549281ccecc9
fetched_at: '2026-06-28T22:44:53.090206+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Prorrogar adicional noturno até o fim da jornada
  do funcionário, mesmo que inicie após as 22:00
type: support-article
updated_at: '2025-12-10T13:00:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058206734-RH-Linha-Protheus-PON-Prorrogar-adicional-noturno-at%C3%A9-o-fim-da-jornada-do-funcion%C3%A1rio-mesmo-que-inicie-ap%C3%B3s-as-22-00
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34216783260183) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como prorrogar adicional noturno até o fim da jornada do funcionário, mesmo que inicie após as 22:00?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Segue abaixo, como devem estar configurados os campos para que o adicional noturno seja prorrogado, até o final da jornada de trabalho, mesmo que o funcionário iniciou após as 22:00.  
  
Para configuração acesse o cadastro de turno de trabalho, em **Atualizações> Cadastros Gerais> Turnos de Trabalho**, filtre o turno e clique em Alterar, valide e configure os campos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31779025314455)​  
  
Em **Atualizações> Cadastro do Ponto> Regras Apontamento**, aba Apontamentos configure o campo Pror. Ad. Not. = 1-Sim:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31779025323287)​  
  
Ainda na rotina Regras Apontamento, aba Outros configure o campo Per.Pro.Ad = 1-Sim:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31779025325975)​  
  
  
Após estes cadastros, ao efetuar a leitura e apontamento das marcações o adicional noturno será apontado até o fim da jornada do funcionário, tendo sempre como base, o hora que ele iniciou.  
  
Em **Atualizações> Lançamentos> Integrados**, veja como ficou os apontamentos:   
No exemplo, o funcionário trabalha das 00h as 10h o sistema vai apontar 10h/52,50\*60=11h26 de adicional noturno. Veja exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31779014587031)  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como gerar o Adicional Noturno e Adicional Noturno sobre Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004252711-RH-Linha-Protheus-PON-Como-gerar-o-Adicional-Noturno-e-Adicional-Noturno-sobre-Horas-Extras)
