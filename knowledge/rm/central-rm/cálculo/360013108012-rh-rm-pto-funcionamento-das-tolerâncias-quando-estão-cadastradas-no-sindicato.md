---
article_id: 360013108012
category: Cálculo
content_hash: 57a5c030bd72af02d61f64f7468cca3f0d7a186bde3a303a27f8e54b36b17213
fetched_at: '2026-06-28T22:46:29.263335+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Funcionamento das tolerâncias quando estão cadastradas no sindicato
type: support-article
updated_at: '2025-02-19T15:22:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013108012-RH-RM-PTO-Funcionamento-das-toler%C3%A2ncias-quando-est%C3%A3o-cadastradas-no-sindicato
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408710436375)*****Tempo aproximado para leitura:** **00:01:00 min****Dúvida**Como funciona a aplicação das tolerâncias quando a mesma está cadastrada no sindicato?  
  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da 12.1  
  
**Solução**A tolerância cadastrada no sindicato **Automação de Ponto**, é aplicada de acordo com a quantidade de batidas a serem realizadas no dia e a natureza da batida, contabilizando também os intervalos de refeição do horário.

Segue exemplo para melhor entendimento.:

Foi definido os seguintes intervalos de tolerância no sindicato. Veja que o registro 4 - saída 2, está sem tolerância.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30090063454871)

Considera o cenário de um horário noturno em que o funcionário executou as seguintes batidas:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044300573)

No dia 18/06 a batida de 02:00 será considerada como 1 batida do dia e natureza saída-1;  
No dia 18/06 a batida de 03:01 será considerada como 2 batida do dia e natureza entrada-2;  
No dia 18/06 a batida de 05:42 será considerada como 3 batida do dia e natureza saída-2;  
No dia 18/06 a batida de 22:00 será considerada como 4 batida do dia e natureza entrada-3;

![](https://totvssuporte.zendesk.com/attachments/token/wb5LqjZ7D5J4oNXcPa3mNl76K/?name=inline-1265894143.png)

Neste cenário a batida de 05:42 não será tolerada, visto  que será considerada o cadastro do sindicato 4-saída-2 que não tem tolerância.

**Importante***- Quando no horário está cadastrado o limite de refeição, a tolerância do sindicato não é aplicada a atrasos ou extras.*  
*- Para tolerar estes intervalos, deve ser considerado a carência diária ou a tolerância do limite de refeição diretamente no cadastro do horário.*

**Saiba Mais**Para maiores informações sobre o intervalo de tolerância acesse o [**link**](https://tdn.totvs.com/pages/viewpage.action?pageId=452718979).  
Para informações sobre onde informar tolerância para o tipo de horário flexível, no sindicato ou horário? Acesse o [**link**](https://tdn.totvs.com/pages/releaseview.action?pageId=160105170).
