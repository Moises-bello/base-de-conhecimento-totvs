---
article_id: 1500011640302
category: Encargos
content_hash: d7f6ecfdebc081b0e16e3d03bcf1383e49da8d29245b5f7469d19c3b2406c2a5
fetched_at: '2026-06-28T22:46:53.230344+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Provisão de férias na situação do não pagamento de 1/3 do abono
  e 1/3 de férias - MP 1.046
type: support-article
updated_at: '2025-03-05T19:39:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011640302-RH-RM-FOP-Provis%C3%A3o-de-f%C3%A9rias-na-situa%C3%A7%C3%A3o-do-n%C3%A3o-pagamento-de-1-3-do-abono-e-1-3-de-f%C3%A9rias-MP-1-046
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Realizar a provisão de férias e abono quando não realizado o pagamento de 1/3 de férias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Causa**Após o pagamento das férias, o período aquisitivo é fechado. E mesmos nos casos onde não são fechados, o processo de provisão considera somente como devido os avos restantes, não contabilizando o passado. No caso do abono pecuniário e 1/3 de abono pecuniário que não foram pagos juntos das férias, o sistema não entende que existe este débito não provisionando o valor devido.

Para solucionar este cenário gerando a provisão com o valor devido, o módulo Folha de Pagamento disponibiliza no parametrizador o recurso de fórmulas, que permite informar uma fórmula para adicionar no valor de férias vencidas ou proporcionais no final da geração da provisão.  
  
**Solução**

Abaixo exemplificarmos uma sugestão de Fórmula para que seja somada na provisão de Férias:

Calculamos e lançamos as férias para o funcionário conforme o exemplo acima. Foi lançado somente os dias de férias e não lançamos o abono pecuniário, 1/3 de abono pecuniário e 1/3 de férias. Para facilitar a identificação do adicional devido, inserimos o evento de base de cálculo no envelope do funcionário com os respectivos valores.

No parametrizador, na menu **Férias | Fórmula**s, inserimos uma fórmula que retorna o valor do 1/3 de férias devido, o valor do abono pecuniário e o valor de 1/3 de abono pecuniário. No nosso exemplo colocamos no campo para somar com férias vencidas:  
  
![](https://tdn.totvs.com/download/attachments/615606796/image2020-4-5_20-2-33.png?version=1&modificationDate=1620241104937&api=v2)  
  
Na fórmula utilizada, usamos a variável MV que retorna a soma do evento de base de cálculo B099, B198 e B199 pago durante o ano de 2021 e abatemos os eventos de proventos que serão usados para pagar o abono pecuniário, 1/3 de abono pecuniário e 1/3 de férias quando for o caso [Folha ou Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=615919977). Assim, quando o pagamento for efetuado o mesmo não será mais somado na provisão:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018802302/mceclip0.png)

|  |
| --- |
| (MV(0,'2021','B099') + MV(0,'2021', 'B199')+ MV(0,'2021','B198')) - (MV(0, '2021', '6005') + MV(0, '2021', '6015') + MV(0, '2021', '6006') + MV(0, '2021', '6016') + MV(0, '2021', 'P020') + MV(0,'2021', 'P199') + MV(0, '2021', 'P198') |

Ao gerar a provisão, o valor pago de férias no mês foi informado e o valor retornado pelo fórmula somado ao campo de provisão de férias vencidas:  
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_14-56-53.png?version=1&modificationDate=1620928613100&api=v2)  
  
Após o pagamento do Abono pecuniário e 1/3 de abono pecuniário que será exemplificado no tópico abaixo, a provisão não considerou o valor do Abono pecuniário e 1/3 de abono pecuniário:  
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_16-30-25.png?version=1&modificationDate=1620934225143&api=v2)  
  
**Saiba mais:**[Provisão de Férias conforme MP 1.046](https://tdn.totvs.com/pages/releaseview.action?pageId=615606796)
