---
article_id: 360014909032
category: RH - Cadastros
content_hash: c8604d337a288b49e66c34d4a8b02a8e28d673c38973dbd0989bd55429557824
fetched_at: '2026-06-28T22:44:53.073300+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - PONA300 - Funcionalidade da rotina Faixa de Hora
  Extra Autorizada
type: support-article
updated_at: '2026-02-04T18:50:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014909032-RH-Linha-Protheus-PON-PONA300-Funcionalidade-da-rotina-Faixa-de-Hora-Extra-Autorizada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33722146011159) Tempo aproximado para leitura: 01:00:00 min**  
  
**Dúvida**  
Funcionalidade da rotina Faixa de Hora Extra Autorizada - PONA300.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A funcionalidade da rotina é criarmos um **intervalo de horas extras** que será autorizado ao funcionário e em apontamento ser gerado o evento autorizado.  
Para isso, será necessário alterar o campo **PA\_FAIXAHE (Faixa de Hora Extra)** na regra de apontamento para **SIM.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28645436909463)  
  
Segue exemplo abaixo:  
-> Um funcionário que possui uma Tabela de Horário Padrão das 08hs às 17hs, com 01h de intervalo:   
das 12hs às 13hs.  
-> No dia 01/08, o funcionário foi autorizado realizar Hora Extra das 17hs às 20hs:  
![61.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010018632)  
  
-> No dia 02/08 foi autorizado apenas das 17hs às 18hs como Hora Extra:  
![62.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010018932)  
  
-> Com isso, nos dois dias, o funcionário finalizou o expediente às 20hs;  
-> No dia 01 foi apontado 3 horas extras autorizadas;  
-> No dia 02 foi apontado somente 01 hora extra autorizada e 02 horas extras não autorizadas, conforme imagem abaixo:  
![63.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010040491)  
  
![64.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010019292)  
  
\*\*Para utilização correta desta rotina, é essencial que nos tipos de horas extras os eventos autorizados e não autorizados não sejam iguais.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28645436910999)  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
