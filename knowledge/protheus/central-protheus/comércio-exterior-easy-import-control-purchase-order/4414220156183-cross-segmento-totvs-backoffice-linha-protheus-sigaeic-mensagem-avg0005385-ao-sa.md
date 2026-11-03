---
article_id: 4414220156183
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 9e8c5c5bce2ed78919f6c2e1285db919eb7199b9236cde535b5062f7cc1b1311
fetched_at: '2026-06-28T22:39:41.184093+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem AVG0005385
  ao salvar a purchase order
type: support-article
updated_at: '2021-11-29T12:32:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414220156183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-AVG0005385-ao-salvar-a-purchase-order
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao tentar salvar o Purchase Order (**EICPO400**) o sistema exta exibindo esta mensagem impeditiva: AVG0005385 Problema: Os códigos de despesas 102 e 103 se referem a despesas internacionais e de uso interno do sistema.  
Como fazemos para salvar o processo sem que exiba esta mensagem?

![AVG00005385.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4414204198295/AVG00005385.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**O parâmetro **MV\_1DUP** está configurado incorretamente. Esta parâmetro define inicialização da 1.parcela do titulo gerado no módulo Financeiro(SIGAFIN). Esta sequência pode ser iniciado por letra (A) ou número(1). Faça o ajuste do parâmetro **MV\_1DUP**  que o erro não será mais exibido.
