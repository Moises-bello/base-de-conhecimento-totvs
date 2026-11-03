---
article_id: 4406199170327
category: RH - Cadastros
content_hash: 2479524abea8a29f11696e36a468932feaf82e9b2d6a37e5fd3a4d6a134f77e8
fetched_at: '2026-06-28T22:44:53.023624+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Funcionamento do parâmetro MV_APONTAF
type: support-article
updated_at: '2025-11-10T12:17:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406199170327-RH-Linha-Protheus-PON-Funcionamento-do-par%C3%A2metro-MV-APONTAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34014198928663) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Funcionamento do parâmetro MV\_APONTAF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O parâmetro **MV\_APONTAF** foi criado para que seja possível apontar **Hora Extras** nos dias que o funcionário **trabalhou conforme previsto**, e existe um **Afastamento Médico** cadastrado.   
O **conteúdo** do parâmetro deve estar como **.T.** para que essa opção esteja habilitada.  
  
Em casos onde o funcionário trabalhou apenas **meio período** e foi ao médico, **não será lançado qualquer evento**, como por exemplo faltas, saída antecipada, hora extra e etc.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406198794135)  
  
  
Como exemplo, vamos utilizar um turno de trabalho com horário: **08h - 12h - 13h - 17h**.  
No dia **01.07**, o funcionário **trabalhou normalmente**, foi ao médico, e foi atestado por 5 dias a contar desta data.  
  
O cadastro do **Afastamento**, ficará desta forma:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406198857879)  
  
  
Acessando a rotina de **Integrados**, o funcionário tem no dia **01.07** as seguintes marcações: **07h - 12h - 13h - 17h**, ou seja, **entrou antecipadamente** e tem direito a **Hora Extra**.   
Com o parâmetro **MV\_APONTAF = .T.** , veja que mesmo o tipo do dia estando como **Não Trabalhado** (bolinha de cor preta na legenda do calendário), o sistema gera o evento de **Hora Extra**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406199070871)  
  
  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
