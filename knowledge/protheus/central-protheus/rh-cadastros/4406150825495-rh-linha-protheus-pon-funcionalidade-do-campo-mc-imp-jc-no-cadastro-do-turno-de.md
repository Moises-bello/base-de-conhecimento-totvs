---
article_id: 4406150825495
category: RH - Cadastros
content_hash: 3bbefb44a73072a4849365ac16970e46d243d30387b907cb94cd19e5e541c9df
fetched_at: '2026-06-28T22:44:53.002663+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Funcionalidade do campo Mc. Imp. JC. no cadastro
  do Turno de Trabalho
type: support-article
updated_at: '2025-09-26T13:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406150825495-RH-Linha-Protheus-PON-Funcionalidade-do-campo-Mc-Imp-JC-no-cadastro-do-Turno-de-Trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29374106922391) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Funcionalidade do campo Mc. Imp. JC. no cadastro do Turno de Trabalho.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – todas as versões  
  
**Solução**Se o campo **Mc. Imp. JC.** estiver preenchido como **APLICA AJUSTE**, e o funcionário se **esquecer** de **marcar o ponto na saída** do expediente, no momento em que for feita a Leitura/Apontamento, o sistema **lança** de forma **automática** a **entrada do dia seguinte como saída do dia anterior**.  
Como exemplo, vamos utilizar um turno das 08h - 12h - 13h - 17h:  
- Campo no cadastro do **Turno** está como **Aplica Ajuste**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406143337751)  
  
  
- No dia **01.07**, o funcionário **não** registrou a **saída** do expediente às 17h:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406150603415)  
  
  
- Depois de processar a Leitura das marcações do dia **02**, veja que o sistema **alocou a entrada feita às 08h como saída do dia 01**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406143068055)  
  
  
Veja que as **marcações** do dia **02** ficaram **ímpares** e sem um **horário de "saída"**, com isso, a **entrada** do dia **03** **seria alocada como saída do dia 02 e assim sucessivamente**, portanto, **recomendamos que este campo SEMPRE fique como NÃO APLICA AJUSTE**, para evitar situações como a descrita na documentação.  
  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como cadastrar um Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho)  
[RH - Linha Protheus - PON - Marcações sendo gravadas em dias incorretos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057320114-RH-Linha-Protheus-PON-Marca%C3%A7%C3%B5es-sendo-gravadas-em-dias-incorretos)  
[RH - Linha Protheus - PON - Passos a verificar quanto a montagem do calendário de marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361412-RH-Linha-Protheus-PON-Passos-a-verificar-quanto-a-montagem-do-calend%C3%A1rio-de-marca%C3%A7%C3%B5es)
