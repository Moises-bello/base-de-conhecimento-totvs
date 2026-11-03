---
article_id: 360035238674
category: RH - Cadastros
content_hash: fda0c6b287eb33652cef4a6c11aa83b177bad26ffa53db71a60d8ea79a0f4368
fetched_at: '2026-06-28T22:44:53.055189+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - O que verificar quando o turno 12x36 está gerando
  Hora Extra no Feriado
type: support-article
updated_at: '2026-02-03T18:03:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035238674-RH-Linha-Protheus-PON-O-que-verificar-quando-o-turno-12x36-est%C3%A1-gerando-Hora-Extra-no-Feriado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19068931938327) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
O que verificar quando o turno 12x36 está gerando Hora Extra no Feriado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Quando o funcionário trabalha em escala, como 12x36, e o dia trabalhado é feriado, o sistema registra esse dia como Hora Extra, pois considera o feriado como dia não trabalhado.  
  
No exemplo, na rotina **Atualizações → Lançamentos → Integrados**, ao filtrar o funcionário, o dia 15/11 aparece marcado em amarelo, indicando feriado cadastrado.  
Embora, pela escala 12x36, esse dia seja considerado trabalhado, o cadastro de feriados tem prioridade. Por isso, o sistema registra Hora Extra quando o funcionário trabalha nesse feriado. Veja:![](https://centraldeatendimento.totvs.com/hc/article_attachments/19069225310359)  
  
Para que o sistema considere o dia como Trabalhado, ignorando o feriado, na **Regra de Apontamento** **(Atualizações → Cadastro do Ponto → Regra Apontamento)**, filtre a regra do funcionário e configure o campo **Trab. Feriado** como SIM.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19070087828503)  
  
Após o ajuste, o tipo de dia passa a ser trabalhado conforme tabela de horário do funcionário e ao reapontar não serão geradas as Horas Extras Feriados e os apontamentos serão gerados conforme um dia trabalhado normal, veja:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360100907913)  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
