---
article_id: 9293765921559
category: TAF - REINF
content_hash: 4940604b5c20799b649f6ee3dda921ceee959f9fda06eb1a059fadc20d70e67a
fetched_at: '2026-06-28T22:41:34.690423+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF - Inclusão do valor da
  aposentadoria especial da REINF no TAF '
type: support-article
updated_at: '2023-03-31T16:46:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9293765921559-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Inclus%C3%A3o-do-valor-da-aposentadoria-especial-da-REINF-no-TAF
---

**Dúvida**Como incluir o valor adicional da aposentadoria especial da REINF diretamente no TAF.  
  
**Ambiente**A partir de 12.1.27  
  
**Solução**

  No layout da REINF consta tag para valor adicional conforme trecho do manual abaixo, nesta situação é necessário lançar a diferença em valor, esse valor irá complementar o valor gerado pelos 11% padrão.

**![Aposentadoria_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9293425161367/Aposentadoria_2.png)**   Para Inserir o valor adicional da aposentadoria especial, detalhe a nota fiscal lançada no documento de entrada do TAF(TAFA062E).

   -> Localize a aba 50 "Produtos e Serviços".

     -> Na linha dos impostos aba 51(tributos do item), localizar o lançamento da previdência"13".

       -> Preencha o valor adicional correspondente a quantidade de anos.

![Aposentadoria4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9293668284951/Aposentadoria4.png)

 Após o correto preenchimento e apuração da nota a informação pode ser confirmada no XML.

![aposentadoria_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9293626123671/aposentadoria_3.png)
