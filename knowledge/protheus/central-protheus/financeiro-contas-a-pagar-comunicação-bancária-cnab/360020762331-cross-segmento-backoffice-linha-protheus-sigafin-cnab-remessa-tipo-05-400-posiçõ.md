---
article_id: 360020762331
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: e2801c71b5b8cdf56338a2c849c0a1bb419bc0129efb9a4d4693e1d35e258554
fetched_at: '2026-06-28T22:37:55.000179+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CNAB - Remessa tipo
  05 - 400 posições
type: support-article
updated_at: '2025-07-22T20:30:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020762331-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Remessa-tipo-05-400-posi%C3%A7%C3%B5es
---

**Dúvida**Como gerar o registro detalhe tipo 5?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da versão 11.80.  
  
  
**Solução**  
O sistema permite gerar o registro complementar na remessa do CNAB de cobrança **modelo 1**.  
O registro Detalhe Tp 5 é normalmente usado para enviar o e-mail para o banco fazer o envio do boleto.  
Para ser gerada a segunda linha de detalhe é necessário que o cliente tenha o campo **"Boleto Email"(A1\_BLEMAIL)** configurado com o valor "Sim".  
Os modelos de 400 posições possuem outros registros detalhes opcionais e esse Detalhe Tp 5 pode ser utilizado como um desses registros opcionais desde que o campo no cliente esteja configurado.

**Importante**

Caso a empresa necessite de mais tipos, exemplo: ter o tipo 2 e também o tipo 5 ou tipo 5 e também o ter tipo 7, será necessário desenvolver o layout do formato modelo 2
