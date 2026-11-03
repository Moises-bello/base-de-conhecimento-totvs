---
article_id: 1500000470581
category: Encargos
content_hash: d4d8e30a40dd7a231ab5d1e6b3830c3639874175de6e0a21be2f77a1445569c8
fetched_at: '2026-06-28T22:46:53.269694+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RM - FOP - Lançamentos Financeiros PIS e FGTS 13º Salário
type: support-article
updated_at: '2025-03-05T19:36:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000470581-RM-FOP-Lan%C3%A7amentos-Financeiros-PIS-e-FGTS-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min**

**Dúvida**Como realizar os Lançamentos Financeiros de PIS e FGTS referente ao 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Referente ao FGTS 13º

O que ocorre é que se o lançamento financeiro for feito por dentro da SEFIP **recolhimento conforme SEFIP**, o valor do 13º estará embutido no valor devido ao fato de não existir uma guia separada para 13º.  
Se o lançamento for feito pela SEFIP e também na geração dos lançamentos, conforme imagens abaixo, será feito lançamento em duplicidade.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000537982/mceclip0.png)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000519262/mceclip0.png)  
  
Sendo assim, o ideal é que se já estão recolhendo na SEFIP o lançamento financeiro, não deverá realizar pela geração dos lançamentos, pois ele validará os códigos ativos presentes em cada parâmetro do lançamento.  
  
Segue materiais complementares:

[Lançamento Financeiro - Documentos de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=452719571)  
[Cadastros Financeiros](https://tdn.totvs.com/display/public/LRM/Cadastros+Financeiros)  
  
Referente ao PIS 13º

O sistema não realiza calculo de PIS automaticamente. Para efetuar tal lançamento para o financeiro, segue um exemplo:

Acessar Encargos | Cadastros Financeiros | Parâmetros e Incluir nova parametrização conforme imagem abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/fnAjgwfligeWLBhfFG4bzF2C5/?name=inline-900292747.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/vv0gLEv4Yly8XUdh7V69COEbr/?name=inline-379505748.png)​​  
  
Abaixo segue **exemplo** de como trazer o valor do PIS do evento de 13º salário na formula que foi inserida na parametrização acima:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101634313/mceclip0.png)  
  
Deverá informar código do evento de 13º salário que está lançado, por exemplo, para o evento de Código 129:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000528221/mceclip1.png)  
  
Texto da fórmula ficaria: C('0129') \* 0.01
