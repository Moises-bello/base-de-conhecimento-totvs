---
article_id: 360004053911
category: RH - Ponto Eletrônico
content_hash: 2b96a0a91312a182e1fe7c198db0b1825925b99c382b010bf9a981f3e12cfeeb
fetched_at: '2026-06-28T22:44:58.262606+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON -  Como funcionam as horas extras autorizadas e não
  autorizadas
type: support-article
updated_at: '2023-06-16T16:43:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004053911-RH-Linha-Protheus-PON-Como-funcionam-as-horas-extras-autorizadas-e-n%C3%A3o-autorizadas
---

**Dúvida** Como funcionam as horas extras autorizadas e não autorizadas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para determinar se uma Hora Extra calculada será autorizada ou não autorizada, são envolvidos os seguintes cadastros no processo:  
  
1 - **Regra de Apontamento**:  
No **campo Pg. Hora Ext.** nós podemos definir em **quais batidas do dia trabalhado, o evento da hora extra será autorizado ou não autorizado**.   
Este campo não determina para o sistema se os funcionários terão ou não horas extras, apenas determinam se o tipo do evento será autorizado ou não autorizado.  
Por exemplo, se deixarmos todas as opções marcadas, as horas extras feitas em qualquer batida nos dias trabalhados, serão autorizadas:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099297493)  
  
Ainda na **Regra de Apontamento**, nós temos o campo **Pg. He. Dia. Nt.**, este campo define se a hora extra será autorizada ou não para os dias não trabalhados.  
Por exemplo, se deixarmos todas as opções marcadas, os dias Compensado, DSR, Feriado e Não Trabalhado terão horas extras calculadas como autorizadas.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096988314)  
  
2 - **Tipos de Horas Extras**:  
Através desta rotina, o sistema saberá qual evento e tipo de hora extra deverá calcular para os funcionários durante o período.  
Para o correto funcionamento, precisamos cadastrar os oito primeiros tipos de horas extras, iniciando no tipo Normal e finalizando no tipo Noturna Feriado. Nestes cadastros, nós vamos vincular os eventos, e é de extrema importância que não ocorra repetição de códigos de eventos, como exemplo abaixo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096989214)  
  
Com toda a parametrização feita, se por exemplo, meu funcionário que está vinculado à um turno diurno fizer hora extra em um dia Trabalhado, sei que o evento gerado será o 101 que trata-se de uma hora extra autorizada. Se ocorrer hora extra em dia Compensado, o evento será o 105 e assim sucessivamente.
