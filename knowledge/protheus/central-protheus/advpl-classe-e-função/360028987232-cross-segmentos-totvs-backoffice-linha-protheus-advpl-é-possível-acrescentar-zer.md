---
article_id: 360028987232
category: ADVPL - Classe e Função
content_hash: 7bd2b7e7288b994066cb79168f405812c3d55f9005a3c99072a1bcdb8c8b7295
fetched_at: '2026-06-28T22:40:19.391735+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - É possível acrescentar
  zeros a esquerda? STRZERO()
type: support-article
updated_at: '2024-01-29T14:43:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028987232-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-acrescentar-zeros-a-esquerda-STRZERO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20942367128215)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**É possível acrescentar zeros a esquerda em uma variável numérica?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Para tal existe a função STRZERO no qual, a partir de um numérico, esta função retorna uma string formatada, inserindo zeros à esquerda e/ou o símbolo decimal (".") em suas casas, de acordo com as informações do parâmetro.

Obs.: Existe uma limitação na linguagem **ADVPL**, onde só é permitido o uso de até 8 casas decimais, desse modo se você utilizar a função **STRZERO**() e informar no parâmetro de casas decimais um valor maior que 8, o sistema não ira retornar o valor esperado.

**Saiba mais**

[StrZero](https://tdn.totvs.com/display/tec/StrZero)
