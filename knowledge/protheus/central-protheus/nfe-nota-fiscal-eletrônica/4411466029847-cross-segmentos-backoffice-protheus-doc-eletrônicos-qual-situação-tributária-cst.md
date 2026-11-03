---
article_id: 4411466029847
category: NFe - Nota Fiscal Eletrônica
content_hash: 97c754d046882ac07834f5dee92760e79419082fc0f72013e8c4b5688e4d5ed6
fetched_at: '2026-06-28T22:40:01.928687+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Qual situação
  tributária (CST) de  IPI que destaca o valor do imposto no XML e DANFE'
type: support-article
updated_at: '2021-10-25T21:00:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411466029847--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Qual-situa%C3%A7%C3%A3o-tribut%C3%A1ria-CST-de-IPI-que-destaca-o-valor-do-imposto-no-XML-e-DANFE
---

**Dúvida**  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Exemplo de **NÃO** destaque d**e IPI no XML**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015435991/mceclip2.png)**

Conforme está no Manual de Orientação do contribuinte da SEFAZ, **versão 6.00, páginas 210 e 211.**  
  
Os únicos CST de IPI que destacam o imposto são **00 e 49 para entrada, 50 e 99 para saída.**  
  
Se quer que o imposto seja destacado no **XML e DANFE deve utilizar um CST** que destaque o mesmo.  
  
Se não sabe qual o CST utilizar, entre em contato com a SEFAZ e questione a mesma qual CST informar nessa operação.

Use um CST diferente de **ISENTO, NÃO TRIBUTADO, ALIQUOTA ZERO, IMUNE ou SUSPENSAO** para o destaque do imposto.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015436091/mceclip3.png)

1- Preencher o campo **F4\_IPI "Calcula IPI" = S - Sim;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411468961687/mceclip0.png)

2- Para a correção preencher o CST do IPI, campo no TES **F4\_CTIPI** deve estar preenchido **Cod. trib. IPI;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057026893/mceclip0.png)

3- Após isso, **exclua a nota** e gere novamente.
